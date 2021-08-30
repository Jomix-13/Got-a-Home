import { useEffect } from 'react'
import { NavLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import homesReducer from '../../store/home'
import {fetchAllHomes} from '../../store/home'
import Map from '../googlemap'

import './homepage.css'



function HomePage() {
    const homes = useSelector(state => state.homesReducer.homes)
    console.log(homes)
    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(fetchAllHomes())
    },[dispatch])

    return (
        <div className='homepage'>
            <div className='map'>
                <Map></Map>
            </div>
            <div className='allHomes'>
                {homes.map((home)=>(
                    <NavLink key={home.id} to={`/homes/${home.id}`}>
                    <div className='oneHome' >
                        <div>{home.price} $</div>
                        <img src={home.images[0]}></img>
                        <div>{home.stAdress}</div>
                        <div>{home.city},{home.state}.{home.zipCode}</div>
                        <div>{home.lotSize} sq ft</div>
                        <div>{home.beds} Bedrooms, {home.bath} Bathrooms</div>
                        <div>{home.status}</div>
                    </div>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default HomePage