# 무협 게임 — 데이터 형식 (코드로 옮길 때 기준)

> 기획 문서의 내용을 **코드가 읽는 데이터**로 옮기는 형식. 원칙(기획서 11장): **사건 · 사람 · 무공을 추가할 때 코드를 고치지 않는다** — 데이터 파일에 한 덩어리 더하면 끝.
> 데이터: `data/wuxia/*.yaml`. **작은 강호 한 판(농부 서막 · 청하진 · 청운산) + 거지 서막 · 낙양은 완성** — 로드맵 M0~M5에 바로 쓴다. 나머지는 기획 문서를 보고 같은 꼴로 채운다.
> 검사: `python3 tools/wuxia_data_check.py` — 형식 · id 중복 · 없는 id 참조를 확인.

---

## 1. 파일 구성

| 파일 | 내용 | 기획 문서 |
|---|---|---|
| `world.yaml` | 세계 변수 · 경지 · 시간 상수 · 확률 기본값 | `wuxia-game.md` · `wuxia-balance.md` |
| `factions.yaml` | 세력 14 | `wuxia-world.md` 3장 |
| `places.yaml` | 지역 · 시작 고을 · 대도시 | `wuxia-world.md` · `wuxia-early.md` · `wuxia-towns.md` · `wuxia-cities.md` |
| `traits.yaml` | 성격 · 체질 · 숨겨진 특성 · 생김새 · 재능 · 특기 · 유산 | `wuxia-game.md` 4장 · `wuxia-traits.md` |
| `martial.yaml` | 무공(심법 · 무공 · 신법) | `wuxia-martial.md` |
| `npcs.yaml` | NPC(핵심 · 고을 사람 · 히로인 · 남성 인연) | `wuxia-npcs.md` · `wuxia-heroines.md` · `wuxia-heroes.md` |
| `origins.yaml` | 출신(정원 · 시작 조건 · 서막 단계 · 결말) | `wuxia-origins.md` · `wuxia-prologues*.md` |
| `events/*.yaml` | 사건(지역별 · 세력 · 꼬리표 · 막 · 서막) | `wuxia-events*.md` · 서막 대본 |
| `texts.yaml` | 문장 풀 | `wuxia-texts.md` |

- **id 규칙**: 영문 소문자 + 밑줄. 앞에 종류: `ev_` 사건 · `npc_` · `org_` 출신 · `ma_` 무공 · `pl_` 장소 · `fac_` 세력 · `tr_` 특성 · `lg_` 유산.
- **보이는 글은 한국어**, 키 이름은 영어.

---

## 2. 조건 — `require` (한 줄 문자열 목록, 모두 맞아야 함)

| 꼴 | 뜻 | 예 |
|---|---|---|
| `realm>=일류` | 경지 | `realm<절정` |
| `tag:이름` / `!tag:이름` | 꼬리표가 있다 / 없다 | `tag:농부출신` |
| `skill:이름>=단계` | 특기(서툶 · 능숙 · 달인) | `skill:의술>=능숙` |
| `looks:이름` | 생김새(얼굴 · 체격 · 특징) | `looks:험상궂음` |
| `trait:이름` | 성격 · 체질 · (드러난) 숨겨진 특성 | `trait:호기심` |
| `talent:갈래>=배수` | 재능 | `talent:검>=1.5` |
| `region:이름` / `place:id` | 지역 종류 / 특정 장소 | `region:산` · `place:pl_qinghe` |
| `act:a-b` | 시즌 막(0 = 메인 전) | `act:1-2` |
| `var:이름 op 값` | 세계 변수 | `var:ritual>=70` |
| `aff:npc_id op 단계` | 호감도(원수~심복) | `aff:npc_hongmae>=신뢰` |
| `faction:fac_id` | 소속 | `faction:fac_kaibang` |
| `money>=n` · `age>=n` · `gender:여` | 돈 · 나이 · 성별 | |
| `seen:ev_id` / `!seen:ev_id` | 이번 생에 겪은 사건 | `seen:ev_v09` |

