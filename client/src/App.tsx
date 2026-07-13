import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainMenu from './pages/MainMenu';
import CharacterCreate from './pages/CharacterCreate';
import Luoyang from './pages/Luoyang';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainMenu />} />
        <Route path="/character/new" element={<CharacterCreate />} />
        <Route path="/game" element={<Luoyang />} />
      </Routes>
    </BrowserRouter>
  );
}
