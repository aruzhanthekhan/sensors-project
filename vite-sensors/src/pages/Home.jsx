import '../App.css'
import 'leaflet/dist/leaflet.css'
import markericon from '/marker-icon.png'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUsers } from '@fortawesome/free-solid-svg-icons'
import { useState, useEffect } from "react"
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import { Icon } from 'leaflet'
import { Link } from 'react-router-dom'


function Map() {
  const [markers, setMarkers] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/')
      .then(res => res.json())
      .then(data => setMarkers(data)).catch(err =>
        console.log(err))
  }, []);

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
        <Marker position={[marker.latitude, marker.longitude]} icon={customIcon} key={marker.id}>
          <Popup>
            <Link to="/indicators" state={marker}>{marker.address}</Link>
          </Popup>
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
          <h1> <FontAwesomeIcon icon={faUsers} />   Команда</h1>
            <Link to="/team" className="button-team">Узнать больше о команде</Link>
          </div>
        </section>
      </main>
    </div>
  )
}