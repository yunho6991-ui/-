# 배 이야기 — 배마다 5화

> 메인 스토리(`fishing-story.md`, `fishing-story-allblue.md`)와 별개로 **배마다 짧은 이야기 5편**이 있다.
> 배가 **★ 오를 때마다 한 편씩 자동으로** 열린다(`ships-solo.md`의 "4레벨마다 ★"). 코드는 고치지 않았다.

## 규칙 (1순위 기준: 복잡하지 않게)

- **자동**: ★이 오르는 순간, 이미 보내는 "새 배 그림 + 한 줄" 밑에 이야기 2~3줄이 붙는다. 따로 할 일 없음.
- **새 명령 없음**: 다시 보기는 메인 스토리와 같은 `1이야기`.
- **새 그림 거의 없음**: 이야기 그림은 그 ★의 배 그림(`ship_<종류>_<등급>.jpg`)을 그대로 쓴다. 단골 NPC 초상화만 몇 장 새로(아래 프롬프트).
- **배를 바꾸면**(`1개조`): 새 배 이야기는 **지금 ★에 해당하는 편**부터 보여 준다. 앞 편들은 `1이야기`에서 볼 수 있다. 원래 배 이야기는 거기서 멈춰 있다가, 돌아오면 이어진다.
- **★5 편은 메인 스토리와 이어진다.** 배마다 다른 쪽에서 해솔의 이야기를 비춘다. 다섯 배 이야기를 다 보면 메인 스토리의 빈 곳이 채워진다(몰라도 메인 진행엔 지장 없음).

## 배마다 단골 NPC

| 배 | 단골 NPC | 한 줄 | ★5에서 이어지는 메인 이야기 |
|---|---|---|---|
| 🕸️ 트롤선 | **실타래 할매** | 항구 끝에서 그물을 짜는 할머니 | 해솔이 마지막으로 주문한 그물 |
| 🎣 어선 | **꼬마 물방울** | 낚시를 배우고 싶어 따라다니는 동네 아이 | 어린 해솔의 모습 |
| 💰 무역선 | **보따리 할멈** | 주문서를 대 주는 수상한 행상 할머니 | 용궁의 잔치 준비 |
| ⛴️ 여객선 | **준호와 미소** | 첫 손님이었던 신혼부부, 그리고 그 가족 | 해솔의 이름이 이어지는 이야기 |
| 🛡️ 방어선 | **순찰대장 한결** · **그림자 상인 무명** | 검문을 같이 하는 해군 대장과 쫓는 밀수꾼 | 재앙이 깨어난 이유 |

---

## 🕸️ 트롤선 — 「그물 아래의 노래」 (난이도 ●○○○○)

**★1 · 첫 그물**
> 🕸️ 첫 그물을 걷자 낡은 그물 조각이 같이 올라와요. 매듭이 꽃무늬처럼 예뻐요.
> 항구 끝에서 그물을 짜던 할머니가 손짓해요. "그거, 이리 줘 봐."

**★2 · 실타래 할매**
> 🧶 실타래 할매: "이 매듭은 우리 어머니 솜씨야. 백 년 전 거지."
> 할매가 새 그물을 하나 짜 줘요. "그물은 물고기만 잡는 게 아니야. 바다 이야기도 걸려 올라와."

**★3 · 걸려 올라온 것들**
> 🐚 요즘 그물에 이상한 게 자꾸 걸려요. 반짝이는 비늘, 부서진 노, 은빛 실 한 가닥.
> 실타래 할매: "은빛 실이라… 그건 어머니가 딱 한 번 쓴 실이야. 아주 특별한 그물에."

**★4 · 어머니의 장부**
> 📒 할매가 오래된 장부를 펼쳐요. 마지막 줄에 이름 하나가 적혀 있어요. "해솔 — 은빛 실 그물, 아주 큰 것."
> 실타래 할매: "물고기를 잡을 그물이 아니었대. 뭔가를 **감싸는** 그물이었다고."

