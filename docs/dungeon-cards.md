# 카드 던전 — 카드 목록 (첫 출시 5구역 · 70장)

> `docs/dungeon-game.md`의 카드 목록. 구역(10층)마다 13장 + 보스 카드 1장.
> 소환은 **내가 도달한 구역까지의** 카드에서만 나온다. 보스 카드는 그 보스를 처음 잡을 때 자동 획득.
> 카드는 시즌마다 구역을 추가해서 계속 늘린다.

## 그림 프롬프트 쓰는 법

- **사람 카드**: `[인물]` + 매력 꼬리 + 묘사
- **몬스터·동물 카드**: `[귀여움]` + 묘사
- 크기 832×1216. 카드 테두리(등급 색)는 봇이 덧씌운다.
- SSR 이상은 ★3·★5 각성 그림도: 같은 묘사 끝에 `, awakened form, more ornate outfit, glowing aura` (★3) / `, ultimate form, radiant wings of light, epic background` (★5)

`[인물]` (= 낚시 `[선원]` 문구에서 배경만 바꿈):
```
Beautiful anime-style character illustration, detailed attractive face, expressive eyes, stylish fantasy outfit, confident pose, soft cinematic lighting, vibrant colors, clean lineart, fantasy dungeon background, upper body portrait, no text, no watermark.
```

`[귀여움]`:
```
Cute kawaii storybook illustration, soft pastel colors, rounded chubby shapes, big sparkly eyes, gentle cel shading, soft clean outlines, cheerful warm lighting, simple uncluttered composition, no text, no letters, no watermark.
```

매력 꼬리: 💕 `adorable and charming, bright friendly smile,` · 😎 `handsome adult man, sharp jawline, confident charming gaze,` · 🌸 `beautiful adult woman, elegant graceful features, gentle captivating gaze,` · 🔥 `alluring adult, glamorous and self-assured, stylish form-fitting outfit, fully clothed, tasteful,`

속성: 🔥불 · 💧물 · 🌿풀 · ✨빛 · 🌑그림자

---

## 1구역 · 1~10층 「이끼 동굴」

> 촉촉한 이끼와 지하 호수가 있는 첫 동굴. 처음 들어온 모험가들의 놀이터.

| 다시 뽑기 | 파일 | 등급 | 속성 | 이름 | 한 줄 | 그림 | 묘사 |
|---|---|---|---|---|---|---|---|
| [ ] | `c1_n1.jpg` | N | 🌿 | 이끼 슬라임 | 밟으면 폭신, 화내도 폭신 | 귀여움 | `A cute green slime covered in soft moss with a tiny sprout on top, bouncing on a mossy cave floor.` |
| [ ] | `c1_n2.jpg` | N | 💧 | 물방울 박쥐 | 거꾸로 매달려 물방울을 모으는 박쥐 | 귀여움 | `A cute little bat hanging upside down holding a big shiny water droplet, damp glowing cave.` |
| [ ] | `c1_n3.jpg` | N | 🌿 | 버섯 꼬마 | 머리 갓이 우산이 되는 버섯 | 귀여움 | `A cute walking mushroom creature using its cap as an umbrella under dripping water.` |
| [ ] | `c1_r1.jpg` | R | 💧 | 등불 게 크랩씨 | 집게에 등불 들고 길 안내 | 귀여움 | `A cute crab holding a tiny lantern in one claw, guiding the way in a dark wet cave.` |
| [ ] | `c1_r2.jpg` | R | 🌿 | 초보 모험가 핀 | 나무검 하나로 시작한 열정맨 | 😎 | `a young adventurer man with a wooden sword and a patched cloak, eager grin, mossy cave entrance.` |
| [ ] | `c1_r3.jpg` | R | 🔥 | 반딧불 정령 | 동굴을 밝히는 작은 불빛 | 귀여움 | `A cute tiny fire spirit like a glowing firefly with a happy face, lighting up a dark cave.` |
| [ ] | `c1_sr1.jpg` | SR | 🌿 | 약초꾼 소라 | 동굴 약초는 다 아는 약초꾼 | 🌸 | `a gentle herbalist woman with a basket of glowing herbs and a leaf hairpin, kneeling by a moss patch.` |
| [ ] | `c1_sr2.jpg` | SR | 💧 | 지하호수 인어 마린 | 지하 호수에 사는 인어 | 🌸 | `a mermaid woman with teal hair resting on a rock in a glowing underground lake, shell accessories.` |
| [ ] | `c1_sr3.jpg` | SR | 🌑 | 그림자 도적 카이 | 동굴 보물만 노리는 날쌘 도적 | 😎 | `a nimble thief man with a dark hood, a dagger and a smirk, crouching on a ledge with a stolen gem.` |
| [ ] | `c1_ssr1.jpg` | SSR | 🌿 | 숲의 궁수 엘라 | 바람 소리로 과녁을 맞히는 엘프 | 🌸 | `an elf archer woman with long braided hair and a vine-wrapped bow, drawing an arrow of green light.` |
| [ ] | `c1_ssr2.jpg` | SSR | 💧 | 폭포 수호자 오르카 | 지하 폭포를 지키는 전사 | 😎 | `a muscular warrior man with orca-pattern armor and a water trident, standing before an underground waterfall.` |
| [ ] | `c1_ur1.jpg` | UR | 🌿 | 이끼 여왕 모스 | 동굴의 모든 이끼가 그녀를 따른다 | 🔥 | `a dryad queen with a crown of moss and flowers, flowing green dress of leaves, glowing spores around her.` |
| [ ] | `c1_lr1.jpg` | LR | 💧 | 지하 호수의 용 아쿠아 | 호수 바닥에서 잠자던 물의 용 | 귀여움 | `A majestic but adorable blue water dragon rising from a glowing underground lake, sparkling droplets, giant and gentle.` |
| — | `boss_10.jpg` | 보스 | 🌿 | 졸린 문지기 골렘 | 1구역 보스. 졸려서 자꾸 문을 열어 준다 | 귀여움 | `A big round stone golem guarding a dungeon door, yawning with sleepy eyes, moss and tiny flowers on its shoulders.` |

