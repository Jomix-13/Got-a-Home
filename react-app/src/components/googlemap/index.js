
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import GoogleMapReact from 'google-map-react';

import { fetchAllHomes } from '../../store/home';
import './map.css'

function Map () {

  
  const dispatch = useDispatch();
  const homes = useSelector((state) => state.homesReducer.homes);
  
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

    const Marker = ({ lat, lng }) => (
      <div className="mapMarker">
          <img src="https://i.imgur.com/B9Qsgm7.png" alt =""></img>
        </div>
      )
    return (
      <div className='googleMap'>
        <GoogleMapReact
          bootstrapURLKeys={{ key: process.env.REACT_APP_GOOGLE_KEY }}
          defaultCenter={bayarea.center}
          defaultZoom={bayarea.zoom}
        >
                {!!homes && homes?.map(home =>(
                    <Link key={home.id} to={`/homes/${home.id}`} lat={home.latitude} lng={home.longitude}>
                        <Marker/>
                    </Link>
                ))}
        </GoogleMapReact>
      </div>
    );
  
}

export default Map;