# 메인 스토리 — 그림 프롬프트 (사람은 매력 있게 · 생물은 귀엽게, ComfyUI)

> `docs/fishing-story.md`(발랄 버전)의 장면·인물 그림. **귀엽고 발랄한 화풍**으로 다시 썼다.
> Krea2 기준 자연어 영어 문장. 파일 이름은 기존 규칙 그대로.
> 물고기·선원 그림은 `docs/art-cute-prompts.md`.

## 공통 설정

| 항목 | 값 |
|---|---|
| 장면(가로) | 1216 × 832 |
| 인물 카드(세로) | 832 × 1216 |
| 아이템(정사각) | 1024 × 1024 |
| 저장 | JPG, 긴 변 1200px 안팎 |

### `[장면]` 스타일 문구 (스토리 장면 · 인물 카드 앞에 — 모든 스토리 프롬프트 공통)

```
Bright anime storybook illustration, attractive expressive characters, cute rounded sea creatures, vibrant cheerful colors, soft cinematic lighting, clean lineart, uplifting mood, no text, no letters, no watermark.
```

> 사람은 **매력 있게**(귀엽거나·잘생기거나·아름답거나·섹시하게), 물고기·동물·유령·마스코트는 **귀엽게**. 물고기·선원 단독 그림은 `art-cute-prompts.md`의 `[귀여움]`(물고기) · `[선원]`(사람) 문구.

### (참고) `[귀여움]` 스타일 문구 — 물고기·동물용

```
Cute kawaii storybook illustration, soft pastel colors, rounded chubby shapes, big sparkly eyes, gentle cel shading, soft clean outlines, cheerful warm lighting, simple uncluttered composition, no text, no letters, no watermark.
```

### 공통 네거티브 (쓰는 워크플로일 때만)

```
scary, creepy, horror, gore, realistic, photorealistic, sharp teeth, menacing, dark gloomy, text, watermark, extra limbs, deformed
```

### 인물 고정 묘사 (얼굴이 매번 달라지지 않게)

장면에 그 인물이 나오면 아래 문장을 **그대로** 넣는다. 각 프롬프트 앞의 `[귀여움]`은 이제 `[장면]`으로 읽는다. 인물 카드를 먼저 뽑고 마음에 드는 걸 참조 이미지(IPAdapter / Redux)로 걸면 장면에서도 같은 얼굴로 나온다.

| 인물 | 고정 문구 |
|---|---|
| 바다곰 영감 | `a charming burly old fisherman grandpa with a big fluffy white beard, rosy cheeks, twinkling kind eyes, a faded navy knit beanie, a patched yellow raincoat vest` |
| 해솔 | `a beautiful lively young woman with long dark hair in a loose side braid, a sea-blue headband, light freckles, a dazzling confident grin, a white shirt with rolled sleeves and a fitted brown vest, holding a sparkly silver fishing rod` |
| 유리 | `a cute feisty young woman with a short ash-silver bob, a faded sea-blue headband, a competitive pout, an oversized black captain coat with shiny buttons` |
| 무능 | 기존 `muneung.jpg` 참조. 없으면 `a small round fluffy yellow chick mascot with big sparkly eyes and a tiny sailor hat` |
| 카론 | `a shy little ghost in a hooded cloak, glowing softly, holding a tiny oar, round dot eyes` |
| 연 | `a bubbly little ghost girl with a glowing paper lantern, translucent and sparkly, big happy eyes` |
| 해왕류의 왕 | `a huge friendly sea serpent with a round snout, a tiny crown, warm lava-orange scales and big gentle eyes` |
| 플레이어 | 얼굴을 그리지 않는다. `a fisherman seen from behind in a raincoat` (모두가 자기라고 느끼게) |

---

## 인물 카드 · 아이템