## 2구역 · 11~20층 「거울 미궁」

> 벽이 전부 거울인 미로. 빛과 그림자가 서로를 비춘다.

| 다시 뽑기 | 파일 | 등급 | 속성 | 이름 | 한 줄 | 그림 | 묘사 |
|---|---|---|---|---|---|---|---|
| [ ] | `c2_n1.jpg` | N | ✨ | 거울 요정 | 거울 속에서 손 흔드는 요정 | 귀여움 | `A cute tiny fairy waving from inside a mirror, sparkles around the frame.` |
| [ ] | `c2_n2.jpg` | N | 🌑 | 그림자 꼬물이 | 누구 그림자인지 모를 꼬물이 | 귀여움 | `A cute round shadow blob with big white eyes peeking from behind a mirror.` |
| [ ] | `c2_n3.jpg` | N | ✨ | 촛불 유령 | 촛불 하나 들고 길 잃은 유령 | 귀여움 | `A cute little ghost holding a candle, lost in a hall of mirrors.` |
| [ ] | `c2_r1.jpg` | R | 🌑 | 가면 광대 피에로 | 웃는 가면 뒤의 장난꾸러기 | 😎 | `a handsome harlequin jester man with a half mask and diamond-pattern costume, juggling glowing orbs.` |
| [ ] | `c2_r2.jpg` | R | ✨ | 견습 성녀 루미 | 기도하면 가끔 빛이 나는 견습생 | 💕 | `a young woman apprentice priestess with a white veil and a small glowing staff, earnest smile.` |
| [ ] | `c2_r3.jpg` | R | 🌑 | 까마귀 우편부 | 미궁 안 편지 배달 담당 | 귀여움 | `A cute crow wearing a tiny postman cap carrying a letter in its beak.` |
| [ ] | `c2_sr1.jpg` | SR | ✨ | 거울 기사 세라핀 | 거울 방패로 빛을 튕기는 기사 | 🌸 | `a knight woman in silver mirror-polished armor with a reflective shield, light beams bouncing.` |
| [ ] | `c2_sr2.jpg` | SR | 🌑 | 마술사 제로 | 거울 사이로 사라지는 마술사 | 😎 | `a stage magician man in a black tailcoat and top hat, cards and shadows swirling around him.` |
| [ ] | `c2_sr3.jpg` | SR | ✨ | 수정 유니콘 | 뿔이 수정으로 된 유니콘 | 귀여움 | `A cute small unicorn with a crystal horn and a pastel mane in a mirror maze.` |
| [ ] | `c2_ssr1.jpg` | SSR | ✨ | 성기사 아론 | 빛의 방패를 든 성기사 | 😎 | `a golden-armored paladin man with a radiant shield and a gentle smile, holy light rays.` |
| [ ] | `c2_ssr2.jpg` | SSR | 🌑 | 밤의 무희 릴리 | 그림자로 춤추는 무희 | 🔥 | `a dancer woman in a flowing dark violet dress with shadow ribbons swirling as she spins.` |
| [ ] | `c2_ur1.jpg` | UR | 🌑 | 그림자 군주 녹스 | 미궁의 모든 그림자를 다스린다 | 😎 | `a mysterious shadow lord man with silver hair, a long dark coat with purple flames, glowing violet eyes.` |
| [ ] | `c2_lr1.jpg` | LR | ✨ | 빛의 대천사 세레스 | 거울 미궁 꼭대기에 내려온 천사 | 🌸 | `an archangel woman with six radiant wings and a halo, white and gold robes, descending through mirrors of light.` |
| — | `boss_20.jpg` | 보스 | 🌑 | 거울 마녀 미라 | 2구역 보스. 거울 보며 화장하느라 바쁨 | 🔥 | `a glamorous witch woman with a pointed hat admiring herself in a giant ornate mirror, holding a makeup brush wand.` |

