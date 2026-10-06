# 귀여운 화풍 — 물고기 · 선원 전체 프롬프트 (ComfyUI)

> 전체 그림을 **귀엽고 발랄한 화풍**으로 다시 뽑기 위한 목록이다. 코드(`fishing.py`)의 물고기 84종, 선원 99명(일반 36 + 유령 2 + 무능 + 신화 60)을 **전부** 넣었다.
> **잘 나온 그림은 "다시 뽑기" 칸을 비워 두고**, 다시 뽑을 것만 `[x]`로 체크해서 쓴다.
> 파일 이름은 지금 코드가 찾는 이름(`FISH_ART_DIR/<id>.jpg`) 그대로다.

## 공통 스타일 (모든 그림 앞에 붙이기)

```
Cute kawaii storybook illustration, soft pastel colors, rounded chubby shapes, big sparkly eyes, gentle cel shading, soft clean outlines, cheerful warm lighting, simple uncluttered composition, no text, no letters, no watermark.
```

> 이 문구가 **모든 프롬프트 파일의 새 기준**이다(`fishing-story-prompts.md`의 예전 스타일 문구 대신). 아래 `[귀여움]` 자리에 넣는다.
> 화풍을 맞추려면: 처음 몇 장을 뽑아 마음에 드는 걸 하나 고르고, 그걸 **스타일 참조(IPAdapter / Redux)**로 걸어 나머지를 뽑으면 통일된다.

## 공통 네거티브 (쓰는 워크플로일 때만)

```
scary, creepy, horror, gore, realistic, photorealistic, sharp teeth, menacing, dark gloomy, text, watermark, extra limbs, deformed
```

---

## 🐟 물고기 (1024×1024)

**프롬프트 = `[귀여움]` + 물고기 앞부분 + 칸의 묘사**

물고기 앞부분:
```
A cute chibi fish mascot character, round chubby body, big sparkly eyes, tiny blush cheeks, floating in clear water with little bubbles, centered, simple soft pastel background,
```
> 쓰레기·보물상자·초대장처럼 물고기가 아닌 것도 같은 앞부분을 써도 된다(사물이 귀여운 캐릭터로 나옴).
> 신화·재앙급은 끝에 `, giant and majestic but adorable, soft glow` 를 덧붙이면 덩치감이 산다.


### 🗑️ 쓰레기

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `boot.jpg` | 🥾 낡은 장화 | `an old rubber boot with a sleepy face, a tiny crab peeking out of it` |
| [ ] | `can.jpg` | 🥫 찌그러진 깡통 | `a dented tin can with a sheepish smile and a little seaweed bow` |
| [ ] | `sock.jpg` | 🧦 누군가의 양말 | `a single striped sock wriggling like a fish, embarrassed blush` |
| [ ] | `phone.jpg` | 📱 물에 빠진 폰 | `a waterlogged smartphone blowing bubbles from its speaker, dizzy swirl eyes` |
| [ ] | `bucket.jpg` | 🪣 구멍 난 양동이 | `a leaky bucket with a hole, water spouting out like a little fountain, surprised face` |
| [ ] | `seaweed.jpg` | 🌿 해초 뭉치 | `a fluffy tangle of green seaweed with tiny eyes peeking out, shy` |
| [ ] | `slipper.jpg` | 🩴 떠내려온 슬리퍼 | `a floating flip-flop sandal with a happy face drifting on waves` |
| [ ] | `rusty_key.jpg` | 🗝️ 녹슨 열쇠 | `a rusty old key with a wise little face and a tiny barnacle hat` |
| [ ] | `soju_bottle.jpg` | 🍶 빈 소주병 | `an empty green glass bottle with rosy cheeks, hiccuping bubbles` |
| [ ] | `lost_ticket.jpg` | 🎫 꽝 난 복권 | `a crumpled lottery ticket with a pouting face and a teardrop` |
| [ ] | `umbrella.jpg` | ☂️ 고장 난 우산 | `a broken inside-out umbrella with a goofy grin, flapping like a jellyfish` |

