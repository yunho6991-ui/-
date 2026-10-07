# 시즌 2 — NPC 배 · 선장 그림 프롬프트 (ComfyUI)

> `docs/season2-ships.md`의 NPC 배 12종용입니다. 크기, 스타일 고정 문구, 네거티브는 `docs/fishing-story-prompts.md`와 같습니다.
> 각 프롬프트 앞 `[스타일]` 자리에 그 파일의 스타일 문구를 붙이세요.
> 지금 배 그림(`ship_<종류>_<등급>.jpg`)과 화풍을 맞추려면 그중 한 장을 스타일 참조로 거세요.

| 종류 | 크기 | 파일 이름 |
|---|---|---|
| NPC 배 (만났을 때 보내는 그림) | 1216 × 832 | `npc_ship_<id>.jpg` |
| NPC 선장 (선택, 대화 카드용) | 832 × 1216 | `npc_cap_<id>.jpg` |
| 항구 (시세표 · 화물 판매용) | 1216 × 832 | `port_<해역>.jpg` |

---

## NPC 배 (1216×832)

### `npc_ship_pirate.jpg` — 검은이빨 해적단
```
[스타일] A menacing pirate galleon with tattered black sails painted with a giant jagged-tooth skull emblem, a golden tooth glinting on the figurehead, cannons out and smoking, cutting through rough grey-blue waves toward the viewer, pirate crew silhouettes cheering on deck, stormy dramatic sky.
```

### `npc_ship_navy.jpg` — 해군 순찰선
```
[스타일] A clean white and navy-blue naval patrol ship with crisp sails bearing an anchor-and-wave emblem, signal flags fluttering, uniformed sailors standing in formation on deck, a spyglass glinting from the bridge, calm sea under a bright clear sky, orderly and authoritative mood.
```

### `npc_ship_peddler.jpg` — 바다 행상 할멈
```
[스타일] A tiny cozy wooden peddler boat overloaded with colorful bundles, hanging lanterns, jars of bait, rolled nets and trinkets, a patched striped awning, a cheerful old grandmother with a headscarf waving from the stern, gentle turquoise sea, warm afternoon light, charming and humorous.
```

### `npc_ship_distress.jpg` — 조난선
```
[스타일] A small battered motorboat drifting with its engine smoking, an orange distress flag waving, a flustered round-faced young captain waving both arms frantically, a fluffy cat sitting calmly on top of the engine covered in cat hair, choppy water, comedic yet urgent mood.
```

### `npc_ship_smuggler.jpg` — 밀수선
```
[스타일] A sleek dark low-profile sailing boat emerging from night fog with no lights except a single shuttered lantern, crates covered with tarps on deck, a hooded figure leaning on the rail with a finger to their lips, moonlight on black water, secretive and tense mood.
```

### `npc_ship_lab.jpg` — 심해 연구선
```
[스타일] A quirky research vessel with a big glass observation dome, cranes lowering a round brass diving bell into the water, specimen tanks with glowing fish on deck, a scientist in a lab coat with octopus-shaped goggles pointing excitedly at the sea, bright deep blue water, curious and playful mood.
```

### `npc_ship_supply.jpg` — 야간 보급선
```
[스타일] A small floating night market boat lit by warm paper lanterns, steaming food stalls, buckets of bait and stacked nets for sale, a sleepy friendly man with an owl-feather hat at the counter, starry night sky over a calm dark sea, cozy late-night atmosphere.
```

### `npc_ship_contest.jpg` — 낚시대회 주최선
```
[스타일] A festive event boat decorated with bunting flags, balloons and a giant fish-shaped trophy on a pedestal, a flamboyant host holding a microphone on a small stage, several small fishing boats gathered around with anglers casting, confetti in the air, bright sunny celebratory mood.
```

### `npc_ship_explorer.jpg` — 탐험가의 배
```
[스타일] A rugged expedition sloop with patched sails covered in hand-drawn maps, a telescope and compass on the bow, an adventurous explorer with a wide-brimmed hat holding up a torn treasure map fragment, a distant mysterious island with a single palm tree on the horizon, golden adventurous light.
```

### `npc_ship_palace.jpg` — 용궁 사신선
```
[스타일] An elegant traditional East Asian dragon-palace envoy boat with curved golden roofs and coral pillars, carried on the back of a giant ancient sea turtle, a slow wise turtle messenger in court robes holding a scroll, seven-colored glowing sea around them, majestic and serene.
```