## 3구역 · 21~30층 「용암 대장간」

> 용암이 흐르는 거대한 대장간. 최고의 무기가 여기서 태어난다.

| 다시 뽑기 | 파일 | 등급 | 속성 | 이름 | 한 줄 | 그림 | 묘사 |
|---|---|---|---|---|---|---|---|
| [ ] | `c3_n1.jpg` | N | 🔥 | 불씨 도마뱀 | 꼬리에 불씨 달린 도마뱀 | 귀여움 | `A cute little salamander with a flickering ember on its tail, sitting on warm stones.` |
| [ ] | `c3_n2.jpg` | N | 🔥 | 숯덩이 골렘 | 손대면 따끈한 숯 골렘 | 귀여움 | `A cute tiny charcoal golem with glowing orange cracks and a happy face.` |
| [ ] | `c3_n3.jpg` | N | 💧 | 김 요정 | 용암에 물 닿을 때 태어나는 요정 | 귀여움 | `A cute fluffy steam spirit puffing out of a hot spring, round cloud body.` |
| [ ] | `c3_r1.jpg` | R | 🔥 | 견습 대장장이 버크 | 망치질 천 번째 날 | 😎 | `a young blacksmith man with a leather apron and soot on his cheek, hammering a glowing sword.` |
| [ ] | `c3_r2.jpg` | R | 🔥 | 화산 토끼 | 귀 끝이 불꽃인 토끼 | 귀여움 | `A cute rabbit with flame-tipped ears hopping near a lava stream.` |
| [ ] | `c3_r3.jpg` | R | 🌑 | 연기 도깨비 | 굴뚝 연기로 장난치는 도깨비 | 귀여움 | `A cute little smoke goblin with a mischievous grin floating out of a chimney.` |
| [ ] | `c3_sr1.jpg` | SR | 🔥 | 불꽃 검사 레아 | 불타는 대검의 검사 | 🌸 | `a fiery swordswoman with crimson hair and a flaming greatsword, ember particles swirling.` |
| [ ] | `c3_sr2.jpg` | SR | 🔥 | 아기 용암 거인 | 아직 무릎 높이밖에 안 되는 거인 | 귀여움 | `A cute baby lava giant made of rock and glowing magma, holding a little hammer.` |
| [ ] | `c3_sr3.jpg` | SR | ✨ | 황금 세공사 골디아 | 보석에 빛을 새기는 세공사 | 🌸 | `a jeweler woman with magnifying goggles holding a glowing gem, gold tools on her belt.` |
| [ ] | `c3_ssr1.jpg` | SSR | 🔥 | 화염 마법사 이그니스 | 불을 손끝으로 접는 마법사 | 😎 | `a fire mage man with flowing red robes conjuring a spiral of flames from his fingertips.` |
| [ ] | `c3_ssr2.jpg` | SSR | 🔥 | 불사조 피닉 | 꺼져도 다시 타오르는 새 | 귀여움 | `A majestic but cute phoenix with blazing feathers rising from a brazier, sparks everywhere.` |
| [ ] | `c3_ur1.jpg` | UR | 🔥 | 화산의 여제 볼카 | 대장간의 주인 | 🔥 | `a volcano empress with obsidian crown and molten-gold jewelry, a fiery gown, lava rivers behind her.` |
| [ ] | `c3_lr1.jpg` | LR | 🔥 | 태양룡 솔 | 대장간 불을 처음 붙인 용 | 귀여움 | `A majestic but adorable golden sun dragon wreathed in gentle flames, glowing like a sunrise.` |
| — | `boss_30.jpg` | 보스 | 🔥 | 대장장이 드래곤 루비 | 3구역 보스. 무기 만들기에 진심인 용 | 귀여움 | `A chubby red dragon wearing a blacksmith apron and goggles, hammering on an anvil with sparks flying.` |

