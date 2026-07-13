import { useNavigate } from 'react-router-dom';
import { hasSave } from '../utils/save';

export default function MainMenu() {
  const navigate = useNavigate();
  const canContinue = hasSave();

  return (
    <div className="flex h-full min-h-screen flex-col items-center justify-end bg-gradient-to-b from-[#1a140d] via-[#221a10] to-[#0f0d0a] pb-24">
      <h1 className="mb-16 text-5xl font-bold tracking-widest text-[#e8dfc8] drop-shadow-[0_2px_4px_rgba(0,0,0,0.6)]">
        무림의 끝
      </h1>

      <nav className="flex w-64 flex-col gap-4">
        <MenuButton label="게임 시작" onClick={() => navigate('/character/new')} />
        <MenuButton
          label="이어하기"
          disabled={!canContinue}
          onClick={() => navigate('/game')}
        />
        <MenuButton label="설정" onClick={() => {}} />
      </nav>
    </div>
  );
}

function MenuButton({
  label,
  onClick,
  disabled,
}: {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className="rounded-md border border-[#7a6a45] bg-[#2a2115]/80 px-6 py-3 text-lg tracking-wide text-[#e8dfc8] transition hover:bg-[#3a2f1c] disabled:cursor-not-allowed disabled:opacity-40"
    >
      ▶ {label}
    </button>
  );
}
