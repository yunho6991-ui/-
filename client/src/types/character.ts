export interface Character {
  name: string;
  level: number;
  rank: string;
  hp: number;
  maxHp: number;
  qi: number;
  maxQi: number;
  location: string;
}

export function createNewCharacter(name: string): Character {
  return {
    name,
    level: 1,
    rank: '삼류',
    hp: 100,
    maxHp: 100,
    qi: 50,
    maxQi: 50,
    location: '낙양',
  };
}
