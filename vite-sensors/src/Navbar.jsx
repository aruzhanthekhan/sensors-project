import './App.css'
import { Link } from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHouse, faRightToBracket, faUserPlus } from '@fortawesome/free-solid-svg-icons'


export function Navbar(props) {

  function logMeOut() {
    fetch('http://localhost:5000/logout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(data => {
        props.token();
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

        <li className="navbar-element"><Link to="/login"><FontAwesomeIcon icon={faRightToBracket} />   Войти</Link></li>
        <li className="navbar-element"><Link to="/register"><FontAwesomeIcon icon={faUserPlus} />   Зарегистрироваться</Link></li>
        
        <li className="navbar-element"><Link to="/login"><FontAwesomeIcon icon={faRightToBracket} />   Выйти</Link></li> 
      </ul>
    </nav>
  )
}