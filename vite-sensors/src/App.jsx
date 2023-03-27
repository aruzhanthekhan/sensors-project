import { Route, Routes } from 'react-router-dom'
import { Navbar } from "./Navbar"
import { Home } from "./pages/Home"
import { Register } from "./pages/Register"
import { Team } from "./pages/Team"
import { Login } from "./pages/Login"
import { Indicators } from './pages/Indicators'
import { PersonalPage } from './pages/PersonalPage'

export default function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/team" element={<Team />} />
        <Route path="/indicators" element={<Indicators />} />
        <Route path="/personalpage" element={<PersonalPage />} />
      </Routes>
    </div>
  )
}