### 흔함

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `minnow.jpg` | 🐟 피라미 | `a tiny slim silver minnow, energetic and zippy` |
| [ ] | `crucian_carp.jpg` | 🐟 붕어 | `a round golden-brown crucian carp, friendly and plump` |
| [ ] | `goby.jpg` | 🐟 망둥어 | `a little goby with big bulging eyes and a cheeky grin, sitting on a pebble` |
| [ ] | `horse_mackerel.jpg` | 🐟 전갱이 | `a sleek silver-blue horse mackerel with a confident smile` |
| [ ] | `smelt.jpg` | 🐟 빙어 | `a tiny translucent smelt fish, shivering cutely with snowflakes around` |
| [ ] | `anchovy.jpg` | 🐟 멸치 | `a tiny anchovy leading a little parade of even tinier anchovies` |
| [ ] | `killifish.jpg` | 🐟 송사리 | `a teeny killifish with sparkly eyes, the smallest and proudest` |
| [ ] | `saury.jpg` | 🐟 꽁치 | `a long slim saury fish with a pointy nose, stretching proudly` |
| [ ] | `greenling.jpg` | 🐟 노래미 | `a speckled greenling fish with a cozy scarf, relaxed smile` |
| [ ] | `bubble_killifish.jpg` | 🫧 거품 송사리 | `a tiny killifish blowing a giant shiny bubble bigger than itself` |
| [ ] | `sleepy_puffer.jpg` | 🐡 졸린 복어 | `a puffer fish half-asleep with a nightcap and a drool bubble` |
| [ ] | `clover_carp.jpg` | 🍀 네잎 붕어 | `a lucky carp with four-leaf-clover patterns on its scales, cheerful` |

### 보통

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `carp.jpg` | 🐟 잉어 | `a chubby orange-and-white koi carp with flowing fins, gentle smile` |
| [ ] | `rockfish.jpg` | 🐟 우럭 | `a grumpy-cute dark rockfish with spiky fins and puffed cheeks` |
| [ ] | `mackerel.jpg` | 🐟 고등어 | `a striped blue mackerel with a sporty headband, energetic` |
| [ ] | `flatfish.jpg` | 🐟 광어 | `a flat flounder-like fish with both eyes on one side, giggling` |
| [ ] | `pufferfish.jpg` | 🐡 복어 | `a puffed-up round pufferfish like a spiky balloon, angry-cute face` |
| [ ] | `flounder.jpg` | 🐟 가자미 | `a flat flounder half-buried in sand, peeking with a smirk` |
| [ ] | `spanish_mackerel.jpg` | 🐟 삼치 | `a long shiny spanish mackerel striking a heroic pose` |
| [ ] | `catfish.jpg` | 🐟 메기 | `a chubby catfish with long whiskers like a mustache, wise grandpa vibe` |
| [ ] | `webfoot_octopus.jpg` | 🐙 쭈꾸미 | `a small webfoot octopus with tiny round tentacles, waving hello` |
| [ ] | `cuttlefish.jpg` | 🦑 갑오징어 | `a cuttlefish with rainbow color-changing skin, blushing in waves of color` |
| [ ] | `blue_crab.jpg` | 🦀 꽃게 | `a blue crab with big claws held up in a cheerful V-sign` |
| [ ] | `rainbow_trout.jpg` | 🌈 무지개 송어 | `a rainbow trout with a glowing rainbow stripe along its body, sparkly` |
| [ ] | `mushroom_catfish.jpg` | 🍄 버섯 메기 | `a catfish with a cute red-spotted mushroom cap on its head` |

