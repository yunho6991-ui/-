# 올 블루 편 — 그림 프롬프트 (ComfyUI)

> `docs/fishing-story-allblue.md`용입니다. 설정(크기, 스타일 고정 문구, 인물 고정 묘사, 네거티브)은 `docs/fishing-story-prompts.md`와 같습니다. 각 프롬프트 앞 `[스타일]` 자리에 그 파일의 스타일 문구를 붙이세요.

## 이미 있는 그림은 다시 뽑지 않는다

| 쓰는 곳 | 기존 그림 |
|---|---|
| 신화 5종 첫 낚시 장면 | `sk_steel.jpg` `sk_abyss.jpg` `sk_thunder.jpg` `sk_bone.jpg` `sk_king.jpg` |
| 재앙급 8종 첫 낚시 장면 | `cal_abyss.jpg` `cal_liras.jpg` `cal_kraken.jpg` `cal_naias.jpg` `cal_teranos.jpg` `cal_arka.jpg` `cal_chronos.jpg` `cal_aurora.jpg` |
| 신화 선원 60명 | 기존 초상화 `<id>.jpg` (`rpg/art/mythic_crew10`) |

> 아래 **봉인 장면**에 재앙이 나오면, 같은 모습이 되도록 그 재앙의 `cal_*.jpg`를 참조 이미지(IPAdapter / Redux)로 걸어 주세요.
> 신화 선원이 장면에 나오면 그 선원의 기존 초상화를 참조로 걸어 주세요.

---

## 5장 스토리 장면 (1216×832)

### `story_5_0.jpg` — 흐려지는 심장
```
[스타일] The seven-colored glowing sea of the All Blue at twilight, seen from a small upgraded ship, one of the seven radiant color bands flickering and fading to grey while the others pulse weakly, deep below the clear water a giant softly glowing heart-shaped light beating unevenly, eight enormous dark silhouettes stirring in the depths around it, a small round yellow chick mascot with a tiny sailor hat on the railing tilting its head in confusion, ominous but beautiful atmosphere.
```

### `story_5_9.jpg` — 다시 뛰는 심장 (결말)
```
[스타일] Epic wide view of the All Blue at sunrise, all seven color bands blazing steadily, beneath the water a giant radiant heart of light beating strongly, around it eight colossal sea beasts sleeping peacefully in a circle, a colossal volcanic sea serpent king bowing its head toward a small ship, four other great sea serpents swimming away toward the four horizons, many small fishing boats of different shapes gathered together around the heart, triumphant hopeful mood, golden morning light.
```

### `story_5_10.jpg` — 잃어버린 얼굴 (숨은 장면)
```
[스타일] Split composition at the water surface: above the surface a small energetic child captain girl with a sea-blue headband and oversized captain's hat kneels at the edge of a ship's deck looking down; below the surface, mirrored, a confident young Korean woman around twenty-five with long dark hair in a loose side braid, a sea-blue headband, light freckles, white linen shirt and brown leather vest holding a glowing silver fishing rod looks up at her, both reaching a hand toward each other through the water surface, soft light ripples where their hands meet, tender emotional reunion with one's past self, warm and cool light blending.
```
> 위쪽 꼬마선장은 기존 `angler_m10.jpg`(천재 꼬마선장 해솔)를 참조로 걸면 같은 아이로 나온다.

---

## 재앙 봉인 장면 (선택, 1216×832)

> 방 봉인 알림(📣)과 같이 보낼 그림이다. 첫 낚시 장면은 기존 `cal_*.jpg`를 쓰고, 봉인 알림에는 이걸 쓰면 "날뛰는 모습 → 잠드는 모습"으로 나뉜다.
> 필요 없으면 봉인 알림도 `cal_*.jpg`를 같이 써도 된다.

### `seal_cal_abyss.jpg` — 청해룡 아비스
```
[스타일] A colossal deep-sea dragon sinking peacefully into the abyss, the curtain of darkness around it dissolving into drifting particles, sunlight finally piercing down through the water for the first time, a faint silver glow from a fishing line at the top of the frame, serene relief after terror, deep navy blue turning to soft turquoise.
```

### `seal_cal_liras.jpg` — 백경의 리라스
```
[스타일] A gigantic luminous whale rising out of the sea into the night sky, its glowing body leaving trails of light, then curling gently as if falling asleep and drifting back down toward the ocean, music-like ripples of light spreading across a mirror-calm sea, dreamy lullaby atmosphere, soft blue and pearl tones under a full moon.
```

