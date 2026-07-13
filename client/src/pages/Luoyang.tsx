import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import type { Character } from '../types/character';
import { loadCharacter } from '../utils/save';

export default function Luoyang() {
  const navigate = useNavigate();
  const [character, setCharacter] = useState<Character | null>(null);

  useEffect(() => {
    const loaded = loadCharacter();
    if (!loaded) {
      navigate('/');
      return;
    }
    setCharacter(loaded);
  }, [navigate]);

  if (!character) return null;

  return (
    <div className="flex h-full min-h-screen flex-col bg-gradient-to-b from-[#2a2416] via-[#1c1710] to-[#0f0d0a]">
      <div className="flex flex-1 items-center justify-center">
        <h2 className="text-3xl tracking-widest text-[#e8dfc8]">낙양</h2>
      </div>

      <div className="border-t border-[#4a3f2a] bg-[#150f0a]/90 px-6 py-4 text-[#e8dfc8]">
        <div className="mb-3 text-sm">
          <p className="font-semibold">{character.name}</p>
          <p>
            Lv.{character.level} {character.rank}
          </p>
          <p>
            HP {character.hp}/{character.maxHp}
          </p>
          <p>
            내공 {character.qi}/{character.maxQi}
          </p>
        </div>

        <nav className="grid grid-cols-4 gap-2">
          <ActionButton label="이동" />
          <ActionButton label="수련" />
          <ActionButton label="상태" />
          <ActionButton label="인벤토리" />
        </nav>
      </div>
    </div>
  );
}

function ActionButton({ label }: { label: string }) {
  return (
    <button className="rounded-md border border-[#7a6a45] bg-[#2a2115]/80 py-2 text-sm tracking-wide text-[#e8dfc8] transition hover:bg-[#3a2f1c]">
      ▶ {label}
    </button>
  );
}
