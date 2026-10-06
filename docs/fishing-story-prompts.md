# 개인톡 낚시 — 스토리 그림 프롬프트 (ComfyUI)

> `docs/fishing-story.md`의 장면마다 그림 한 장씩 뽑을 프롬프트입니다.
> 코드 주석에 지금 그림은 **Krea2**로 뽑는다고 되어 있어서, Flux 계열에 맞게 **자연어 영어 문장**으로 썼습니다.
> SDXL·Pony 같은 태그형 모델을 쓴다면 문장을 쉼표 태그로 바꿔야 합니다.
> 파일 이름은 기존 규칙(`FISH_ART_DIR/<이름>.jpg`)에 맞췄습니다.

## 공통 설정

| 항목 | 값 |
|---|---|
| 장면(가로) | 1216 × 832 |
| 인물 카드(세로) | 832 × 1216 |
| 아이템(정사각) | 1024 × 1024 |
| 저장 | JPG, 카톡 전송용이라 긴 변 1200px 안팎이면 충분 |
| 네거티브 | Flux 계열은 보통 안 씀(CFG 1). 쓰는 워크플로라면 맨 아래 공통 네거티브 사용 |

### 스타일 고정 문구 (모든 프롬프트 앞에 붙이기)

```
Painterly fantasy adventure illustration with soft cel shading, warm cinematic lighting, rich ocean colors, slightly whimsical storybook mood, clean readable composition, highly detailed, no text, no letters, no watermark.
```

> 지금 선원 카드나 전설 물고기 그림과 화풍을 맞추고 싶다면, 그 그림을 뽑을 때 쓴 스타일 문구로 위 줄을 바꾸세요.
> 화풍이 들쭉날쭉하면 기존 카드 한 장을 IPAdapter/Redux 스타일 참조로 걸면 잘 맞습니다.

### 인물 고정 묘사 (얼굴이 매번 달라지지 않게)

장면에 그 인물이 나오면 아래 문장을 **그대로** 넣으세요. 먼저 인물 카드(`npc_*.jpg`)를 뽑고, 마음에 드는 시드를 기록해 두면 장면에서도 일관되게 나옵니다.

| 인물 | 고정 문구 |
|---|---|
| 바다곰 영감 | `an elderly Korean fisherman around seventy with a broad bear-like build, thick white beard, deeply tanned weathered skin, small kind eyes under bushy brows, faded navy knit cap, patched oilskin vest over a grey wool sweater` |
| 해솔 | `a confident young Korean woman around twenty-five with long dark hair in a loose side braid, a sea-blue headband, light freckles, a bold grin, white linen shirt with rolled sleeves, brown leather vest, holding a slender silver fishing rod that glows faintly` |
| 유리 | `a sharp-eyed young Korean woman around twenty with a short ash-silver bob, a faded sea-blue headband, an oversized black captain's coat with brass buttons, fingerless gloves` |
| 무능 | 기존 `muneung.jpg`를 참조 이미지로 쓰기 권장. 없으면: `a small round fluffy yellow chick mascot with big sparkly eyes and a tiny sailor hat` |
| 카론 · 연 | 기존 `ghost_l.jpg` · `ghost_l2.jpg`를 참조 이미지로 쓰기 권장 |
| 플레이어 | 얼굴을 그리지 않는다(누구나 자기라고 느끼게). `a fisherman seen from behind` 또는 손·실루엣만 |

---

## 인물 카드 · 아이템

### `npc_bear.jpg` — 바다곰 영감 (832×1216)
```
[스타일] Character portrait of an elderly Korean fisherman around seventy with a broad bear-like build, thick white beard, deeply tanned weathered skin, small kind eyes under bushy brows, faded navy knit cap, patched oilskin vest over a grey wool sweater. He stands behind the wooden counter of a cluttered old harbor tackle shop, arms crossed, gruff but warm expression, fishing rods and nets hanging on the walls, a pipe in the corner of his mouth, warm lamplight, upper body shot.
```

