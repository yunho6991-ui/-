"""무협 게임 밸런스 모의실험 (docs/wuxia-balance.md).
한 생을 행동 단위로 돌려서 수명(행동 수) · 짧은 생 비율 · 도달 경지 · 천수 비율을 본다.
규칙은 wuxia-combat.md(3합 2선승 · 경지 차 = 기세 2배) · wuxia-traits.md(벽) · wuxia-game.md(수명)를 단순화.

실행: python3 tools/wuxia_sim.py           (기본 값)
     python3 tools/wuxia_sim.py 0.25       (탐험 중 전투 확률 바꿔 보기)
"""
import random, sys, statistics as st

REALMS = ['삼류', '이류', '일류', '절정', '초절정', '화경', '현경', '생사경']
NEED = [15, 35, 70, 120, 200, 320, 500]          # 다음 경지까지 숙련 점수
LIFE_BONUS = [0, 0, 0, 10, 20, 40, 60, 100]      # 경지별 최대 수명 보너스
ACT_DAYS = 10                                     # 행동 1번 = 10일
PER_DAY = 24                                      # 하루 행동 수

# 플레이 성향: 행동 비율(수련 · 탐험 · 의뢰 · 생업), 가는 지역 위험도(내 경지 기준 +n)
# up: 위험한 곳(+1)에 갈 확률, flee: 불리한 싸움에서 도망을 고를 확률
STYLES = {
    '평화': dict(mix=(0.05, 0.10, 0.00, 0.85), up=0.0, flee=1.0),
    '보통': dict(mix=(0.35, 0.35, 0.20, 0.10), up=0.2, flee=0.7),
    '모험': dict(mix=(0.20, 0.50, 0.30, 0.00), up=0.35, flee=0.5),
}
FIGHT_P = {'수련': 0.007, '탐험': 0.105, '의뢰': 0.21, '생업': 0.007}   # 행동마다 싸움이 날 확률(모의실험으로 조정)
KILL_P = [0.03, 0.05, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18]         # 지면 상대가 죽이기로 할 확률(지역 위험도별)
FLEE_OK = 0.6                                                       # 도망 성공 확률(실패하면 첫 합을 지고 시작)
WALL_P = 0.08                                                      # 벽 앞에서 수련 · 승리할 때마다 깨달음 확률
TALENT = [(0.6, 15), (1.0, 55), (1.5, 25), (2.0, 5)]               # (재능 배수, 비율)


def round_win(ratio):
    if ratio >= 2: return .9
    if ratio >= 1.3: return .7
    if ratio >= .8: return .5
    if ratio >= .5: return .3
    return .1


def fight(me, foe, injured, r, lost_first=False):
    ratio = 2 ** (me - foe) * (0.6 if injured else 1) * r.lognormvariate(0, 0.35)  # 랜덤 사건을 잡음으로
    w, l = 0, (1 if lost_first else 0)
    while w < 2 and l < 2:
        if r.random() < round_win(ratio): w += 1
        else: l += 1
    return w == 2


def life(style, r, fight_scale=1.0):
    s = STYLES[style]
    talent = r.choices([t for t, _ in TALENT], [w for _, w in TALENT])[0]
    lv, pts, acts, injured, heal = 0, 0.0, 0, 0, 0   # injured: 0 없음 · 1 경상 · 2 중상
    start_age = 15
    while True:
        acts += 1
        age = start_age + acts * ACT_DAYS / 365
        if age >= 60 + LIFE_BONUS[lv]:
            return acts, lv, '천수'
        if injured:
            heal -= 1
            if heal <= 0: injured = 0
        kind = r.choices(['수련', '탐험', '의뢰', '생업'], s['mix'])[0]
        if kind == '수련': pts += 1.0 * talent
        elif kind == '탐험':
            pts += 0.8 * talent
            if r.random() < 0.02 * (1 + lv - max(0, lv - 1) if s['up'] else 1):   # 기연(위험한 곳일수록 조금 더)
                pts += 20 * talent
        elif kind == '의뢰': pts += 1.0 * talent
        tier = lv + (1 if r.random() < s['up'] else 0)
        if r.random() < FIGHT_P[kind] * fight_scale:
            foe = max(0, tier + r.choice([-1, 0, 0, 1]))
            lost_first = False
            if foe > lv or injured == 2:
                if r.random() < s['flee']:
                    if r.random() < FLEE_OK: continue
                    lost_first = True
            if fight(lv, foe, injured, r, lost_first):
                pts += 3.0 * talent * (2 if foe > lv else 1)   # 강적을 이기면 두 배
                if lv < 7 and pts >= NEED[lv] and r.random() < WALL_P:
                    lv += 1; pts = 0
                if injured == 2 and r.random() < 0.15 and pts >= NEED[min(lv, 6)]:
                    lv = min(7, lv + 1); pts = 0      # 생사의 고비에서 벽을 넘음
            else:
                if r.random() < KILL_P[min(tier, 7)] + (0.4 if injured == 2 else 0):
                    return acts, lv, '사망'
                injured = 2 if (injured or r.random() < 0.4) else 1
                heal = 8 if injured == 2 else 3
                pts += 1.0 * talent                                   # 진 싸움에서도 배운다
                if injured == 2 and lv < 7 and pts >= NEED[lv] and r.random() < 0.10:
                    lv += 1; pts = 0                                  # 생사의 고비를 넘기며 벽을 넘음
        # 벽: 수련할 때만 깨달음이 온다(그냥 오래 산다고 넘지 않음)
        if kind == '수련' and lv < 7 and pts >= NEED[lv] and r.random() < WALL_P:
            lv += 1; pts = 0


def summarize(style, n=4000, seed=1, fs=1.0):
    r = random.Random(seed)
    res = [life(style, r, fs) for _ in range(n)]
    acts = sorted(a for a, _, _ in res)
    med = acts[len(acts) // 2]
    short = sum(1 for a in acts if a < 36) / n
    tenure = sum(1 for _, _, c in res if c == '천수') / n
    lvs = [l for _, l, _ in res]
    il = sum(1 for l in lvs if l >= 2) / n
    jl = sum(1 for l in lvs if l >= 3) / n
    hw = sum(1 for l in lvs if l >= 5) / n
    return med, med / PER_DAY, short, tenure, il, jl, hw, st.mean(lvs)


if __name__ == "__main__":
    fs = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    print(f"한 생 모의실험 · 성향별 4,000생 · 전투 빈도 ×{fs:g} · 하루 {PER_DAY}행동")
    print("성향 | 중간 수명(행동 · 실제 일) | 짧은 생 | 천수 | 일류↑ | 절정↑ | 화경↑ | 평균 경지")
    for style in STYLES:
        med, days, short, ten, il, jl, hw, avg = summarize(style, fs=fs)
        print(f"{style} | {med:>5}번 · {days:>4.1f}일 | {short:>5.0%} | {ten:>4.0%} | {il:>4.0%} | {jl:>4.0%} | {hw:>4.0%} | {REALMS[round(avg)]}({avg:.1f})")
