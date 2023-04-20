import '../App.css'
import { useLocation } from 'react-router-dom';

export function Indicators() {
    const location = useLocation();

    return (
        <div className="indicator-container">
            <h3>{location.state.address}</h3>
            <div>
                <p className='indicator-info'>Давление горячей воды: <span>{location.state.hot_water_pressure}</span></p>
                <p className='indicator-info'>Давление холодной воды: <span>{location.state.cold_water_pressure}</span></p>
                <p className='indicator-info'>Показания счетчика горячей воды: <span>{location.state.hot_water_consumption}</span></p>
                <p className='indicator-info'>Показания счетчика холодной воды: <span>{location.state.cold_water_consumption}</span></p>
                <p className='indicator-info'>Входное напряжение: <span>{location.state.input_voltage}</span></p>
                <p className='indicator-info'>Температура прямого потока: <span>{location.state.direct_flow_temperature}</span></p>
                <p className='indicator-info'>Температура обратного потока: <span>{location.state.return_flow_temperature}</span></p>
                <p className='indicator-info'>Сила входного тока: <span>{location.state.input_current_strength}</span></p>
            </div>
            <div>
                <p className='indicator-info'>Адрес: <span>{location.state.address}</span></p>
                {/* <p className='indicator-info'>Номер ОСИ: <span>N/A</span></p>
                <p className='indicator-info'>Имя председателя ОСИ: <span>sample text</span></p>
                <p className='indicator-info'>Фамилия председателя ОСИ: <span>sample text</span></p> */}
            </div>
        </div>
    )
} 