import '../App.css'
export function Team() {
    return (
            <main>
                <h1 className="centered-header">Команда</h1>
                <div className='team-container'>
                    <div className='person-container'>
                        <img src="/a_n.jpg" className='team-member-picture'></img>
                        <div>
                            <h2 className='team-member-description'>Нефтисов Александр</h2>
                            <p className='team-member-description'>Руководитель НИЦ Industry 4.0 AITU</p>
                        </div>
                    </div>
                    <div className='person-container'>
                        <img src="/s_a.jpg" className='team-member-picture'></img>
                        <div>
                            <h2 className='team-member-description'>Саринова Асия Жумабаевна</h2>
                            <p className='team-member-description'>Доктор PhD, кандидат технических наук</p>
                        </div>
                    </div>
                    </div>
                    <div className='team-container'>
                    <div className='person-container'>
                        <img src="/k_l.jpg" className='team-member-picture'></img>
                        <div>
                            <h2 className='team-member-description'>Кириченко Лалита Николавена</h2>
                            <p className='team-member-description'>Магистр технических наук</p>
                        </div>
                    </div>
                    <div className='person-container'>
                        <img src="/k_i.jpg" className='team-member-picture'></img>
                        <div>
                            <h2 className='team-member-description'>Казамбаев Ильяс Маратулы</h2>
                            <p className='team-member-description'>Магистр технических наук</p>
                        </div>
                    </div>
                </div>
            </main>
    )
}