### ✨ 희귀

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `red_seabream.jpg` | 🐠 참돔 | `an elegant pink-red sea bream with a tiny crown, celebratory` |
| [ ] | `mandarin_fish.jpg` | 🐠 쏘가리 | `a mandarin fish with bold leopard-like patterns, cool sunglasses` |
| [ ] | `salmon.jpg` | 🐟 연어 | `a determined salmon jumping up a tiny waterfall, sparkling droplets` |
| [ ] | `sea_bass.jpg` | 🐟 농어 | `a sleek silver sea bass with a calm cool expression` |
| [ ] | `octopus.jpg` | 🐙 문어 | `a round red octopus giving a big eight-armed hug` |
| [ ] | `lobster.jpg` | 🦞 랍스터 | `a proud red lobster flexing its big claws` |
| [ ] | `butterflyfish.jpg` | 🦋 나비고기 | `a yellow butterflyfish with fins like butterfly wings, fluttering` |
| [ ] | `thunder_eel.jpg` | ⚡ 번개 뱀장어 | `a long eel crackling with tiny cute lightning sparks, hair sticking up` |
| [ ] | `ice_trout.jpg` | ❄️ 얼음 송어 | `a trout made of sparkling ice crystals, frosty breath` |
| [ ] | `flame_goldfish.jpg` | 🔥 불꽃 금붕어 | `a goldfish with flickering little flame fins, warm glow` |
| [ ] | `pearl_clam.jpg` | 🐚 진주조개 | `an open clam holding a big glowing pearl like a treasure, proud smile` |
| [ ] | `moon_jellyfish.jpg` | 🌙 달빛 해파리 | `a translucent jellyfish glowing softly like the moon at night` |
| [ ] | `firefly_squid.jpg` | ✨ 반딧불 오징어 | `a tiny squid glowing with blue firefly dots at night` |

### 🔥 대물

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `tuna.jpg` | 🐟 참치 | `a big strong tuna with a muscular cute pose, sporty` |
| [ ] | `shark.jpg` | 🦈 상어 | `a chubby friendly shark with a toothy grin and a tiny party hat` |
| [ ] | `sturgeon.jpg` | 🐟 철갑상어 | `an ancient-looking sturgeon with bony plates and a monocle, gentlemanly` |
| [ ] | `sunfish.jpg` | 🐡 개복치 | `a huge round ocean sunfish floating flat, blissfully sunbathing` |
| [ ] | `giant_squid.jpg` | 🦑 대왕오징어 | `a giant squid with huge round eyes, shyly hugging itself with tentacles` |
| [ ] | `marlin.jpg` | 🐟 청새치 | `a marlin with a long sword-like nose leaping, dramatic and dashing` |
| [ ] | `hammerhead.jpg` | 🦈 망치상어 | `a hammerhead shark with a goofy wide head, cross-eyed smile` |
| [ ] | `crystal_turtle.jpg` | 🐢 수정 거북 | `a sea turtle with a shell made of glowing crystals, serene` |
| [ ] | `treasure_chest.jpg` | 💰 해적의 보물상자 | `a treasure chest with a happy face, mouth open showing gold coins` |
| [ ] | `ghost_ray.jpg` | 👻 유령 가오리 | `a translucent ghostly manta ray with a cute boo face, glowing at night` |

### 🌟 전설

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `golden_carp.jpg` | 🐉 황금 잉어 | `a majestic golden carp with dragon-like whiskers, shining scales` |
| [ ] | `coelacanth.jpg` | 🦕 실러캔스 | `an ancient blue coelacanth with white spots and a tiny fossil hat` |
| [ ] | `sperm_whale.jpg` | 🐋 향유고래 | `a huge gentle sperm whale with a big boxy head and kind eyes` |
| [ ] | `blue_dragon.jpg` | 🐉 청룡 | `a small chubby blue eastern dragon swimming, playful whiskers` |
| [ ] | `kraken.jpg` | 🐙 크라켄 | `a cute chubby kraken with big eyes, tentacles curled shyly` |
| [ ] | `narwhal.jpg` | 🦄 일각고래 | `a narwhal with a long sparkly spiral horn like a unicorn` |
| [ ] | `lava_shark.jpg` | 🌋 용암 상어 | `a shark with glowing lava-crack patterns, warm and fiery but smiling` |
| [ ] | `dragon_palace_letter.jpg` | 📜 용궁의 초대장 | `an ornate scroll letter with a dragon seal floating, sparkles` |
| [ ] | `abyss_eye.jpg` | 👁️ 심해의 눈 | `a deep-sea creature that is one huge curious round eye with tiny fins, glowing` |

