import { useState } from 'react'
import './App.css'
import './Team'

const mapSection = function() {
  return (
    <div className='map-section' id="map">
    </div>
  )
}

function App() {
  return (
    <div className="App">
      <navbar>
        <ul>
          <li><a href="" target="_blank">Главная страница</a></li>
          <li><a href="" target="_blank">Войти/Зарегистрироваться</a></li>
        </ul>
      </navbar>
      <main>
        <section>
          <div className="map">
            Тут будет карта
          </div>
        </section>
        <section className='general-info'>
          <div className='about-section'>
            <h1>О проекте</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non rutrum justo, at tincidunt libero. Duis porta elit ac ornare commodo. Nunc et risus a sapien condimentum vehicula non id ligula. Vivamus sollicitudin nibh eu tellus scelerisque tincidunt. Nam vestibulum enim ac tempus volutpat.</p>
            <p>Phasellus blandit, purus nec pretium sodales, elit risus rutrum metus, vitae tempor ipsum eros vitae justo. Aenean feugiat ipsum ut nisi ultricies, id porttitor nibh luctus. Nunc iaculis varius sodales. Suspendisse id porta tellus. Integer efficitur faucibus risus, in vestibulum dolor.</p>
            <p>Cras et augue vel nunc blandit efficitur at congue magna. Vivamus ac augue nec odio viverra auctor. Nam porttitor, nibh vel porta feugiat, ipsum lacus placerat nibh, sit amet lobortis justo sapien facilisis lacus. Curabitur leo lacus, malesuada ac luctus in, tincidunt eget mi. Vivamus facilisis tempor massa. Nullam pulvinar risus id arcu dictum elementum. </p>

          </div>
          <div className='team-section'>
            <h1>Команда</h1>
            <button>Узнать больше о команде</button>
          </div>
        </section>
      </main>
      <footer>
        2023
      </footer>
    </div>
  )
}

export default App