## 3. 가중치 — `weight` + `weight_mod`

```yaml
weight: 20                 # 기본
weight_mod:                # 조건이 맞으면 더하거나(+) 곱한다(x)
  "looks:곱상함": +10
  "trait:다혈질": x1.5
  "act:3-7": x0
```

## 4. 결과 — `result` (모두 선택 사항)

| 키 | 뜻 | 예 |
|---|---|---|
| `money` | 돈(± · 비율 가능) | `-30` · `"-50%"` |
| `pts` | 숙련(갈래 또는 무공 id) | `{검: 2}` · `{ma_samjae: 1}` |
| `learn` | 무공 · 특기 얻기 | `[ma_samjae]` · `{skill: 의술}` |
| `injury` | 부상(경상 · 중상 · 불구:부위) | `중상` |
| `poison` | 독(일수) | `3` |
| `aff` | 호감도 변화 | `{npc_noseok: +2}` |
| `rep` | 세력 평판 | `{fac_greenwood: -1}` |
| `fame` / `infamy` | 명성 · 악명 | `+5` |
| `world` | 세계 변수 | `{ritual: -10}` |
| `tag` | 꼬리표 붙이기 · 떼기 | `[+녹림원한, -추격자]` |
| `item` | 물건 | `[it_soguhandan]` |
| `clue` | 시작 사건 단서(같은 갈래 셋이면 시작) | `blood_cult` |
| `fight` | 전투(상대 · 대수) | `{foe: npc_bandit, count: 3}` |
| `death_check` | 사망 판정 확률 | `0.3` |
| `next` | 이어지는 사건 | `ev_v09_track` |
| `ending` | 서막 결말 | `end_farmer_disciple` |
| `record` | 생애 기록 한 줄(전기용) | `"산적이 온 날 살아남았다"` |
| `text` | 결과 문장 | `"허리가 끊어질 것 같지만, 저녁밥이 달다."` |

### 4-1. 작은 강호 데이터에서 더 쓴 키 (`events/prologue_farmer.yaml` · `qinghe.yaml` · `romance_qinghe.yaml`)

| 키 | 뜻 |
|---|---|
| `roll: [{p, result}]` | 확률로 결과 하나 고르기 |
| `heal: n` · `sick: p` | 부상 회복 · 병에 걸릴 확률 |
| `stat: {체력: +1}` | 기본 능력 변화 |
| `skill_xp: {특기: n}` | 특기 숙련 경험 |
| `rumor: n` · `clue_relic: local` | 소문 · 기연 단서 |
| `shop: market` · `discount` · `gamble: n` · `quest_board: bounty` | 장터 · 흥정 할인 · 도박 · 의뢰판 열기 |
| `move: random_neighbor` · `move_menu: river` | 이동 |
| `cost_actions: n` | 이 선택이 행동력을 n 더 씀(여러 날 걸리는 일) |
| `world_local: {키: 값}` | 그 장소만의 상태(마을 피해 등) |
| `set_npc: {npc: 상태}` · `kill_npc_p: {npc: p}` | NPC 상태 바꾸기 · 확률로 죽이기 |
| `pick_npc: [..]` (사건 키) · `"{npc}"` · `"{passerby}"` | 회차마다 등장 인물 고르기 · 그 인물 자리 표시 |
| `fight: {foe, count, ally, lost_first, win: {...}, lose: {...}}` | 전투 + 이겼을 때 · 졌을 때 결과 |
| `ally: npc` · `master: npc` · `romance: {npc: 연모}` | 동료 · 스승 · 인연 단계 |
| `epithet_seed: 이름` | 별호 후보 쌓기 |
| `reveal: tr_id` · `wall_chance: p` · `flag: 이름` | 숨은 특성 드러내기 · 벽 넘기 기회 · 표시 |
| `check: {aff: "npc>=단계"}` · `{trait_any: [...], else_p}` | 호감 · 성격으로 판정 |
| 조건 `literacy` · `alive:npc_id` · `item:it_id` · `flag:이름` | 글을 앎 · NPC가 살아 있음 · 물건을 가짐 · 표시가 있음 |
| `item_remove: [..]` · `regression_piece: n` | 물건 내주기 · 회귀 비밀 조각(천기록 n번, `wuxia-regression.md`) |
| `main_start: 이름` · `reveal_trait: tr_id` · `insight: n` · `deviation_p: p` | 메인 시작 사건을 터뜨림(W11) · 숨은 특성 드러냄 · 깨달음 · 주화입마 확률 |
| 출신 `variants` · 조건 `variant:이름` · `{variant_*}` | 한 출신 안의 갈래(화산 · 무당) — 빙의 때 하나를 고르고, 사건 · 결말의 `{variant_…}` 자리에 그 값이 들어감 |
| 사건 `mirror: ev_id` · 출신 `looks_bias` | 다른 출신의 같은 사건을 반대편에서(녹림 2-3 ↔ 농부 습격 — 결과가 같은 세계에 쌓임) · 출신이 생김새를 기울임 |
| `romance_open: npc` · NPC `age_as_romance` | 인연 루트만 열어 둠 — **나와 상대 모두 성인일 때만** 인연 진행(어린 출신 서막은 열기만) · 미성년 동기는 성인 나이로 다시 만남 |
| `text_if: {"조건": "문장"}` | 조건이 맞으면 본문을 바꿔 보여 줌(표국 3-1 "…열어 봤군.") |
| 출신 `init.journal` | 빙의 화면의 `[일지]` 한 줄 |
| 결말 `faction_hidden` · `hidden` | 본인도 모르게 세력에 묶임 · 숨은 후속(꿈 · 다음 의뢰) |

