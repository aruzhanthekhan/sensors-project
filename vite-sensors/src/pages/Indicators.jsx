import '../App.css'

export function Indicators() {
    return (
        <div className="indicator-container">
            <div>
                <p className='indicator-info'>Показания счетчика горячей воды: <span>sample text</span></p>
                <p className='indicator-info'>Показания счетчика холодной воды: <span>sample text</span></p>
                <p className='indicator-info'>Показания счетчика электроэнергии: <span>sample text</span></p>
            </div>
            <div>
                <p className='indicator-info'>Адрес: <span>sample text</span></p>
                <p className='indicator-info'>Подъезд: <span>sample text</span></p>
                <p className='indicator-info'>Номер ОСИ: <span>sample text</span></p>
                <p className='indicator-info'>Имя: <span>sample text</span></p>
                <p className='indicator-info'>Фамилия: <span>sample text</span></p>
            </div>
        </div>
    )
} 