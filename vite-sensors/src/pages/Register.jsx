import '../App.css'
import { Link } from 'react-router-dom'
import { useState } from "react"

export function Register() {
    const [lastname, setLastname] = useState();
    const [firstname, setFirstname] = useState();
    const [fathersname, setFathersname] = useState("");
    const [phone, setPhone] = useState();
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('http://localhost:5000/register', {
            method: 'POST',
            body: JSON.stringify({
                firstname: firstname,
                lastname: lastname,
                fathersname: fathersname,
                phone: phone,
                email: email,
                password: password
            }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            },
        })
            .then((res) => res.json())
            .catch((err) => {
                console.log(err.message);
            });
            setLastname("");
            setFirstname("");
            setFathersname("");
            setEmail("");
            setPhone("");
            setPassword("");
    };

    return (
        <div>
            <div className="register-container">
                <h1>Зарегистрироваться</h1>
                <p>Строки отмеченные * обязательны для заполнения</p>
                <form onSubmit={handleSubmit}>
                    <label htmlFor="lastname">Фамилия *</label>
                    <input value={lastname}
                        onChange={(e) => setLastname(e.target.value)}
                        type="text" id="lastname" name="lastname" required />

                    <label htmlFor="firstname">Имя *</label>
                    <input value={firstname}
                        onChange={(e) => setFirstname(e.target.value)}
                        type="text" id="firstname" name="firstname" required />

                    <label htmlFor="fathersname">Отчество</label>
                    <input value={fathersname}
                        onChange={(e) => setFathersname(e.target.value)}
                        type="text" id="fathersname" name="fathersname" />

                    <label htmlFor="phone">Номер телефона</label>
                    <input value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        type="tel" id="phone" name="phone" pattern="[0-9]{3}[0-9]{3}[0-9]{4}" />

                    <label htmlFor="email">Адрес электронной почты *</label>
                    <input value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        type="email" id="email" name="email" required />

                    <label htmlFor="password">Придумайте пароль *</label>
                    <input value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        type="password" id="password" name="password" required />

                    <button type="submit" className='registerbtn'>Зарегистрироваться</button>
                </form>
            </div>
            <div className="alternative-container">
                <p>Уже есть аккаунт? <Link to="/login">Нажмите сюда, чтобы войти</Link>.</p>
            </div>
        </div>
    )
}