### `npc_ship_bear.jpg` — 바다곰 영감의 고깃배
```
[스타일] A small old wooden fishing boat with faded paint and a patched sail, an elderly Korean fisherman around seventy with a broad bear-like build, thick white beard, deeply tanned weathered skin, faded navy knit cap and patched oilskin vest raising a hand in greeting while holding out a small bait tin, calm turquoise bay, warm morning light.
```

### `npc_ship_yuri.jpg` — 유리의 쾌속선
```
[스타일] A sleek black-and-silver racing speedboat cutting across the water with a big spray wake, a sharp-eyed young Korean woman around twenty with a short ash-silver bob, a faded sea-blue headband and an oversized black captain's coat standing at the wheel pointing a fishing rod at the viewer with a challenging grin, dynamic speed lines, bright competitive energy.
```

---

## NPC 선장 카드 (선택, 832×1216)

> 바다곰 영감·유리는 `fishing-story-prompts.md`의 `npc_bear.jpg` · `npc_yuri.jpg`를 같이 쓰면 된다.

| 파일 | 프롬프트 |
|---|---|
| `npc_cap_pirate.jpg` | `[스타일] Portrait of a burly pirate captain called Black Tooth, scarred face, wild black beard with beads, one shining gold front tooth in a wide grin, tricorn hat with a bone ornament, heavy dark coat, cutlass on his shoulder, standing on a stormy deck.` |
| `npc_cap_navy.jpg` | `[스타일] Portrait of a stern but fair young Korean naval patrol captain, neat short hair, crisp white and navy uniform with an anchor badge, holding a spyglass under one arm, calm sea and patrol ship flags behind.` |
| `npc_cap_peddler.jpg` | `[스타일] Portrait of a cheerful tiny old Korean grandmother peddler with a colorful headscarf, rosy cheeks and a gap-toothed smile, a huge cloth bundle on her back overflowing with goods, holding up a trinket persuasively.` |
| `npc_cap_distress.jpg` | `[스타일] Portrait of a flustered chubby young captain with messy hair and a too-big captain's hat, sweating and waving his arms, a calm fluffy cat perched on his head, smoke behind him.` |
| `npc_cap_smuggler.jpg` | `[스타일] Portrait of a mysterious hooded smuggler, face mostly hidden in shadow with only a sly smile visible, long dark coat lined with hidden pockets, holding a small glowing wrapped package, foggy night background.` |
| `npc_cap_lab.jpg` | `[스타일] Portrait of an excitable marine scientist with curly hair, octopus-shaped goggles pushed up on the forehead, lab coat covered in ink stains, holding a clipboard and a glowing specimen jar.` |
| `npc_cap_supply.jpg` | `[스타일] Portrait of a sleepy kind middle-aged man with an owl-feather hat and round glasses, holding a steaming cup and a lantern, night market boat background with warm lanterns.` |
| `npc_cap_contest.jpg` | `[스타일] Portrait of a flamboyant event host with a saury-fish themed sparkly suit and a bow tie, holding a microphone and pointing with dramatic flair, confetti and stage lights.` |
| `npc_cap_explorer.jpg` | `[스타일] Portrait of a young adventurous explorer with a wide-brimmed hat, sun-tanned skin, scarf and satchel full of rolled maps, holding a torn treasure map fragment and grinning.` |
| `npc_cap_palace.jpg` | `[스타일] Portrait of a very old wise sea turtle messenger standing upright in traditional East Asian court robes and a tall official hat, holding a scroll with slow dignified posture, coral palace background.` |

---

## 항구 (1216×832)

> 시즌 2 항구 시세 · 화물 판매 때 보내는 그림. 해역 이름을 바꾸면 파일 이름만 맞추면 된다.

| 파일 | 프롬프트 |
|---|---|
| `port_east.jpg` | `[스타일] A peaceful small harbor town on a turquoise bay with colorful wooden houses, a fish market with striped awnings, a chalkboard price board with fish icons and no readable text, fishing boats moored, seagulls, bright morning.` |
| `port_grand.jpg` | `[스타일] A bustling rough pirate-era trading port with stone docks, many ships with varied sails, merchants haggling, crates and barrels stacked high, a large market board with fish icons and no readable text, lively afternoon.` |
| `port_newworld.jpg` | `[스타일] A fortified harbor built into volcanic rock with glowing lava channels, heavy iron gates, armored merchant ships docking, a black-market fish auction under red lanterns, dangerous and rich atmosphere, crimson sky.` |
| `port_allblue.jpg` | `[스타일] A shimmering mythical harbor floating on the seven-colored sea, coral and pearl buildings, dragon-palace style rooftops, exotic fish displayed in glowing water tanks, envoy turtles and grand ships, dreamlike luminous light.` |
