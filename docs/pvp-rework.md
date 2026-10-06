# 약탈 개편 — 유저끼리 털지 않게

> 유저가 유저를 터는 약탈은 순간의 도파민은 크지만, 털린 쪽 기분이 나빠서 전체적으로는 싫어하는 분위기다.
> 이 문서는 **짜릿함은 남기고 피해자는 없애는** 안이다. 코드는 고치지 않았다.

## 무엇이 재밌고 무엇이 싫은가

| 재밌는 것 (남긴다) | 싫은 것 (없앤다) |
|---|---|
| 기습이 성공하는 순간 | 내 오늘 수익이 남에게 넘어감 |
| 포격·돌격·방어 가위바위보 심리전 | 자고 일어나니 털려 있음 |
| 전리품, 약탈왕 랭킹 | "누가 날 털었지" 하는 앙금, 복수 |
| 위험한 바다일수록 크게 먹는 긴장감 | 털리지 않으려고 보호막을 사야 함 |

→ **상대를 유저에서 NPC로 바꾸면** 왼쪽은 그대로 남고 오른쪽은 전부 사라진다.

---

## ⭐ 추천안: 약탈 상대를 NPC로

**규칙 한 줄: "바다에서 만나는 배는 이제 NPC다. 털어도 털려도 유저끼리 주고받는 건 없다."**

### 1. 내가 터는 쪽 — NPC 상선 기습 (`1약탈`, 지금 명령 그대로)

- 낚시하다 가끔 **NPC 상선**을 만난다. 결과 끝에 한 줄:
  `⛵ 상선 발견! 크기: 중 · 1약탈 / 1지나가기`
- **크기**(소·중·대)가 클수록 성공률은 낮고 전리품은 크다. 한 줄로 보이는 유일한 판단 거리.
- **성공**: 전리품(포인트)은 **시스템이 준다.** 아무도 잃지 않는다.
- **실패**: 반격으로 배가 잠깐 부서진다(지금 있는 "기습 들켰을 때 파손"과 같은 규칙). **배상금은 없다**(줄 사람이 없으니).
- 대포·해적 선원은 그대로 성공률·전리품을 올린다. 안 고르고 다음 낚시를 하면 그냥 지나간다.

| 크기 | 성공률 (예) | 전리품 (예) |
|---|---|---|
| 소 | 70% | 오늘 낚시 수익의 5% |
| 중 | 50% | 10% |
| 대 | 30% | 20% |

### 2. 나를 습격하는 쪽 — NPC 해적 (`1포격`·`1돌격`·`1방어`, 지금 명령 그대로)

- 위험한 바다에서 가끔 **NPC 해적**이 습격해 온다. 결과 끝에 한 줄:
  `🏴‍☠️ 검은이빨 고드가 습격해 와요! (돌격을 좋아한대요) · 1포격 / 1돌격 / 1방어`
- 해적 선장마다 **버릇**이 있어서 한 줄 힌트가 나온다 → 가위바위보 심리전이 그대로 산다.
- **이기면** 전리품(시스템이 줌). **지면** 배가 잠깐 부서진다(느려짐). **포인트는 잃지 않는다.**
- **시간 압박 없음**: 해적은 내가 답할 때까지 기다린다. 답하지 않고 다음 낚시를 하면 무작위 수로 싸운다(지금도 맞서지 않으면 무작위).
- 선체·목수 선원은 그대로 "덜 부서짐"으로 쓰인다.

| 해적 선장 | 버릇 (힌트) |
|---|---|
| 검은이빨 고드 | 돌격을 좋아한다 |
| 쌍칼 미나 | 방어부터 한다 |
| 포탄 할배 | 포격밖에 모른다 |
| 변덕쟁이 롤로 | 힌트 없음 (진짜 무작위) |

> 버릇은 "60% 정도 그 수"로. 힌트를 믿으면 유리하지만 확실하진 않다.

### 3. 해역 위험도는 그대로

- 지금 해역별 "다른 배를 만날 확률"(`Zone.meet`)을 **NPC를 만날 확률**로 그대로 쓴다.
- 이스트 블루: NPC 해적 없음(평화) · 그랜드 라인: 보통 · 신세계: 해적 많고 상선 큼 · 올 블루: 가장 위험하고 가장 크게 먹는다.
- 날씨도 그대로: 안개 → 아무도 못 만남, 폭풍 → 해적 2배.

### 4. 방 분위기는 그대로

- **약탈왕 랭킹**: NPC에게서 뺏은 전리품 기준으로 그대로 집계(`plunder_ranking`).
- 큰 전리품·대형 상선 털기 성공은 방에 한 줄 자랑(지금 전설 알림과 같은 방식).
- 유저끼리 미워할 일은 없고, "오늘 대형 상선 털었다" 같은 자랑만 남는다.

---

## 없어지는 것 (하나 넣으면 여러 개 빼기)

| 없어지는 것 | 지금 명령·설정 | 이유 |
|---|---|---|
| 유저 기습 · 유저 선상싸움 | (조우 대상이 유저일 때) | 상대가 NPC로 바뀜 |
| 털림 알림 | 알림 "털림" | 털릴 일이 없음 |
| 보호막 | `1보호막` | 막을 대상이 없음 |
| 몸값 · 약탈 빚 | `1몸값` (이미 보호막으로 바뀜), 빚 자동 상환 | 빚이 생기지 않음 |
| 대물 빚 (진 쪽 다음 대물 1마리 뺏김) | (자동) | 유저 간 이동 없음 |
| 기습 실패 배상금 | (자동) | 줄 상대가 없음 |
| 하루 공격받는 횟수 제한 | `RAID_TARGET_DAILY`, `_attack_capped` | 필요 없음 |
| 태세 | `1태세` | 이미 안내만 남은 기능 |