## 5. 선택지 — `choices`

```yaml
choices:
  - text: 싸운다
    require: []                 # 이 선택지가 보일 조건(특기 · 생김새로 열림)
    show_reason: ""             # 열린 이유 표시 "(험상궂은 얼굴)"
    check: {stat: 신법, dc: 50}  # 판정(없으면 바로 result)
    success: {...}              # check 성공
    fail: {...}                 # check 실패
    result: {...}               # check 없을 때
```

---

## 6. 종류별 형식

### 사건 `events/*.yaml`
```yaml
- id: ev_v09
  name: 사라진 아이
  region: 마을                 # 또는 place: pl_qinghe
  weight: 12
  require: ["act:1-2"]
  death_possible: true
  main: true                  # 메인 사건(전체의 15% 안팎 — 그 지역 · 꼬리표가 없으면 소문으로만)
  text: "이웃집 아이가 밤새 돌아오지 않았다. 문간에 붉은 진흙 발자국이 찍혀 있다."
  choices: [...]
  record: "사라진 이웃집 아이의 일을 겪었다"
  memory_key: blood_cult_kidnap   # 전생 기억 · 원한 연결
```

### NPC `npcs.yaml`
```yaml
- id: npc_hongmae
  name: 홍매
  age: 41
  gender: 여
  realm: 이류
  hidden_realm: true
  looks: {face: 요염함, build: 보통}
  personality: 냉정
  faction: fac_kaibang
  place: pl_qinghe
  role: 객잔 주인            # 역할 틀
  goal: "객잔을 지키는 것"
  secret: "개방의 청하진 연락책. 구장로의 지시를 의심한다"
  action: "소문을 모으고, 개방에 보고한다"   # 세계가 하루 한 번 돌릴 때 하는 일
  speech: "외상은 사절이고, 칼은 문밖에 두고 들어와."
  reactions:                 # 호감 단계별 반응(없으면 기본 문장)
    경계: "값을 두 배로 부른다"
    호의: "소문 하나를 공짜로 알려 준다"
    신뢰: "개방에 연결해 준다"
    심복: "구장로가 수상하다고 털어놓는다"
  growth: []                 # 성장 조건
  death: ["ev_a305:실패"]     # 사망 조건
  on_death: {world: {}}      # 죽으면 생기는 일
  romance: null              # 히로인 · 남성 인연이면 아래 꼴
```
히로인 · 남성 인연은 `romance`를 채운다:
```yaml
  romance:
    stages:
      관심: ev_h_xueying_1
      신뢰: ev_h_xueying_2
      연모: ev_h_xueying_3
    branch: ev_h_xueying_branch
    marriage_once: true      # 혼인은 세계에 한 번
```

