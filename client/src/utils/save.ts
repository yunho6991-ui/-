import type { Character } from '../types/character';

const SAVE_KEY = 'muhrim-save';

export function saveCharacter(character: Character): void {
  localStorage.setItem(SAVE_KEY, JSON.stringify(character));
}

export function loadCharacter(): Character | null {
  const raw = localStorage.getItem(SAVE_KEY);
  if (!raw) return null;
  try {
    return JSON.parse(raw) as Character;
  } catch {
    return null;
  }
}

export function hasSave(): boolean {
  return localStorage.getItem(SAVE_KEY) !== null;
}

export function clearSave(): void {
  localStorage.removeItem(SAVE_KEY);
}