### 👑 초대박

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `golden_whale.jpg` | 🐳 황금 고래 | `a giant golden whale shimmering with coins in its spout` |
| [ ] | `galaxy_whale.jpg` | 🌌 은하수 고래 | `a whale whose body is a starry galaxy, nebula fins, dreamy` |
| [ ] | `island_turtle.jpg` | 🏝️ 움직이는 섬 | `a giant turtle carrying a tiny island with a palm tree on its back` |

### 🐉 신화 (해왕류)

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `sk_steel.jpg` | 🐉 강철비늘 해왕류 | `a long sea serpent with shiny steel scales and a tiny storm cloud above, proud` |
| [ ] | `sk_abyss.jpg` | 🦑 심연아귀 해왕류 | `an anglerfish sea serpent with a glowing green lantern, sleepy cute` |
| [ ] | `sk_thunder.jpg` | ⚡ 천둥뿔 해왕류 | `a sea serpent with a lightning-shaped horn, sparks crackling, excited` |
| [ ] | `sk_bone.jpg` | 💀 백골이빨 해왕류 | `a white bony sea serpent in icy water with an aurora overhead, shy` |
| [ ] | `sk_king.jpg` | 👑 해왕류의 왕 | `a big sea serpent king with a lava-red body and a crown, warm and regal` |

### ☠️ 재앙급 (해왕류)

| 다시 뽑기 | 파일 | 이름 | 묘사 |
|---|---|---|---|
| [ ] | `cal_abyss.jpg` | 🌊 청해룡 아비스 | `an enormous deep-blue sea dragon wrapped in a cozy dark cloud blanket, yawning` |
| [ ] | `cal_liras.jpg` | 🐋 백경의 리라스 | `an enormous glowing white whale flying in the sky, singing a lullaby` |
| [ ] | `cal_kraken.jpg` | 🐙 붉은문어 크라켄 | `an enormous red octopus with a huge appetite, holding a fork and napkin` |
| [ ] | `cal_naias.jpg` | 🐲 나락의 제왕 나이아스 | `an enormous swirling dragon king making whirlpools, dizzy happy face` |
| [ ] | `cal_teranos.jpg` | 🐢 대지거북 테라노스 | `an enormous turtle with a forest and a little temple on its back, sleepy` |
| [ ] | `cal_arka.jpg` | 🦈 심연의 아르카 | `an enormous dreamy shark-like spirit surrounded by floating memory bubbles` |
| [ ] | `cal_chronos.jpg` | ⏳ 다크피쉬 크로노스 | `an enormous dark fish with clock patterns, holding a tiny hourglass` |
| [ ] | `cal_aurora.jpg` | 🪼 빛의 군주 아우로라 | `an enormous jellyfish made of soft aurora light, shining gently` |

---

## 🧑‍✈️ 선원 (832×1216)

**프롬프트 = `[귀여움]` + 선원 앞부분 + 칸의 묘사**

선원 앞부분:
```
A cute chibi character portrait, big head small body, big sparkly eyes, friendly expression, standing on a small boat deck with the sea behind, upper body,
```
> 등급이 높을수록 끝에 덧붙이기: 영웅 `, sparkly purple aura` · 전설 `, golden sparkles and a soft halo glow` · 신화 `, cosmic starry aura, magical floating particles`.
> 지금 코드는 전설 이상만 초상화를 카드로 보낸다. 일반~영웅은 원하면 뽑아 두고 쓰면 된다.