### `npc_haesol.jpg` — 해솔 (832×1216)
```
[스타일] Character portrait of a confident young Korean woman around twenty-five with long dark hair in a loose side braid, a sea-blue headband, light freckles, a bold grin, white linen shirt with rolled sleeves, brown leather vest, holding a slender silver fishing rod that glows faintly. She stands on the bow of a wooden sailing ship, one foot on the railing, wind in her hair, sunrise over the ocean behind her, adventurous legendary aura, three-quarter body shot.
```

### `npc_yuri.jpg` — 유리 (832×1216)
```
[스타일] Character portrait of a sharp-eyed young Korean woman around twenty with a short ash-silver bob, a faded sea-blue headband, an oversized black captain's coat with brass buttons, fingerless gloves. She points a finger accusingly at the viewer with a competitive smirk, black sails and stormy sky behind her, rival character energy, three-quarter body shot.
```

### `log_page.jpg` — 항해일지 조각 (1024×1024)
```
[스타일] A torn, water-stained page from an old ship's logbook lying on wet wooden planks, faded ink handwriting that is illegible, a small drawn map sketch in the corner, a dried strand of seaweed, a single fish scale glinting on it, soft morning light, close-up still life.
```

### `item_silver_rod.jpg` — 은빛 낚싯대 (1024×1024)
```
[스타일] A legendary slender silver fishing rod floating upright above calm glowing water, intricate wave engravings along the handle, a sea-blue ribbon tied near the reel, soft light particles rising around it, seven-colored shimmer in the water below, dark background, item showcase illustration.
```

---

## 프롤로그

### `story_0_1.jpg` — 낚시점 영감 (1216×832)
```
[스타일] Interior of a small cluttered old harbor tackle shop at dusk, the door creaking open with light spilling in. Behind the counter stands an elderly Korean fisherman around seventy with a broad bear-like build, thick white beard, deeply tanned weathered skin, small kind eyes under bushy brows, faded navy knit cap, patched oilskin vest over a grey wool sweater, looking up with a gruff half-smile. Buckets of bait, hanging nets, glass floats, a fisherman's silhouette in the doorway seen from behind.
```

### `story_0_2.jpg` — 젖은 종이 (1216×832)
```
[스타일] Close-up of weathered hands holding a freshly caught silver fish on a small wooden dock, a soaked torn piece of old paper hanging from the fish's mouth with faded blurry handwriting, calm sea and fishing village in the soft-focus background, golden hour, sense of discovery.
```

---

## 1장 — 이스트 블루

### `story_1_1.jpg` — 반짝이는 비늘 (1216×832)
```
[스타일] A small fishing boat on a calm turquoise bay, a fisherman seen from behind lifting a shimmering rare fish with iridescent blue scales that sparkle in the sunlight, droplets flying, on the nearby dock an elderly fisherman with a thick white beard and navy knit cap watches with raised eyebrows, peaceful tropical islands in the distance, bright cheerful daylight.
```

### `story_1_2.jpg` — 망치 소리 (1216×832)
```
[스타일] A small wooden fishing boat in a harbor dry dock being upgraded, fresh pale wood planks, a new brass engine part, tools and wood shavings scattered around, an elderly fisherman around seventy with a broad bear-like build, thick white beard, faded navy knit cap and patched oilskin vest standing with arms crossed approvingly, a small round yellow chick mascot with a tiny sailor hat sitting on a toolbox looking confused, warm afternoon light.
```

### `story_1_3.jpg` — 첫 선원 (1216×832)
```
[스타일] The deck of a small fishing boat at the pier in the morning, a cheerful newcomer sailor dropping a heavy canvas duffel bag onto the deck with a friendly wave, the boat owner seen from behind, seagulls overhead, coiled ropes and crates, cozy found-family vibe, soft morning mist.
```

