import { Route, Routes, BrowserRouter } from 'react-router-dom'
import { Navbar } from "./Navbar"
import { Home } from "./pages/Home"
import { Register } from "./pages/Register"
import { Team } from "./pages/Team"
import { Login } from "./pages/Login"
import { Indicators } from './pages/Indicators'
import { Profile } from './pages/Profile'
import { useToken } from './useToken'

export default function App() {

  const { token, removeToken, setToken } = useToken();

  return (
    <div>
      <Navbar token={removeToken} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login setToken={setToken} />} />
        <Route path="/team" element={<Team />} />
        <Route path="/indicators" element={<Indicators />} />
        <Route path="/profile" element={<Profile token={token} setToken={setToken} />} />
        <Route path="*" element={<Home />} />
      </Routes>
    </div>
  )
}