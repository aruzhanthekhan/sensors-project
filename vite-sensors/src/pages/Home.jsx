import '../App.css';
import { Link } from 'react-router-dom';
import { GoogleMap, useLoadScript, MarkerF } from "@react-google-maps/api";

function Map() {
  const { isLoaded } = useLoadScript({
    //googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_API,
    googleMapsApiKey: "AIzaSyBRhURGMnFFB5ziAB8a5e68qyPuigsBnhk",
  });

  if (!isLoaded) return (<div>Loading...</div>);
  return (
    <GoogleMap zoom={13} center={{ lat: 51.1410139, lng: 71.4409839 }} mapContainerClassName="map"></GoogleMap>
  )
}

export function Home() {
  return (
    <div className="App">
      <main>
        <section>
          <div className="map">
            <Map />
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
            <Link to="/team" target="_blank" className="button-team">Узнать больше о команде</Link>
            <br />
            <Link to="/indicators" target="_blank" className="button-team">Показатели</Link> 
          </div>
        </section>
      </main>
    </div>
  )
}