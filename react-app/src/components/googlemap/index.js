
import React from 'react';
import GoogleMapReact from 'google-map-react';

import './map.css'


function Map () {
    
    // const AnyReactComponent = ({ text }) => <div>{text}</div>;
    
    const bayarea = {
        center: {
        lat: 37.8272,
        lng: -122.2913
        },
        zoom: 9
    };

    return (
      // Important! Always set the container height explicitly
      <div className='googleMap'>
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'AIzaSyBUDoNSCh1np3t8RCyZ-BZRkbjMFb_9Gyg' }}
          defaultCenter={bayarea.center}
          defaultZoom={bayarea.zoom}
        >
          {/* <AnyReactComponent
            lat={59.955413}
            lng={30.337844}
            text="My Marker"
          /> */}
        </GoogleMapReact>
      </div>
    );
  
}

export default Map;