### `seal_cal_kraken.jpg` — 붉은문어 크라켄
```
[스타일] A colossal crimson kraken slowly releasing its tentacles from a battered ship and sinking back into the sea, the blood-red tint of the water fading to clear blue, scattered bait floating on the surface, sailors on deck exhausted but cheering, dramatic aftermath, overcast sky breaking into sunlight.
```

### `seal_cal_naias.jpg` — 나락의 제왕 나이아스
```
[스타일] A vast abyssal sea dragon king coiling downward into a whirlpool that is gradually calming, chaotic twisting ocean currents straightening into one smooth flowing direction, a ship's compass in the foreground with its needle finally steady, violet poisonous haze clearing from the water, sense of order returning, teal and deep purple tones.
```

### `seal_cal_teranos.jpg` — 대지거북 테라노스
```
[스타일] An island-sized ancient sea turtle with a forest and a ruined stone temple on its shell, slowly submerging into calm water leaving only gentle ripples instead of a tidal wave, birds flying off the trees, on the temple wall a carved relief of a girl holding a fishing rod, peaceful majestic farewell, golden afternoon light.
```

### `seal_cal_arka.jpg` — 심연의 아르카
```
[스타일] A colossal ethereal shark-like deep-sea god fading into the depths, from its body countless glowing bubbles rise toward the surface, each bubble containing a tiny scene of a memory, one large bubble near the surface showing a little girl with a sea-blue headband laughing at a harbor, melancholic and beautiful, soft violet and silver light.
```

### `seal_cal_chronos.jpg` — 다크피쉬 크로노스
```
[스타일] A colossal dark fish with clockwork-like patterns on its body being drawn up from the sea while frozen water droplets hanging in mid-air suddenly start falling again, a broken wave resuming its motion, an hourglass on the ship's deck with sand beginning to flow, time distortion ripples dissolving, surreal cinematic moment, dark teal and amber tones.
```

### `seal_cal_aurora.jpg` — 빛의 군주 아우로라
```
[스타일] A gigantic radiant jellyfish of pure light hovering above the sea, its scorching white glare softening into warm gentle aurora colors as it touches the glow of a silver fishing rod held up from a small ship, the burning sea surface cooling into shimmering calm water, awe and tranquility, aurora greens, pinks and gold.
```

---

## 출신별 표지 그림 (선택, 1216×832)

> `1신화도감`이나 `1선원`에서 출신별로 묶어 보여 줄 때 쓰는 표지. 사람은 넣지 않고 그곳 풍경만.

| 파일 | 프롬프트 |
|---|---|
| `home_abyss.jpg` | `[스타일] The lightless deep sea, a sunken mansion with faintly glowing windows on the ocean floor, bioluminescent creatures drifting, a single shaft of light from far above, mysterious and calm.` |
| `home_liras.jpg` | `[스타일] A night sky over the ocean where small cloud-whales drift among the stars, a huge full moon, ribbons of light like musical notes floating in the air, dreamy and gentle.` |
| `home_kraken.jpg` | `[스타일] A stormy crimson sea graveyard of broken pirate ships, giant tentacle marks on the rocks, red sails torn in the wind, dangerous hunting ground atmosphere.` |
| `home_naias.jpg` | `[스타일] Endless swirling ocean currents seen from above forming spiral patterns, mist banks and a faint path of calm water winding through them, a lone deer silhouette standing on a rock in the fog.` |
| `home_teranos.jpg` | `[스타일] The back of a gigantic sea turtle covered in a lush forest with a giant world tree and an ancient stone temple, coral villages along the shell's edge, waterfalls pouring into the sea.` |
| `home_arka.jpg` | `[스타일] An underwater library of memories, shelves of glowing books and floating bubbles containing faint scenes, ancient bones carved with patterns, soft violet light, quiet and nostalgic.` |
| `home_chronos.jpg` | `[스타일] A frozen moment at sea where waves are suspended mid-crash, giant clock gears half-submerged in the water, a steam engine glowing amber, droplets hanging in the air.` |
| `home_aurora.jpg` | `[스타일] A frozen polar sea under a brilliant aurora, ice floes and an ice ship sparkling, distant lightning over the horizon, fishing holes cut into the ice glowing with reflected light.` |
| `home_king.jpg` | `[스타일] An underwater dragon palace with golden roofs and coral pillars beside an erupting volcanic island, lava flowing into the sea creating steam, treasure and pearls scattered, majestic and regal.` |
