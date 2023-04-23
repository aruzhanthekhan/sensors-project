import { Route, Routes, Link } from 'react-router-dom'
import { Home } from "./pages/Home"
import { Register } from "./pages/Register"
import { Team } from "./pages/Team"
import { Login } from "./pages/Login"
import { Indicators } from './pages/Indicators'
import { Profile } from './pages/Profile'
import { useToken } from './useToken'
import './App.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHouse, faRightToBracket, faUserPlus } from '@fortawesome/free-solid-svg-icons'

export default function App() {

  const { token, removeToken, setToken } = useToken();

  return (
    <div>
      <Navbar token={token} removeToken={removeToken} />
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

function Navbar({token, removeToken}) {

  function logMeOut() {
    fetch('http://localhost:5000/logout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(data => {
        removeToken.token();
      })
      .catch(error => {
        console.error(error);
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
        }
      });
  }


  return (
    <nav className='navigation-bar'>
      <ul>
        <li className="navbar-element"><Link to="/"><FontAwesomeIcon icon={faHouse} />   Главная страница</Link></li>
        {!token ? (
          <>
        <li className="navbar-element"><Link to="/login"><FontAwesomeIcon icon={faRightToBracket} />   Войти</Link></li>
        <li className="navbar-element"><Link to="/register"><FontAwesomeIcon icon={faUserPlus} />   Зарегистрироваться</Link></li>
        </>):
        <>
        <li className="navbar-element"><Link to="/profile"><FontAwesomeIcon icon={faRightToBracket} />   Мой кабинет</Link></li>
        <li className="navbar-element"><Link to="/"><FontAwesomeIcon icon={faRightToBracket} />   Выйти</Link></li>
        </> 
        }
        </ul>
    </nav>
  )
}