| 파일 | 크기 | 프롬프트 (`[장면]` 뒤에) |
|---|---|---|
| `npc_bear.jpg` | 832×1216 | `Character portrait of a charming burly old fisherman grandpa with a big fluffy white beard, rosy cheeks, twinkling kind eyes, a faded navy knit beanie, a patched yellow raincoat vest, pretending to be grumpy with arms crossed but secretly smiling, behind the counter of a cozy cluttered tackle shop with hanging fishing floats.` |
| `npc_haesol.jpg` | 832×1216 | `Character portrait of a beautiful lively young woman with long dark hair in a loose side braid, a sea-blue headband, light freckles, a dazzling confident grin, a white shirt with rolled sleeves and a fitted brown vest, holding a sparkly silver fishing rod, giving a peace sign on the bow of a small wooden ship, sunrise behind her.` |
| `npc_yuri.jpg` | 832×1216 | `Character portrait of a cute feisty young woman with a short ash-silver bob, a faded sea-blue headband, a competitive pout, an oversized black captain coat with shiny buttons, pointing at the viewer with a competitive pout, cute black-sailed boat behind her.` |
| `npc_charon_yeon.jpg` | 832×1216 | `Two cute little ghosts floating together over a moonlit sea, a shy hooded ghost holding a tiny oar and a bubbly ghost girl holding a glowing paper lantern, translucent and sparkly, waving happily.` |
| `npc_seaking.jpg` | 832×1216 | `A huge friendly sea serpent with a round snout, a tiny crown, warm lava-orange scales and big gentle eyes, resting its chin on the water and smiling, little fish swimming around it.` |
| `letter_bottle.jpg` | 1024×1024 | `A cute glass bottle with a rolled letter inside tied with a sea-blue ribbon, bobbing on sparkling waves, a tiny smiley doodle visible on the letter, sunny.` |
| `item_silver_rod.jpg` | 1024×1024 | `A sparkly silver fishing rod floating above calm glowing water, wave-pattern engravings, a sea-blue ribbon on the handle, tiny stars and bubbles around it, magical and cute.` |

> 예전 `log_page.jpg`(젖은 일지 조각)는 `letter_bottle.jpg`(병 속 편지)로 바뀌었다.

---

## 프롤로그

| 파일 | 프롬프트 (`[장면]` 뒤에) |
|---|---|
| `story_0_1.jpg` | `Inside a cozy little tackle shop with a bell over the door, colorful floats and nets hanging, a charming burly grandpa fisherman with a fluffy white beard and navy beanie behind the counter pretending to frown, a small round yellow chick mascot staring at his beard, a little fisherman in a raincoat seen from behind in the doorway.` |
| `story_0_2.jpg` | `A little fisherman seen from behind on a wooden pier holding up a cute fish that is proudly holding a small glass bottle with a letter in its mouth, sparkles around the bottle, sunny harbor, delighted mood.` |

## 1장 — 이스트 블루

| 파일 | 프롬프트 (`[장면]` 뒤에) |
|---|---|
| `story_1_1.jpg` | `A rainbow-shimmering cute fish leaping out of a turquoise bay with a happy face, splashing droplets, a chubby grandpa fisherman with a fluffy white beard watching from the pier with a surprised O-shaped mouth, little islands in the background.` |
| `story_1_2.jpg` | `A cute small boat being fixed up on the beach, fresh wooden planks and a hammer, the fluffy-bearded grandpa nodding approvingly with arms crossed, a small yellow chick mascot in a hard hat holding a tiny nail, sunny.` |
| `story_1_3.jpg` | `A handsome cheerful young sailor dragging a big suitcase onto a small boat and waving hello, seagulls overhead, morning sea, warm welcoming mood.` |
| `story_1_4.jpg` | `View from a small boat where pale turquoise water meets a deep blue sea in a soft line, a cute black-sailed boat tiny in the distance, the fluffy-bearded grandpa on the boat pointing ahead with a nostalgic smile, gentle afternoon breeze.` |

## 2장 — 그랜드 라인

