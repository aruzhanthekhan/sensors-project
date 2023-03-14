import {Link} from 'react-router-dom'
export function Navbar() {
    return (
      <nav>
        <ul>
          <li><Link to="/">Главная страница</Link></li>
          <li><Link to="/login" target="_blank">Войти</Link></li>
          <li><Link to="/register" target="_blank">Зарегистрироваться</Link></li>
        </ul>
      </nav>
    )
  }