import '../App.css'
import 'leaflet/dist/leaflet.css'
import markericon from '/marker-icon.png'

import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import { Icon } from 'leaflet'
import { Link } from 'react-router-dom'

function Map() {
  const markers = [
    {
      index: 1,
      geocode: [51.1611436, 71.4592416],
      popup: 'улица Ахмета Жубанова, 10'
    },
    {
      index: 2,
      geocode: [51.1117596, 71.4261293],
      popup: 'улица Туркестан, 8/1'
    }
  ]

  const customIcon = new Icon({
    iconUrl: markericon,
    iconSize: [38, 38]
  })

  return (
    <MapContainer center={{ lat: 51.1410139, lng: 71.4409839 }} zoom={13}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url='https://tile.openstreetmap.org/{z}/{x}/{y}.png' />
      {markers.map((marker) => (
        <Marker position={marker.geocode} icon={customIcon} key={marker.index}>
          <Popup>{marker.popup}</Popup>
        </Marker>
      ))}
    </MapContainer>
  )
}

export function Home() {
  return (
    <div className="App">
      <main>
        <section>
          <Map />
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
            <Link to="/team" target="_blank" className="button-team">Узнать больше о команде</Link>
            <br />
            <Link to="/indicators" target="_blank" className="button-team">Показатели</Link>
          </div>
        </section>
      </main>
    </div>
  )
}