**★5 · 심장을 감싼 그물**
> 💙 할매가 마지막 매듭을 묶어 그물을 완성해요. 할머니의 어머니가 못다 짠 무늬예요.
> 실타래 할매: "해솔 그 아가씨, 바다의 심장이 식지 않게 감쌀 그물을 주문했었대. 이제야 짝이 맞네."
> (메인: 해솔이 심장을 지키는 방법 — `fishing-story-allblue.md` 5장)

---

## 🎣 어선 — 「물방울의 낚싯대」 (난이도 ●●○○○)

**★1 · 따라오는 아이**
> 🎣 부두에서 꼬마 하나가 내 낚싯대만 쳐다봐요.
> 꼬마 물방울: "나도 낚시하고 싶어! 근데 낚싯대가 없어."

**★2 · 첫 붕어**
> 🐟 여분 낚싯대를 빌려줬더니, 물방울이 손바닥만 한 붕어를 낚았어요.
> 꼬마 물방울: "봤어? 봤어?! 내가 잡았어!" 하루 종일 붕어를 들고 다녀요.

**★3 · 놓친 녀석**
> 💧 큰 놈이 물었다가 줄이 끊어졌어요. 물방울이 울음을 터뜨려요.
> 바다곰 영감이 지나가며 한마디 해요. "허허, 놓친 놈이 있어야 다음 날 또 오는 거다."

**★4 · 내 낚싯대**
> 🎣 물방울이 자기 낚싯대를 만들어 왔어요. 삐뚤빼뚤하지만 제법이에요.
> 꼬마 물방울: "이제 나도 옆에서 같이 낚을래. 언젠가는 형/누나보다 큰 거 잡을 거야!"

**★5 · 은빛을 꿈꾸는 아이**
> 🌟 물방울이 처음으로 대물을 낚아 올렸어요. 영감이 그 모습을 오래 바라봐요.
> 바다곰 영감: "…해솔 그 녀석도 꼭 저 나이에 저렇게 웃었지."
> (메인: 어린 해솔의 기억 — 신화 선원 "천재 꼬마선장 해솔", 5-10 숨은 장면)

---

## 💰 무역선 — 「보따리 할멈의 주문서」 (난이도 ●●○○○)

**★1 · 첫 주문서**
> 🧾 보따리 할멈이 꼬깃꼬깃한 종이를 내밀어요. "고등어 세 마리만 구해 줘. 값은 두 배로 쳐 줄게."
> 🐤 무능: 두 배요?! 그럼 여섯 마리 값이네요! (맞음)

**★2 · 이상하게 꼼꼼한 주문**
> 📝 주문이 점점 구체적이에요. "참돔 한 마리, 크기는 50cm 넘는 걸로. 꼭 그랜드 라인 것."
> 할멈은 받은 물고기를 소금에 절이지도 않고 어딘가로 보내요.

**★3 · 요리 재료**
> 🍲 주문서를 다 모아 보니 하나의 요리법이에요. 백 가지 바다 재료로 만드는 잔치 음식.
> 보따리 할멈: "눈치챘구먼. 큰 잔치가 있어. 아주아주 오래 기다린 잔치."

**★4 · 용궁 도장**
> 🐉 주문서 귀퉁이에 처음 보는 도장이 찍혀 있어요. 용 모양이에요.
> 보따리 할멈: "쉿. 할멈은 그냥 심부름꾼이야. 용궁 수라간의."

**★5 · 돌아올 손님을 위한 잔치**
> 🎉 마지막 재료를 건네자 할멈이 허리를 펴요. 갑자기 키가 커 보여요.
> 보따리 할멈: "백 년 전 떠난 손님이 곧 숨을 돌린대. 그 손님 좋아하던 음식으로 상을 차려야지. …해솔이라는 아가씨야."
> (메인: 해왕류의 왕과 용궁, 5-9 결말 — 심장이 다시 뛰면 해솔이 쉴 수 있다)

---

## ⛴️ 여객선 — 「준호와 미소」 (난이도 ●●●○○)