## 4구역 · 31~40층 「얼음 도서관」

> 얼어붙은 책장이 끝없이 이어진 도서관. 조용히 하세요.

| 다시 뽑기 | 파일 | 등급 | 속성 | 이름 | 한 줄 | 그림 | 묘사 |
|---|---|---|---|---|---|---|---|
| [ ] | `c4_n1.jpg` | N | 💧 | 눈송이 정령 | 책장 위에 내려앉는 눈송이 | 귀여움 | `A cute snowflake spirit with a tiny face floating above frosty bookshelves.` |
| [ ] | `c4_n2.jpg` | N | 💧 | 아기 펭귄 사서 | 책 정리 담당 펭귄 | 귀여움 | `A cute baby penguin wearing round glasses carrying a stack of books.` |
| [ ] | `c4_n3.jpg` | N | ✨ | 책벌레 | 진짜 책을 먹는 벌레 | 귀여움 | `A cute chubby bookworm with glasses munching on a page, glowing letters around.` |
| [ ] | `c4_r1.jpg` | R | 💧 | 얼음 학자 노엘 | 얼음에 글을 새기는 학자 | 😎 | `a scholar man in a fur-lined coat writing glowing runes on an ice tablet, frosty breath.` |
| [ ] | `c4_r2.jpg` | R | ✨ | 부엉이 조수 | 밤새 책을 읽어 주는 부엉이 | 귀여움 | `A cute owl reading an open book with a little candle, wearing a scarf.` |
| [ ] | `c4_r3.jpg` | R | 💧 | 서리 고양이 | 꼬리에 서리가 맺힌 고양이 | 귀여움 | `A cute fluffy white cat with frost on its tail curled up on a frozen book.` |
| [ ] | `c4_sr1.jpg` | SR | 💧 | 빙결 마법사 시린 | 숨결로 책장을 얼리는 마법사 | 🌸 | `an ice mage woman with pale blue hair and a crystal staff, snowflakes swirling around her.` |
| [ ] | `c4_sr2.jpg` | SR | ✨ | 점성가 오리온 | 천장 별자리를 읽는 점성가 | 😎 | `an astrologer man in a starry cloak pointing at constellations on a frozen dome ceiling.` |
| [ ] | `c4_sr3.jpg` | SR | 🌑 | 금서 수호자 | 가면 뒤에 금서를 지키는 자 | 😎 | `a masked guardian man in dark robes holding a chained forbidden book, mysterious aura.` |
| [ ] | `c4_ssr1.jpg` | SSR | 💧 | 눈의 여왕 아이시아 | 도서관을 얼린 장본인 | 🌸 | `a snow queen woman with an ice crystal crown and a flowing gown of frost, cold but kind eyes.` |
| [ ] | `c4_ssr2.jpg` | SSR | ✨ | 시간의 사서 크로노 | 모든 책의 마지막 장을 아는 사서 | 😎 | `a librarian man with a pocket-watch monocle surrounded by floating clock-gear books.` |
| [ ] | `c4_ur1.jpg` | UR | 💧 | 오로라 공주 보레아 | 오로라를 실로 짜는 공주 | 🌸 | `an aurora princess woman weaving ribbons of aurora light like silk, glowing northern sky behind her.` |
| [ ] | `c4_lr1.jpg` | LR | ✨ | 지혜의 고래 아스트라 | 책 속 바다를 헤엄치는 고래 | 귀여움 | `A majestic but adorable starlight whale swimming through floating open books, constellations on its body.` |
| — | `boss_40.jpg` | 보스 | 💧 | 사서장 스노우 올빼미 | 4구역 보스. 떠들면 혼난다 | 귀여움 | `A big fluffy snowy owl librarian with tiny glasses holding a "shh" finger feather, towering over bookshelves.` |

## 5구역 · 41~50층 「별빛 정원」

> 탑 안인데 하늘이 보이는 이상한 정원. 모든 속성이 모여 있다.

