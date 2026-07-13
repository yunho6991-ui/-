import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createNewCharacter } from '../types/character';
import { saveCharacter } from '../utils/save';

export default function CharacterCreate() {
  const [name, setName] = useState('');
  const navigate = useNavigate();

  function handleStart() {
    const trimmed = name.trim();
    if (!trimmed) return;
    saveCharacter(createNewCharacter(trimmed));
    navigate('/game');
  }

  return (
    <div className="flex h-full min-h-screen flex-col items-center justify-center gap-6 bg-[#0f0d0a] px-4">
      <p className="text-xl text-[#e8dfc8]">당신의 이름을 입력하세요.</p>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleStart()}
        maxLength={12}
        autoFocus
        className="w-64 rounded-md border border-[#7a6a45] bg-[#1a140d] px-4 py-2 text-center text-lg text-[#e8dfc8] outline-none focus:border-[#c0a668]"
      />
      <button
        onClick={handleStart}
        disabled={!name.trim()}
        className="rounded-md border border-[#7a6a45] bg-[#2a2115]/80 px-6 py-3 text-lg tracking-wide text-[#e8dfc8] transition hover:bg-[#3a2f1c] disabled:cursor-not-allowed disabled:opacity-40"
      >
        ▶ 시작
      </button>
    </div>
  );
}