**★1 · 첫 손님**
> 💑 첫 손님은 신혼부부예요. "그랜드 라인 섬에서 사진 찍고 싶어요!"
> 미소: "선장님 배가 첫 배예요? 우리도 첫 여행이에요!"

**★2 · 다시 찾아온 손님**
> 🧳 준호와 미소가 다시 탔어요. 미소가 배를 살짝 감싸 쥐어요.
> 준호: "이번엔 셋이서 탔어요. 아직 안 보이지만요."

**★3 · 작은 승객**
> 👶 이번엔 정말 셋이에요. 아기가 갑판 너머 바다를 보고 꺄르르 웃어요.
> 미소: "얘가 바다를 보면 울음을 뚝 그쳐요. 선장님 배라서 그런가 봐요."

**★4 · 혼자 온 꼬마 손님**
> 🎒 몇 해가 지나, 그 아이가 혼자 배낭을 메고 탔어요. "엄마 아빠가 선장님 배라면 혼자 가도 된대요!"
> 아이는 내내 키를 잡고 싶어 해요.

**★5 · 이어지는 이름**
> 🌅 아이가 내리면서 말해요. "나 커서 선장 될 거예요. 배 이름도 정했어요. **해솔호**!"
> 준호: "옛날에 바다를 지킨 사람 이름이래요. 이 배에서 처음 들었대요."
> (메인: 해솔의 이름이 사람들 사이에 다시 이어진다 — 본편 에필로그)

---

## 🛡️ 방어선 — 「그림자를 쫓는 배」 (난이도 ●●●●○)

**★1 · 해군의 부탁**
> ⚓ 순찰대장 한결: "요즘 수상한 배가 많소. 귀선이 좀 도와주시오. 검문은 선장 판단에 맡기겠소."
> 🐤 무능: 경찰 놀이다! (진짜임)

**★2 · 압수품**
> 🐚 검문에서 나온 밀수품 상자에 **해왕류의 비늘**이 잔뜩 들어 있어요.
> 순찰대장 한결: "비늘을 노리는 놈들이 있소. 살아 있는 해왕류에게서 억지로 뜯어낸 거요."

**★3 · 화난 바다**
> 🌊 비늘을 뺏긴 해왕류들이 사납게 날뛴다는 소문이 돌아요. 깊은 바다가 술렁여요.
> 순찰대장 한결: "그 뒤에 늘 같은 이름이 있소. **그림자 상인 무명**."

**★4 · 그림자의 꼬리**
> 🌑 안개 속에서 무명의 배를 놓쳤어요. 갑판에 쪽지 하나만 남았어요.
> 쪽지: "비늘을 모으면 올 블루로 가는 길이 열린다. 나는 선장님을 만나야 한다."

**★5 · 무명의 정체**
> ⛓️ 마침내 무명을 붙잡았어요. 두건을 벗긴 얼굴은 생각보다 앳돼요.
> 그림자 상인 무명: "우리 증조할아버지는 해솔 선장 배의 선원이었어. 선장을 찾으려고 비늘을 모았는데… 그게 바다를 깨운 줄은 몰랐어."
> 순찰대장 한결: "이제 알았으니 됐소. 깨운 바다는 우리가 같이 재우면 되오."
> (메인: 여덟 재앙이 깨어난 이유 하나 — 5-0 프롤로그, 방 공동 봉인)

---

## 메인 스토리와 이어지는 곳 정리

| 배 이야기 ★5 | 메인에서 비추는 것 | 메인 위치 |
|---|---|---|
| 트롤선 | 해솔이 심장을 지키는 방법(은빛 실 그물) | 5장 |
| 어선 | 어린 해솔 | 5-10 숨은 장면 · 신화 선원 꼬마선장 해솔 |
| 무역선 | 해솔을 기다리는 용궁의 잔치 | 5-9 결말 |
| 여객선 | 해솔의 이름이 이어짐 | 본편 에필로그 |
| 방어선 | 재앙이 깨어난 이유(비늘 밀수) | 5-0 프롤로그 |