### 요리사

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `cook_c.jpg` | 일반 | 덕배 | `a burly young sailor cook with a bandana grilling fish skewers` |
| [ ] | `cook_u.jpg` | 고급 | 분식집 순자 | `a cheerful middle-aged snack-bar auntie with an apron and a pot of tteokbokki` |
| [ ] | `cook_r.jpg` | 희귀 | 칼잡이 미숙 | `a cool girl sushi chef with a headband holding a shiny knife` |
| [ ] | `cook_h.jpg` | 영웅 | 궁중요리사 강 | `an elegant royal court chef in traditional hanbok-style uniform` |
| [ ] | `cook_l.jpg` | 전설 | 불꽃손 마르코 | `a passionate chef with flames bursting from a wok, big grin` |
| [ ] | `cook_l2.jpg` | 전설 | 달빛 파티시에 세라 | `a dreamy pastry chef girl with moon-shaped desserts, starry apron` |

### 행운펫

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `pet_c.jpg` | 일반 | 똥개 복실이 | `a scruffy fluffy mutt puppy with a wagging tail` |
| [ ] | `pet_u.jpg` | 고급 | 뚱냥 치즈 | `a chubby orange cheese-colored cat lying belly up` |
| [ ] | `pet_r.jpg` | 희귀 | 삼색냥 나비 | `a calico cat with a butterfly perched on its nose` |
| [ ] | `pet_h.jpg` | 영웅 | 백호 새끼 호돌 | `a baby white tiger cub with a tiny sailor hat` |
| [ ] | `pet_l.jpg` | 전설 | 구미호 연화 | `a nine-tailed fox spirit girl with fluffy tails and a moon hairpin` |
| [ ] | `pet_l2.jpg` | 전설 | 백호 무진 | `a majestic but fluffy white tiger with storm-blue stripes` |

### 해적

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `pirate_c.jpg` | 일반 | 외눈 철수 | `a one-eyed young pirate with an eyepatch, sneaky grin` |
| [ ] | `pirate_u.jpg` | 고급 | 술고래 박선장 | `a red-nosed jolly pirate captain holding a mug` |
| [ ] | `pirate_r.jpg` | 희귀 | 갈고리 장미 | `a pirate girl with a hook hand and a rose in her hair` |
| [ ] | `pirate_h.jpg` | 영웅 | 붉은수염 바르바 | `a big red-bearded pirate with braided beard, hearty laugh` |
| [ ] | `pirate_l.jpg` | 전설 | 진홍의 레온 | `a dashing crimson-coated pirate with a feathered hat` |
| [ ] | `pirate_l2.jpg` | 전설 | 폭풍의 카밀라 | `a fierce pirate captain girl with storm-gray hair and lightning earrings` |

### 목수

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `carpenter_c.jpg` | 일반 | 망치 영식 | `a sturdy young carpenter with a big hammer, sweat drop` |
| [ ] | `carpenter_u.jpg` | 고급 | 톱질 막내 | `a small rookie carpenter kid carrying a saw bigger than himself` |
| [ ] | `carpenter_r.jpg` | 희귀 | 대들보 김목수 | `a reliable carpenter with a pencil behind the ear holding a beam` |
| [ ] | `carpenter_h.jpg` | 영웅 | 도편수 영감 | `an old master shipwright grandpa with round glasses` |
| [ ] | `carpenter_l.jpg` | 전설 | 천년목 하율 | `a forest-spirit carpenter with leaves in their hair and a wooden mallet` |
| [ ] | `carpenter_l2.jpg` | 전설 | 목련 장인 서아 | `a graceful carpenter girl carving magnolia flowers into wood` |

### 비서

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `secretary_c.jpg` | 일반 | 인턴 민지 | `a nervous intern girl hugging a stack of papers` |
| [ ] | `secretary_u.jpg` | 고급 | 계약직 도윤 | `a contract worker boy with a laptop and coffee, tired smile` |
| [ ] | `secretary_r.jpg` | 희귀 | 엑셀장인 하윤 | `a spreadsheet genius girl with glasses and floating charts` |
| [ ] | `secretary_h.jpg` | 영웅 | 비서실장 서진 | `a sharp chief secretary in a neat suit with a tablet` |
| [ ] | `secretary_l.jpg` | 전설 | 만능비서 세바스찬 | `a perfect butler-secretary with a monocle and a tea set` |
| [ ] | `secretary_l2.jpg` | 전설 | 완벽비서 유나 | `a flawless secretary girl with a planner and a sparkly pen` |

