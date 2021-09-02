
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import GoogleMapReact from 'google-map-react';
import Geocode from "react-geocode";

import { fetchAllHomes } from '../../store/home';
import './map.css'



function Map () {

  
  const dispatch = useDispatch();
  const homes = useSelector((state) => state.homesReducer.homes);
  
  Geocode.setLanguage("en");
  useEffect(() => {
    dispatch(fetchAllHomes());
  }, [dispatch]);
  
  const bayarea = {
    center: {
      lat: 37.8272,
      lng: -122.2913
    },
    zoom: 9
  };
  
  
//  const code = (add, city, state, zip) => Geocode.fromAddress(add, city, state, zip).then(
//     (response) => {
//       const { lat, lng } = response.results[0].geometry.location;
//       return { lat, lng }
//     },
//     (error) => {
//       console.error(error);
//     }
//     );
    
    const Marker = ({ lat, lng }) => (
      <div className="mapMarker">
          <img src="https://i.imgur.com/B9Qsgm7.png" alt =""></img>
        </div>
      )
    // const Marker = ({ add, city, state, zip }) => (
    //   <div className="mapMarker">
    //     <img src="https://i.imgur.com/B9Qsgm7.png" alt =""></img>
    //   </div>
    // )

    return (
      // Important! Always set the container height explicitly
      <div className='googleMap'>
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'AIzaSyBUDoNSCh1np3t8RCyZ-BZRkbjMFb_9Gyg' }}
          defaultCenter={bayarea.center}
          defaultZoom={bayarea.zoom}
        >
                {!!homes && homes?.map(home =>(
                    <Link key={home.id} to={`/homes/${home.id}`} lat={home.latitude} lng={home.longitude}>
                        <Marker/>
                    </Link>
                ))}
                {/* {!!homes && homes?.map(home =>(
                    <Link key={home.id} to={`/homes/${home.id}`} lat={code(home.stAddress, home.city, home.state, home.zipCode).lat} lng={code(home.stAddress, home.city, home.state, home.zipCode).lng} >
                        <Marker/>
                    </Link>
                ))} */}
                {/* {!!homes && homes?.map(home =>(
                    <Link key={home.id} to={`/homes/${home.id}`} 
                    add={home.stAddress} 
                    city={home.city}
                    state={home.state}
                    zip={home.zipCode}
                    >
                        <Marker/>
                    </Link>
                ))} */}
        </GoogleMapReact>
      </div>
    );
  
}

export default Map;