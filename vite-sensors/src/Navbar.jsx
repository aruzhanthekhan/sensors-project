import './App.css'
import { Link } from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHouse, faRightToBracket, faUserPlus } from '@fortawesome/free-solid-svg-icons'


export function Navbar() {
  return (
    <nav className='navigation-bar'>
      <ul>
        <li className="navbar-element"><Link to="/"><FontAwesomeIcon icon={faHouse} />   Главная страница</Link></li>
        <li className="navbar-element"><Link to="/login"><FontAwesomeIcon icon={faRightToBracket} />   Войти</Link></li>
        <li className="navbar-element"><Link to="/register"><FontAwesomeIcon icon={faUserPlus} />   Зарегистрироваться</Link></li>
      </ul>
    </nav>
  )
}