> 메인 스토리는 어느 배를 타도 똑같이 다 볼 수 있다. 배 이야기는 "다른 각도에서 본 덤"이다.

---

## 코드에 넣을 때 (나중에 로컬에서)

- 메인 스토리와 같은 `story_seen` 표·`unlock` 함수를 쓴다. 장면 id: `ship:<종류>:<★>` (예: `ship:trawler:3`).
- ★이 오르는 곳(`_upgrade`에서 ★이 바뀔 때)에서 `unlock(..., f"ship:{kind}:{star}")` 하나 부르고, 돌려받은 글을 ★ 오름 메시지에 붙인다.
- `1개조`로 종류를 바꾼 직후에도 `unlock(..., f"ship:{new_kind}:{star}")` (앞 편은 열린 걸로만 표시하고 보내지는 않음).

---

## 그림 프롬프트 (ComfyUI)

> 이야기 그림은 ★별 배 그림을 그대로 쓴다. 새로 필요한 건 단골 NPC 초상화와 ★5 장면(선택)뿐이다.
> 스타일·크기는 `fishing-story-prompts.md`와 같다. 보따리 할멈·순찰대장 한결·그림자 상인 무명은 `season2-ships-prompts.md`의 `npc_cap_peddler` · `npc_cap_navy` · `npc_cap_smuggler`를 쓴다. 바다곰 영감은 `npc_bear.jpg`.

### 단골 NPC 초상화 (832×1216)

| 파일 | 프롬프트 |
|---|---|
| `npc_netgran.jpg` | `[스타일] Portrait of a tiny cheerful elderly Korean grandmother sitting on an upturned crate at the end of a harbor pier, weaving a large fishing net with intricate flower-like knots, a basket of colorful thread spools beside her, one silver thread glinting, warm sunset light.` |
| `npc_droplet.jpg` | `[스타일] Portrait of an energetic seven-year-old Korean child with a messy bowl haircut and a too-big straw hat, holding a crooked homemade fishing rod, sun-tanned cheeks and a gap-toothed grin, standing on a wooden dock with a bucket.` |
| `npc_couple.jpg` | `[스타일] Portrait of a sweet young Korean newlywed couple on a ferry deck, the husband with round glasses carrying two suitcases, the wife in a sun hat laughing and pointing at the sea, wind in their hair, bright cheerful morning.` |
| `npc_couple_family.jpg` | `[스타일] The same young Korean couple a few years later on a ferry deck, the husband with round glasses and the wife in a sun hat, now holding a giggling toddler who reaches toward the sea, warm family moment, golden light.` |

### ★5 장면 (선택, 1216×832)

| 파일 | 프롬프트 |
|---|---|
| `shipstory_trawler_5.jpg` | `[스타일] An elderly grandmother tying the final knot of an enormous shimmering net woven with glowing silver thread, the net spread across a pier at night, its pattern forming the shape of a beating heart, soft blue magical light.` |
| `shipstory_fisher_5.jpg` | `[스타일] A small child on a wooden dock hauling up a surprisingly huge fish with a crooked homemade rod, splashing water, an elderly bearded fisherman in a navy knit cap watching from behind with teary proud eyes, golden hour.` |
| `shipstory_merchant_5.jpg` | `[스타일] A grand underwater dragon palace banquet hall being prepared, long tables filled with seafood dishes, an old peddler grandmother standing tall in royal kitchen robes overseeing servants, a single empty seat of honor at the head of the table, festive warm lantern light.` |
| `shipstory_liner_5.jpg` | `[스타일] A young teenager with a backpack stepping off a ferry and turning back to wave, pointing proudly at a hand-painted toy boat in their hand, the ferry captain seen from behind waving back, sunrise over the harbor, hopeful mood.` |
| `shipstory_guard_5.jpg` | `[스타일] On an armored patrol ship deck, a young smuggler with a lowered hood looking down remorsefully, a fair naval captain placing a hand on his shoulder, a seized chest of glowing sea serpent scales open between them, stormy sky breaking into light.` |
