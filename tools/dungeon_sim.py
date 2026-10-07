"""카드 던전 난이도 모의실험 (docs/dungeon-game.md "난이도").
10층 던전 + 판 교체 방식: 10층 보스를 깨면 '내' 다음 판으로 넘어간다
(몬스터가 세지고, 내 소환 풀에서 반 구역(6~7장)이 빠지고 새로 들어온다).
하루 소환 수(채팅량 · 포인트 구매)에 따라 판을 며칠마다 넘기는지 본다.

실행: python3 tools/dungeon_sim.py              (기본: 몬스터 = 60 × 1.25^층 × 1.4^(판-1))
     python3 tools/dungeon_sim.py 70 1.25 1.35  (기본값 · 층 배수 · 판 배수)
"""
import random, sys
P = [60, 28, 9, 2.5, 0.45, 0.05]          # N R SR SSR UR LR
BASE = [10, 25, 60, 150, 400, 1000]
# 구역(13장)을 반으로 나눠 판마다 반 구역씩 교체한다. A=6장, B=7장 (등급: 장 수)
HALF = {'A': {0: 1, 1: 2, 2: 1, 3: 1, 4: 1}, 'B': {0: 2, 1: 1, 2: 2, 3: 1, 5: 1}}
HALVES = 10                                 # 첫 출시 5구역 = 반 구역 10개
ELEM = 5
FLOORS = 10
DAYS = 60


def half_cards(i):
    i %= HALVES                             # 카드가 바닥나면 처음부터 다시(실제로는 새 구역 추가)
    z, h = i // 2 + 1, 'AB'[i % 2]
    return [(z, h, g, k) for g, n in HALF[h].items() for k in range(n)]


def pool_of(pan):
    """pan판(1부터)의 소환 풀 = 반 구역 4개(26장). 판마다 가장 오래된 반 구역이 빠지고 다음 반 구역이 들어온다."""
    by = {}
    for i in range(pan - 1, pan + 3):
        for c in half_cards(i):
            by.setdefault(c[2], []).append(c)
    return by


def win_p(r):
    if r >= 1.5: return .98
    if r >= 1.0: return .85
    if r >= 0.7: return .50
    if r >= 0.5: return .20
    return .05


def sim(base, g, k, spd, seed, days=DAYS, runs=3, first=10, boss_bonus=5):
    """한 사람. 돌려주는 값: 날마다 '지금 몇 판째인지' 목록."""
    r = random.Random(seed)
    coll, elem = {}, {}
    pity, pan, bonus, bosses = 0, 1, first, 0
    hist = []
    for d in range(days):
        by = pool_of(pan)
        for _ in range(spd + bonus):
            pity += 1
            if pity >= 100: gi, pity = 4, 0
            else:
                gi = r.choices(range(6), P)[0]
                if gi >= 4: pity = 0
            if gi not in by: gi = 4 if 4 in by else 5   # 이번 판에 UR/LR 하나뿐일 때
            c = r.choice(by[gi])
            elem.setdefault(c, r.randrange(ELEM))
            coll[c] = min(5, coll.get(c, 0) + 1)
        bonus = 0
        dex = 1 + 0.005 * (len(coll) + bosses)        # 보스 카드도 도감 +1
        party = []
        for fe in range(ELEM):
            pw = sorted((BASE[c[2]] * (1 + 0.3 * (s - 1)) * (1.5 if elem[c] == (fe + 1) % ELEM else 1)
                         for c, s in coll.items()), reverse=True)
            party.append(sum(pw[:5]) * dex)
        for _ in range(runs):
            ok = True
            for f in range(1, FLOORS + 1):
                mon = base * g ** f * k ** (pan - 1)
                if r.random() >= win_p(party[r.randrange(ELEM)] / mon):
                    ok = False; break
            if ok:
                pan += 1; bosses += 1; bonus += boss_bonus   # 남은 탐험은 다음 판에서(새 풀은 다음 소환부터)
        hist.append(pan)
    return hist


def med(v):
    v = sorted(v); return v[len(v) // 2]


def first_day(h, p):
    for d, x in enumerate(h):
        if x >= p: return d + 1
    return None


if __name__ == "__main__":
    base = float(sys.argv[1]) if len(sys.argv) > 1 else 60
    g = float(sys.argv[2]) if len(sys.argv) > 2 else 1.25
    k = float(sys.argv[3]) if len(sys.argv) > 3 else 1.4
    N = 200
    print(f"몬스터 = {base:g} × {g:g}^층 × {k:g}^(판-1) · 탐험 하루 3번 · 첫날 무료 10번 · {N}명")
    print("하루 소환        | 1판 클리어 | 7일째 | 14일째 | 30일째 | 60일째  (중간값, 몇 판째)")
    rows = [(2, "채팅 100마디"), (4, "채팅 200마디"), (6, "채팅 300마디"), (12, "채팅 600마디"),
            (6 + 2, "300마디+포인트 2번"), (6 + 5, "300마디+포인트 5번")]
    for spd, label in rows:
        hs = [sim(base, g, k, spd, s) for s in range(N)]
        fc = [first_day(h, 2) or 999 for h in hs]
        m = med(fc)
        cols = [med([h[d - 1] for h in hs]) for d in (7, 14, 30, 60)]
        print(f"{label:<14}({spd:>2}번) | {str(m) + '일째' if m != 999 else '못 깸':>8} | "
              + " | ".join(f"{c:>4}판" for c in cols))