### `story_1_4.jpg` — 수평선 너머 (1216×832)
```
[스타일] Wide view from the stern of a small boat where calm pale turquoise water abruptly turns deep dark blue at a sharp line on the horizon, distant storm clouds and a tiny black sail far away, on the boat an elderly fisherman with a thick white beard and navy knit cap gazes toward the horizon with a melancholic expression, wind picking up, dramatic late afternoon light.
```

---

## 2장 — 그랜드 라인

### `story_2_1.jpg` — 낯선 돛 (1216×832)
```
[스타일] A sleek pirate-style ship with black sails pulling alongside a small fishing boat on choppy deep blue sea. On its railing stands a sharp-eyed young Korean woman around twenty with a short ash-silver bob, a faded sea-blue headband, an oversized black captain's coat with brass buttons, fingerless gloves, pointing and shouting with a competitive smirk. A small round yellow chick mascot with a tiny sailor hat hides behind a barrel on the fishing boat, dynamic composition, spray of waves.
```

### `story_2_2.jpg` — 황금빛 (1216×832)
```
[스타일] A legendary giant golden fish bursting out of the sea in a spray of glowing water, its scales radiating golden light, faint ancient engraved lines visible on one large scale, the small fishing boat below dwarfed by it, the fisherman seen from behind bracing the bent rod, sunset sky turning gold, epic awe-inspiring moment.
```
> 스타일 문구에 `no text`가 있어서 비늘의 "더 깊이" 글씨는 그려지지 않는다. 글씨를 넣고 싶으면 뽑은 뒤 편집으로 넣는 게 깔끔하다.

### `story_2_3.jpg` — 안개 속의 배 (1216×832)
```
[스타일] Thick night fog over a still dark sea, a ghostly tattered old sailing ship drifting silently past, its hull faintly translucent, only a single warm lantern glowing on its deck held by a pale spectral figure raising one hand in greeting, the small fishing boat in the foreground with a lantern of its own, eerie but sad and beautiful atmosphere, cool blue and teal tones with one warm light.
```

### `story_2_4.jpg` — 괴물들의 바다로 (1216×832)
```
[스타일] Two boats sailing side by side into a boiling volcanic sea, a black-sailed ship and a small fishing boat, crimson sky with ash clouds, volcanic islands erupting in the distance, steam rising from the water, on the black-sailed ship a young woman with a short ash-silver bob, faded sea-blue headband and oversized black captain's coat looks over her shoulder with a reluctant smile, sense of a new alliance, dramatic red and orange lighting.
```

---

## 3장 — 신세계

### `story_3_1.jpg` — 완성된 배 (1216×832)
```
[스타일] A fully upgraded sturdy fishing ship gleaming in a harbor at sunrise, polished brass cannons, reinforced hull plates, a powerful engine with a smoking stack, a sonar dish on the mast, an elderly fisherman around seventy with a broad bear-like build, thick white beard, navy knit cap and patched oilskin vest stands on the dock looking up at it with proud teary eyes, heroic composition, warm golden light.
```

### `story_3_2.jpg` — 떠돌이 조선공 (1216×832)
```
[스타일] A mysterious wandering shipwright with a long grey coat, a wide-brimmed hat hiding most of the face, and a leather tool belt, gently placing a hand on the hull of a ship moored at a lonely rocky cove, old blueprints tucked under one arm, one blueprint corner shows a sketch of a slender silver fishing rod, overcast moody light, sense of a secret.
```

### `story_3_3.jpg` — 심연에서 돌아온 자 (1216×832)
```
[스타일] The fisherman seen from behind climbing up the last steps out of the dark lowest deck of a ghost ship into pale moonlight, a gentle spectral lantern-bearer ghost following close behind, holding a softly glowing lantern, looking at the fisherman with hopeful recognition, rotting timbers, floating dust, wisps of mist, bittersweet haunting atmosphere, cold blue light with warm lantern glow.
```
> 유령은 기존 `ghost_l2.jpg`(등불지기 연)를 참조 이미지로 걸면 같은 인물로 나온다.

