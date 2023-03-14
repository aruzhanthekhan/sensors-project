import './App'

function Register() {
    <div>
        <p>Строки отмеченные * обязательны для заполнения</p>
        <form>
            <label for="last-name">Фамилия *<input type="text" id="last-name" name="last-name" required></input></label>
            <label for="first-name">Имя *<input type="text" id="first-name" name="first-name" required></input></label>
            <label for="fathers-name">Отчество<input type="text" id="fathers-name" name="fathers-name"></input></label>
            <label for="date-of-birth">Дата рождения *<input type="date" id="date-of-birth" name="date-of-birth" required></input></label>
            <label for="email">Адрес электронной почты *<input type="email" id="email" name="email" required></input></label>
            <label for="password">Придумайте пароль *<input type="password" id="password" name="password" required></input></label>
        </form>
        <button>Зарегистрироваться</button>
    </div>
}