### 출신 `origins.yaml`
```yaml
- id: org_farmer
  name: 농부의 아이
  grade: 흔함                # 흔함 · 드묾 · 희귀 · 전설
  cap: null                  # 정원(고정 출신만), null = 무제한
  shared_prologue: false     # 공유 서막(세계 · 실제 날짜로 흐름)
  start: {age: 14, money: 5, literacy: false, places: [town]}   # town · city · 특정 place id
  gender: random             # 또는 여 / 남
  init: {skills: {농사: 능숙}, martial: []}
  stages:
    - id: st_farmer_1
      name: 평범한 마을
      days: null             # 공유 서막이면 실제 날짜 수
      fixed: [ev_p_farmer_1_1]          # 반드시 나오는 사건(★)
      pool: [ev_p_farmer_1_2, ev_p_farmer_1_3, ev_p_farmer_1_4, ev_p_farmer_1_5, ev_p_farmer_1_6]
      pick: 3
  endings:
    - id: end_farmer_disciple
      name: 노석의 제자
      to: {place: same, faction: null}
      tags: [농부출신, 노석의제자]
```

### 무공 `martial.yaml`
```yaml
- id: ma_namgung_sword
  name: 창궁무애검
  layer: 무공                # 심법 · 무공 · 신법
  branch: 검                 # 검 · 도 · 권장 · 암기 · 신법 · 내공
  grade: 신공                # 삼류 · 이류 · 일류 · 절정 · 신공 · 전설
  nature: 쾌                 # 쾌 · 중 · 유 · 변
  qi: 정                     # 정 · 불 · 마 · 혈 · 요 · 독
  need_realm: 일류
  need_literacy: true        # 비급으로 익힐 때
  faction_lock: fac_namgung  # 밖에서 쓰면 원한
  power: 1.8
  qi_deviation: 낮음
  cap: null                  # 전설 기연이면 1
  lines: ["하늘을 가르는 검광이 세 갈래로 갈라진다", "끝없는 창공처럼 칼이 넓어진다"]
```

### 장소 `places.yaml`
```yaml
- id: pl_qinghe
  name: 청하진
  kind: town                 # town · city · region · site
  region: 중원
  tier: 0                    # 위험도(0 초반 ~ 3 최종)
  start_for: [org_farmer, org_hunter, org_inn, org_doctor, org_escort]
  spots: [나루터, 장터, 객잔, 의원, 표국, 관아, 서당, 청운산]
  threat: 녹림 산적          # 서막 2단계 위협
  clue: [blood_cult, yaoshou]
  links: {pl_luoyang: 5}     # 이동 행동 수
```

### 세계 `world.yaml`
```yaml
time: {action_days: 10, regen_minutes: 60, max_stock: 20, world_day_per_real_day: 30}
realms: [삼류, 이류, 일류, 절정, 초절정, 화경, 현경, 생사경]
life_bonus: [0, 0, 0, 10, 20, 40, 60, 100]
short_life_actions: 36
vars:
  ritual: {name: 혈교 의식 진행도, start: 0, min: 0, max: 100}
```

### 문장 `texts.yaml`
```yaml
round_win: ["{초식}이 {상대}의 빈틈을 파고든다", "한 걸음 빨랐다"]
```

---

## 7. 세계를 하루 한 번 돌릴 때 (배치)

1. 강호 날짜 +30일(메인이 깨어난 뒤에만).
2. NPC마다 `action` 실행 · 성장 조건 · 사망 조건 확인.
3. 세계 변수에 따라 막 넘김(`wuxia-season1.md`).
4. 공유 서막 단계 넘김(실제 날짜).
5. 강호 일보 만들기(`texts.yaml`의 틀).
