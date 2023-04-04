import '../App.css'
import { Link } from 'react-router-dom'

export function Register() {
    return (
        <div>
            <div className="register-container">
                <h1>Зарегистрироваться</h1>
                <p>Строки отмеченные * обязательны для заполнения</p>
                <form>
                    <label htmlFor="last-name">Фамилия *</label><input type="text" id="last-name" name="last-name" required />
                    <label htmlFor="first-name">Имя *</label><input type="text" id="first-name" name="first-name" required />
                    <label htmlFor="fathers-name">Отчество</label><input type="text" id="fathers-name" name="fathers-name" />
                    <label htmlFor="phone">Номер телефона</label><input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" /> 
                    <label htmlFor="email">Адрес электронной почты *</label><input type="email" id="email" name="email" required />
                    <label htmlFor="password">Придумайте пароль *</label><input type="password" id="password" name="password" required />
                    <button type="submit" className='registerbtn'>Зарегистрироваться</button>
                </form>
            </div>
            <div className="alternative-container">
                <p>Уже есть аккаунт? <Link to="/login">Нажмите сюда, чтобы войти</Link>.</p>
            </div>
        </div>
    )
}