| 파일 | 프롬프트 (`[장면]` 뒤에) |
|---|---|
| `story_2_1.jpg` | `A cute black-sailed boat zooming alongside a small fishing boat, on its deck a cute feisty young woman with a short ash-silver bob, sea-blue headband and oversized black captain coat pointing and shouting with puffed cheeks, a small yellow chick mascot peeking from behind a barrel, splashy waves.` |
| `story_2_2.jpg` | `A big golden fish with a cheeky grin leaping from glittering golden water, a silly doodle drawn on one of its scales, a little fisherman seen from behind holding a bent rod, sunset sparkles.` |
| `story_2_3.jpg` | `A glowing sparkly ghost ship floating over a calm night sea like a lantern boat, a cute ghost girl with a paper lantern waving from the deck, little star sparkles trailing behind, a small fishing boat waving back, magical and friendly.` |
| `story_2_4.jpg` | `Two cute boats sailing side by side into a warm steamy sea like a hot spring, little volcano islands puffing heart-shaped smoke, a feisty silver-bob young woman in a big black coat looking back with a reluctant smile.` |

## 3장 — 신세계

| 파일 | 프롬프트 (`[장면]` 뒤에) |
|---|---|
| `story_3_1.jpg` | `A cute upgraded little ship sparkling in the harbor at sunrise with shiny new parts, the fluffy-bearded grandpa on the pier wiping a happy tear with his beard.` |
| `story_3_2.jpg` | `A handsome whistling shipwright with a big straw hat and a tool belt patting the side of a cute boat, an old blueprint sketch of a silver fishing rod sticking out of his pocket, cozy cove.` |
| `story_3_3.jpg` | `A little fisherman seen from behind stepping out of a glowing sparkly ghost ship into moonlight, a bubbly ghost girl with a paper lantern happily floating after them and sniffing curiously, cute and magical.` |
| `story_3_4.jpg` | `A dreamy sea split into seven soft pastel colors like a rainbow flower, tons of cute baby fish swimming underneath, a shy hooded little ghost on the bow pointing down, a huge pair of big round curious eyes blinking deep below.` |

## 4장 — 올 블루

| 파일 | 프롬프트 (`[장면]` 뒤에) |
|---|---|
| `story_4_1.jpg` | `A huge friendly sea serpent rising from the rainbow sea, tilting its head curiously at a small boat with a question-mark expression, a feisty silver-bob young woman on the boat holding up a letter, misty sparkly light.` |
| `story_4_2.jpg` | `A huge sea serpent giggling and dropping a single big shiny scale onto a small boat, a heart-shaped map drawn on the inside of the scale, bubbles and sparkles, playful mood.` |
| `story_4_3.jpg` | `A mythical starry cosmic fish rising from a mirror-calm night sea, the whole sea twinkling, a small yellow chick mascot on the railing with its beak wide open in awe.` |
| `story_4_4.jpg` | `In the middle of a rainbow sea, beside a giant softly glowing heart surrounded by cute baby fish, a beautiful lively young woman with a long dark braid, sea-blue headband and freckles waving excitedly and holding out a sparkly silver fishing rod to a little fisherman seen from behind, a bubbly ghost girl with a lantern flying into her arms for a hug and a shy hooded ghost waving a tiny oar, confetti of light.` |
| `story_epilogue.jpg` | `The same cozy tackle shop in bright morning light, the charming fluffy-bearded grandpa laughing heartily at a sparkly silver fishing rod leaning on the counter, a little fisherman seen from behind in the doorway, seagulls outside, happy ending.` |

---

## 뽑는 순서 팁

1. 인물 카드 먼저(`npc_bear`, `npc_haesol`, `npc_yuri`, `npc_charon_yeon`, `npc_seaking`) — 마음에 드는 시드를 아래에 적기.
2. 장면을 뽑을 때 그 인물 카드를 참조로 건다.
3. 장면 속 인물이 작으면 얼굴이 뭉개지기 쉽다 → FaceDetailer 한 번.

| 파일 | 시드 | 메모 |
|---|---|---|
| npc_bear.jpg | | |
| npc_haesol.jpg | | |
| npc_yuri.jpg | | |