> 명령 3~4개와 규칙 여러 개가 빠진다. 새로 생기는 명령은 **없다**.

### 선원·배 능력은 상대만 바뀐다

> ⚠️ 해적·목수 선원은 이후 **혼자 플레이 능력으로 재설계**했다(해적 = 보물·전리품 +, 목수 = 강화 비용 −). 최신은 `crew-traits.md` 맨 아래. 아래 표는 첫 안.

| 능력 | 지금 | 바뀐 뒤 |
|---|---|---|
| 해적 선원 | 유저 기습 성공률 ↑, 더 뺏음 | NPC 상선 기습 성공률 ↑, 전리품 ↑ |
| 목수 선원 | 유저에게 덜 털림, 파손 ↓ | NPC 해적에게 졌을 때 파손 ↓ (덜 뺏김 부분은 없어짐 → 대신 파손 감소를 조금 키움) |
| 신화 목수 "요새" | 뺏기는 양 ×, 기습 실패자 배상 × | NPC 해적에게 **지지 않고 비김** 확률 ↑ 같은 하나로 단순화 |
| 대포 · 선체 강화 | 유저 싸움 몫 | NPC 싸움 몫 (같은 숫자 그대로) |
| 방어선 | 도발 · 철벽 | ⚔️ **전투선**으로 바뀜: 현상수배 해적과 싸우고, NPC 해적과 비기면 이김 (`ships-solo.md`) |

### 바꿀 때 정리
- 남아 있는 **약탈 빚은 전부 탕감**(빚진 사람에게 알림 한 줄).
- 남은 **보호막 시간은 포인트로 환불**(남은 비율만큼).
- "털림" 알림 설정은 그냥 무시.

---

## (선택) 유저끼리 붙는 재미가 아쉽다면 — 친선 대결

> 추천안만으로도 충분하다. 그래도 "친구랑 붙는 맛"이 아쉬우면 이거 하나만.

- `1대결 [닉]` → 상대에게 가위바위보 대결 신청. **판돈 없음.**
- 이긴 사람은 **시스템이** 소소한 보상(미끼 1개 등). 진 사람은 **아무것도 안 잃는다.**
- 상대가 답하지 않으면 무작위 수로 처리(지금 선상싸움과 같음). 하루 n번까지.
- 새 명령 1개. 1순위 기준상 ⚠️(조건부)라서 정말 원할 때만. (backlog K-06과 같은 것)

---

## 다른 방법들 (추천하지 않음)

| 방법 | 내용 | 왜 안 하나 |
|---|---|---|
| 해적 깃발 | 깃발 단 사람끼리만 서로 털 수 있음 | 설정이 하나 생기고, 깃발 단 사람들 사이엔 피해자가 그대로 남는다 |
| 피해 상한 · 신규 보호 · 새벽 금지 | 털리는 양·시간을 제한 | 덜 아플 뿐 "털린다"는 기분은 그대로 |
| 그림자 약탈 | 성공하면 시스템이 주고 상대는 안 잃음, 알림만 감 | 상대는 "털렸다" 알림만 받고 아무 일도 없어서 어색하다 |

> 추천안을 고르면 backlog의 L-01 현상금, L-02 복수, L-05 새벽 금지, L-06 평화 모드, G-03 피해 상한, D-05 신규 보호막, S-05 같은 상대 반복 제한은 **필요 없어진다.**

---

## 그림 프롬프트 (ComfyUI)

> 스타일 고정 문구와 크기는 `fishing-story-prompts.md`와 같다. NPC 해적선 그림은 `season2-ships-prompts.md`의 `npc_ship_pirate.jpg`를 같이 쓴다.

| 파일 | 크기 | 프롬프트 |
|---|---|---|
| `npc_merchant_s.jpg` | 1216×832 | `[스타일] A small chubby merchant sailboat loaded with a few barrels and sacks, a nervous plump merchant at the helm, calm sea, easy target, comedic mood.` |
| `npc_merchant_m.jpg` | 1216×832 | `[스타일] A mid-sized merchant brigantine with striped sails and crates stacked on deck, two armed guards on the railing, steady sea, moderate challenge.` |
| `npc_merchant_l.jpg` | 1216×832 | `[스타일] A huge treasure-laden merchant galleon with golden trim, cannons along its sides, chests of gold visible on the open deck, escort flags flying, high-stakes target, dramatic sunset.` |
| `npc_pirate_god.jpg` | 832×1216 | `[스타일] Portrait of a burly pirate captain called Black Tooth, wild black beard with beads, one shining gold front tooth in a wide grin, charging forward with a cutlass raised, aggressive reckless pose.` |
| `npc_pirate_mina.jpg` | 832×1216 | `[스타일] Portrait of a calm cunning female pirate captain with twin curved swords crossed in a defensive guard, short dark hair, eye patch, red sash, patient watchful expression.` |
| `npc_pirate_grandpa.jpg` | 832×1216 | `[스타일] Portrait of a cheerful elderly pirate gunner with a huge white mustache, soot-covered face, hugging a small cannon like a pet, cannonballs stacked behind him, explosive comedic energy.` |
| `npc_pirate_rolo.jpg` | 832×1216 | `[스타일] Portrait of an unpredictable young pirate captain with mismatched clothes, one boot one sandal, spinning a dice in his fingers, chaotic grin, swirling confetti-like sea spray.` |
