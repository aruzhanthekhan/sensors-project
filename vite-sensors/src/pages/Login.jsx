import '../App.css'
import { Link } from 'react-router-dom'

export function Login() {
    return (
        <div>
            <div className="register-container">
                <h1>Войти</h1>
                <form>
                    <label htmlFor="email">Адрес электронной почты<input type="email" id="email" name="email" required></input></label>
                    <label htmlFor="password">Пароль<input type="password" id="password" name="password" required></input></label>
                    <button type="submit" className='registerbtn'>Войти</button>
                </form>
            </div>
            <div className="alternative-container">
                <p>Ещё не создали аккаунт? <Link to="/register">Нажмите сюда, чтобы зарегистрироваться</Link>.</p>
            </div>
        </div>
    )
} 