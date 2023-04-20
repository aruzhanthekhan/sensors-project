import '../App.css'
import { useState } from 'react'
import { Link } from 'react-router-dom'

export function Login(props) {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('http://localhost:5000/token', {
            method: 'POST',
            body: JSON.stringify({
                email: email,
                password: password
            }),
            headers: {
                'Content-type': 'application/json',
            },
        })
            .then((res) => res.json())
            .then(data => {
                props.setToken(data.access_token);
            })
            .catch((err) => {
                console.log(err.message);
            });
        setEmail("");
        setPassword("");
    };

    return (
        <div>
            <div className="register-container">
                <h1>Войти</h1>
                <form onSubmit={handleSubmit}>
                    <label htmlFor="email">Адрес электронной почты</label>
                    <input value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        type="email" id="email" name="email" required></input>

                    <label htmlFor="password">Пароль</label>
                    <input value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        type="password" id="password" name="password" required></input>

                    <button type="submit" className='registerbtn'>Войти</button>
                </form>
            </div>
            <div className="alternative-container">
                <p>Ещё не создали аккаунт? <Link to="/register">Нажмите сюда, чтобы зарегистрироваться</Link>.</p>
            </div>
        </div>
    )
} 