### 낚시꾼

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `angler_c.jpg` | 일반 | 낚시광 만수 | `a fishing-crazy guy in a bucket hat holding a rod, excited` |
| [ ] | `angler_u.jpg` | 고급 | 쌍낚대 영철 | `an angler holding two fishing rods at once, proud` |
| [ ] | `angler_r.jpg` | 희귀 | 물때박사 은비 | `a tide-expert girl reading a tide chart with a magnifying glass` |
| [ ] | `angler_h.jpg` | 영웅 | 강태공 노인 | `a calm old angler grandpa with a long white beard and a bamboo rod` |
| [ ] | `angler_l.jpg` | 전설 | 은빛 낚싯대 리안 | `a young angler with a gleaming silver fishing rod, heroic pose` |
| [ ] | `angler_l2.jpg` | 전설 | 달빛 낚시꾼 하린 | `a moonlit angler girl with a crescent-moon rod` |

### 유령

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `ghost_l.jpg` | 전설 | 저승 뱃사공 카론 | `a cute ghost ferryman with a hooded cloak and a tiny oar, gentle` |
| [ ] | `ghost_l2.jpg` | 전설 | 등불지기 연 | `a cute ghost girl holding a warm glowing lantern` |

### 마스코트

| 다시 뽑기 | 파일 | 등급 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `muneung.jpg` | 전설 | 무능 | `a small round fluffy yellow chick mascot with a tiny sailor hat, confused` |

### 🌌 신화 선원 (60명)