### `story_3_4.jpg` — 모든 바다가 모이는 곳 (1216×832)
```
[스타일] A breathtaking sea where the water splits into seven distinct glowing colors radiating outward like a giant flower, countless never-before-seen fantastical fish swimming visibly beneath the clear surface, a small upgraded ship entering from the edge, a tall silent ghostly ferryman standing at its bow, far below in the depths an enormous dark eye slowly opening, wonder mixed with dread, dreamy luminous lighting.
```

---

## 4장 — 올 블루

### `story_4_1.jpg` — 파수꾼 (1216×832)
```
[스타일] A colossal sea serpent dragon rising from the seven-colored sea, its body coiled high above a small ship, scales like ancient stone and coral, not attacking but calmly staring down with wise glowing eyes as if judging, on the ship a young woman with a short ash-silver bob and oversized black captain's coat holds up an old torn notebook page toward it, epic scale, misty divine light.
```

### `story_4_2.jpg` — 시험을 통과하다 (1216×832)
```
[스타일] A giant sea serpent dragon slowly sinking back into the glowing sea, leaving behind a single huge iridescent scale floating on the water, the inside of the scale faintly etched with lines like a map, the fisherman seen from behind reaching down from the boat to pick it up, calm after the battle, soft dawn light and sparkling water.
```

### `story_4_3.jpg` — 바다의 이름 (1216×832)
```
[스타일] A mythical cosmic fish rising from the sea at night, its body like a starry galaxy with nebula fins, the entire sea gone perfectly still and mirror-like reflecting the stars, a small round yellow chick mascot with a tiny sailor hat on the boat railing staring with its beak wide open in shock, sense of the sacred, deep indigo and violet with starlight.
```

### `story_4_4.jpg` — 심장지기 (결말) (1216×832)
```
[스타일] At the center of a luminous seven-colored whirlpool stands a confident young Korean woman around twenty-five with long dark hair in a loose side braid, a sea-blue headband, light freckles, a gentle grin, white linen shirt with rolled sleeves, brown leather vest, holding out a slender silver fishing rod that glows brightly toward the fisherman seen from behind. Behind her a tall silent ghostly ferryman and a lantern-bearing spirit are rushing toward her with joy, their forms becoming less transparent, glowing light particles everywhere, emotional reunion, heavenly radiant lighting.
```

### `story_epilogue.jpg` — 다시 항구 (1216×832)
```
[스타일] The same cluttered old harbor tackle shop as the beginning, now in bright morning light, an elderly Korean fisherman around seventy with a broad bear-like build, thick white beard, deeply tanned skin, faded navy knit cap and patched oilskin vest laughing warmly with tears in his eyes, looking at a glowing silver fishing rod leaning against the counter, the fisherman seen from behind in the doorway, seagulls outside, peaceful happy ending.
```

---

## 공통 네거티브 (쓰는 워크플로일 때만)

```
text, letters, watermark, signature, logo, blurry, lowres, deformed hands, extra fingers, extra limbs, distorted face, cropped head, jpeg artifacts, oversaturated
```

## 뽑는 순서 팁

1. **인물 카드 3장 먼저** (`npc_bear`, `npc_haesol`, `npc_yuri`). 마음에 드는 시드를 아래 표에 적어 두기.
2. 장면을 뽑을 때 그 인물 카드를 참조 이미지(IPAdapter / Redux / PuLID 등 쓰는 것)로 걸면 얼굴이 맞는다.
3. 장면 그림 안의 인물이 작으면 얼굴이 뭉개지기 쉽다. FaceDetailer를 한 번 거치면 좋다.

| 파일 | 시드 | 메모 |
|---|---|---|
| npc_bear.jpg | | |
| npc_haesol.jpg | | |
| npc_yuri.jpg | | |