| 다시 뽑기 | 파일 | 등급 | 속성 | 이름 | 한 줄 | 그림 | 묘사 |
|---|---|---|---|---|---|---|---|
| [ ] | `c5_n1.jpg` | N | 🌿 | 꽃잎 요정 | 꽃잎 하나를 이불로 쓰는 요정 | 귀여움 | `A cute tiny fairy sleeping under a flower petal blanket in a starlit garden.` |
| [ ] | `c5_n2.jpg` | N | ✨ | 별똥별 다람쥐 | 떨어진 별을 도토리처럼 모음 | 귀여움 | `A cute squirrel hugging a glowing fallen star like an acorn.` |
| [ ] | `c5_n3.jpg` | N | 💧 | 이슬 개구리 | 이슬 한 방울에 들어가는 개구리 | 귀여움 | `A cute tiny frog sitting inside a giant dew drop on a leaf.` |
| [ ] | `c5_r1.jpg` | R | 🌿 | 정원사 해온 | 별빛으로 꽃에 물 주는 정원사 | 😎 | `a gardener man with a straw hat watering flowers with a can pouring starlight.` |
| [ ] | `c5_r2.jpg` | R | 🔥 | 반딧불 마녀 | 반딧불로 등불 켜는 마녀 | 💕 | `a young witch woman with a lantern full of fireflies and a cute pointed hat, cheerful.` |
| [ ] | `c5_r3.jpg` | R | 🌑 | 달그림자 여우 | 달그림자를 밟고 다니는 여우 | 귀여움 | `A cute fox with a dark crescent-moon pattern trotting on moonlit grass.` |
| [ ] | `c5_sr1.jpg` | SR | 🌿 | 장미 기사 로즈 | 장미 가시 검의 기사 | 🌸 | `a rose knight woman in red-and-green armor with a thorned rapier, petals swirling.` |
| [ ] | `c5_sr2.jpg` | SR | ✨ | 별의 음유시인 리라 | 노래하면 별이 반짝 | 🌸 | `a bard woman with a starry lyre singing, tiny stars twinkling to the music.` |
| [ ] | `c5_sr3.jpg` | SR | 💧 | 연못의 요정왕 | 연꽃 위에 앉은 요정왕 | 😎 | `a fairy king man with dragonfly wings sitting on a giant lotus in a glowing pond, elegant smile.` |
| [ ] | `c5_ssr1.jpg` | SSR | 🌿 | 꽃의 여신 플로라 | 걸음마다 꽃이 핀다 | 🌸 | `a flower goddess woman with a dress of blooming petals, flowers sprouting where she steps.` |
| [ ] | `c5_ssr2.jpg` | SSR | 🌑 | 밤의 정원사 녹턴 | 밤에만 피는 꽃을 가꾼다 | 😎 | `a night gardener man in a dark cloak tending glowing moonflowers, mysterious gentle smile.` |
| [ ] | `c5_ur1.jpg` | UR | ✨ | 별을 엮는 자 스텔라 | 별을 실처럼 엮어 하늘을 짠다 | 🔥 | `a star weaver woman pulling threads of starlight from the sky and weaving them, cosmic gown.` |
| [ ] | `c5_lr1.jpg` | LR | 🌿 | 세계수의 정령 이그드라 | 탑을 뚫고 자란 나무의 정령 | 귀여움 | `A majestic but adorable spirit of a giant world tree, a gentle leafy creature with glowing eyes and branches full of stars.` |
| — | `boss_50.jpg` | 보스 | 🌿 | 정원사 거인 미르 | 5구역 보스. 꽃을 밟을까 봐 조심조심 | 귀여움 | `A huge gentle giant with a flower crown tiptoeing carefully through a starlit garden, holding a tiny watering can.` |

---

## 분포 확인

| | N | R | SR | SSR | UR | LR | 보스 | 계 |
|---|---|---|---|---|---|---|---|---|
| 구역마다 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 14 |
| 5구역 | 15 | 15 | 15 | 10 | 5 | 5 | 5 | **70** |

- 매력 분포(사람 카드): 😎 잘생김 12 · 🌸 아름다움 11 · 🔥 섹시 4 · 💕 귀여움 2 — 나머지는 귀여운 몬스터.
- 섹시는 성인 캐릭터에만, 옷은 다 입은 채로.

## 다음 구역 아이디어 (시즌 2 이후)

| 구역 | 층 | 테마 |
|---|---|---|
| 6 | 51~60 | 🍰 과자 성 — 사탕 골렘, 케이크 기사 |
| 7 | 61~70 | ⚙️ 태엽 공장 — 로봇, 시계 장인 |
| 8 | 71~80 | 🌊 가라앉은 신전 — 인어 왕국 (낚시 세계관과 이어도 좋음) |
| 9 | 81~90 | ☁️ 구름 섬 — 하늘 고래, 바람 정령 |
| 10 | 91~100 | 🌌 탑의 바닥 — "소원을 들어주는 무언가"의 정체 |