| 다시 뽑기 | 파일 | 역할 | 이름 | 묘사 |
|---|---|---|---|---|
| [ ] | `cook_m1.jpg` | 요리사 | 해룡 셰프 청운 | `a dragon-clan chef with small horns and a jade apron` |
| [ ] | `cook_m2.jpg` | 요리사 | 심연의 미식가 루시엘 | `a mysterious deep-sea gourmet with glowing bioluminescent chopsticks` |
| [ ] | `cook_m3.jpg` | 요리사 | 화산 주방장 바르칸 | `a volcano chef cooking on a lava stone, fiery hair` |
| [ ] | `cook_m4.jpg` | 요리사 | 빙해 디저트 장인 시아 | `an icy dessert artisan girl with snowflake pastries` |
| [ ] | `cook_m5.jpg` | 요리사 | 독의 요리사 베노아 | `a poison chef with purple bottles, mischievous wink` |
| [ ] | `cook_m6.jpg` | 요리사 | 용궁 수라간 연화 | `a dragon-palace royal kitchen lady with a pearl hairpin` |
| [ ] | `cook_m7.jpg` | 요리사 | 바비큐 대장 드레이크 | `a barbecue boss with a giant grill and a smoky grin` |
| [ ] | `cook_m8.jpg` | 요리사 | 달빛 제빵사 루나 | `a moonlight baker girl with crescent bread` |
| [ ] | `cook_m9.jpg` | 요리사 | 번개칼 카이토 | `a lightning knife chef slicing fish in a flash` |
| [ ] | `cook_m10.jpg` | 요리사 | 정수 연금술사 엘릭서 | `an alchemist chef with bubbling glowing potions` |
| [ ] | `pet_m1.jpg` | 행운펫 | 진주 해달 몽글 | `a sea otter floating on its back holding a pearl` |
| [ ] | `pet_m2.jpg` | 행운펫 | 구름고래 포포 | `a tiny cloud whale floating in the air` |
| [ ] | `pet_m3.jpg` | 행운펫 | 물결여우 소금 | `a wave fox with a tail like a curling wave` |
| [ ] | `pet_m4.jpg` | 행운펫 | 뿔고래 일각 | `a baby narwhal with a little horn` |
| [ ] | `pet_m5.jpg` | 행운펫 | 천둥냥 번쩍 | `a thunder cat with sparking fur standing up` |
| [ ] | `pet_m6.jpg` | 행운펫 | 서리물범 눈꽃 | `a frosty baby seal with snowflake spots` |
| [ ] | `pet_m7.jpg` | 행운펫 | 달토끼 미리내 | `a moon rabbit holding a little mallet` |
| [ ] | `pet_m8.jpg` | 행운펫 | 화산 레서판다 불씨 | `a volcano red panda with an ember on its tail` |
| [ ] | `pet_m9.jpg` | 행운펫 | 안개사슴 아련 | `a misty deer with antlers fading into fog` |
| [ ] | `pet_m10.jpg` | 행운펫 | 황금 물개 금비 | `a golden seal clapping its flippers` |
| [ ] | `pirate_m1.jpg` | 해적 | 해왕 여제 세일라 | `a sea-king empress pirate with a coral crown` |
| [ ] | `pirate_m2.jpg` | 해적 | 진홍 폭풍 레이븐 | `a crimson storm pirate with a raven on the shoulder` |
| [ ] | `pirate_m3.jpg` | 해적 | 망령선장 모르간 | `a cute ghost pirate captain, translucent, friendly` |
| [ ] | `pirate_m4.jpg` | 해적 | 사막해의 자라 | `a desert-sea pirate girl with a sand-colored scarf` |
| [ ] | `pirate_m5.jpg` | 해적 | 빙해 약탈자 프레이야 | `an ice-sea raider girl with a fur cape and frosty axe` |
| [ ] | `pirate_m6.jpg` | 해적 | 심연 작살꾼 바다르 | `an abyss harpoon pirate with a glowing harpoon` |
| [ ] | `pirate_m7.jpg` | 해적 | 황금닻 레오니다스 | `a golden anchor pirate with a huge golden anchor` |
| [ ] | `pirate_m8.jpg` | 해적 | 장미 쌍권총 로즈 | `a rose twin-pistol pirate girl winking` |
| [ ] | `pirate_m9.jpg` | 해적 | 용왕의 아들 해랑 | `a runaway dragon prince pirate with small horns` |
| [ ] | `pirate_m10.jpg` | 해적 | 번개 함장 볼트 | `a lightning captain with electric hair and goggles` |
| [ ] | `carpenter_m1.jpg` | 목수 | 송곳니 망치 도윤 | `a fang-hammer carpenter with a shark-tooth mallet` |
| [ ] | `carpenter_m2.jpg` | 목수 | 산호 건축가 마리나 | `a coral architect girl building a coral house` |
| [ ] | `carpenter_m3.jpg` | 목수 | 강철팔 아이언 | `a carpenter with a shiny steel robot arm` |
| [ ] | `carpenter_m4.jpg` | 목수 | 세계수 목공 엘린 | `a world-tree carpenter elf with leaf ears` |
| [ ] | `carpenter_m5.jpg` | 목수 | 고대 룬 장인 토르빈 | `an ancient rune craftsman with glowing rune chisel` |
| [ ] | `carpenter_m6.jpg` | 목수 | 증기 기관사 노바 | `a steam engineer girl with goggles and a wrench` |
| [ ] | `carpenter_m7.jpg` | 목수 | 뼈 조각가 오스카 | `a bone sculptor with carved whale-bone charms` |
| [ ] | `carpenter_m8.jpg` | 목수 | 빙결 조선공 유키 | `an ice shipwright girl carving an ice boat` |
| [ ] | `carpenter_m9.jpg` | 목수 | 용골 수호자 강철 | `a keel guardian with a sturdy shield-like plank` |
| [ ] | `carpenter_m10.jpg` | 목수 | 별의 설계자 아스트라 | `a star architect girl drawing constellations as blueprints` |
| [ ] | `secretary_m1.jpg` | 비서 | 심해 항해사 리베라 | `a deep-sea navigator with a glowing compass` |
| [ ] | `secretary_m2.jpg` | 비서 | 금화 회계사 골디 | `a gold-coin accountant with an abacus of coins` |
| [ ] | `secretary_m3.jpg` | 비서 | 시간 관리인 크로나 | `a time keeper girl holding a pocket watch` |
| [ ] | `secretary_m4.jpg` | 비서 | 정보상 섀도 | `a shadowy info broker with a hood and a sly smile` |
| [ ] | `secretary_m5.jpg` | 비서 | 용궁 서기관 해윤 | `a dragon-palace scribe with a brush and scroll` |
| [ ] | `secretary_m6.jpg` | 비서 | 마법 사서 아르카나 | `a magic librarian girl with floating books` |
| [ ] | `secretary_m7.jpg` | 비서 | 심해 집사 노블 | `a deep-sea butler with a jellyfish lamp` |
| [ ] | `secretary_m8.jpg` | 비서 | 계약의 마녀 릴리스 | `a contract witch girl with a glowing quill` |
| [ ] | `secretary_m9.jpg` | 비서 | 점성술사 셀레네 | `an astrologer girl with a starry telescope` |
| [ ] | `secretary_m10.jpg` | 비서 | 해도 제작자 마젤 | `a sea chart maker with rolled maps` |
| [ ] | `angler_m1.jpg` | 낚시꾼 | 백발의 하루 | `a white-haired dreamy angler with a gentle forgetful smile` |
| [ ] | `angler_m2.jpg` | 낚시꾼 | 달의 낚시꾼 세레나 | `a moon angler girl fishing in moonlight` |
| [ ] | `angler_m3.jpg` | 낚시꾼 | 폭풍 낚시꾼 썬더 | `a storm angler with a lightning rod` |
| [ ] | `angler_m4.jpg` | 낚시꾼 | 신선 낚시꾼 청명 | `an immortal hermit angler on a cloud` |
| [ ] | `angler_m5.jpg` | 낚시꾼 | 심해 잠수부 마린 | `a deep-sea diver angler with a round helmet` |
| [ ] | `angler_m6.jpg` | 낚시꾼 | 황금그물 페드로 | `an angler with a golden net` |
| [ ] | `angler_m7.jpg` | 낚시꾼 | 오로라 얼음낚시꾼 니바 | `an aurora ice-fishing girl in a fluffy parka` |
| [ ] | `angler_m8.jpg` | 낚시꾼 | 별을 낚는 스텔라 | `a star-fishing girl catching stars with her rod` |
| [ ] | `angler_m9.jpg` | 낚시꾼 | 갈고리 잭 | `a hook-hand angler grinning` |
| [ ] | `angler_m10.jpg` | 낚시꾼 | 천재 꼬마선장 해솔 | `a genius kid captain girl with a sea-blue headband and oversized captain hat` |

---

## 그 밖에 다시 뽑을 수 있는 것

| 무엇 | 어디 프롬프트 |
|---|---|
| 스토리 장면 · 스토리 인물 | `fishing-story-prompts.md` (귀여운 버전으로 다시 씀) |
| 5장 올 블루 장면 · 봉인 · 출신 표지 | `fishing-story-allblue-prompts.md` (귀여운 버전으로 다시 씀) |
| 배 이야기 NPC · ★5 장면 | `fishing-story-ships.md` 맨 아래 (귀여운 버전으로 다시 씀) |
| 배 25장 · 의료선 | `ships-solo.md` 맨 아래 — 앞에 `[귀여움]`만 붙이면 됨 |
| NPC 배 · NPC 해적 · 항구 | `season2-ships-prompts.md` · `pvp-rework.md` — 앞에 `[귀여움]`을 붙이고, `menacing`·`scarred` 같은 무서운 말은 빼고 쓴다 |
| 선원 갑판 장면(`scene_<id>.jpg`) | 위 선원 묘사 + `, doing their job happily on deck` |
