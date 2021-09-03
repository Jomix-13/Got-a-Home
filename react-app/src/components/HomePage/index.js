import { useEffect } from 'react'
import { NavLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import {fetchAllHomes} from '../../store/home'
import Map from '../googlemap'

import './homepage.css'



function HomePage() {
    const homes = useSelector(state => state.homesReducer.homes)
    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(fetchAllHomes())
    },[dispatch])

    return (
        <div className='homepage'>
            <div className='map'>
                <Map></Map>
            </div>
            <div className='aallHomes'>
                {homes.map((home)=>(
                    <NavLink key={home.id} to={`/homes/${home.id}`}>
                    <div className='oneHome' >
                        <div className='pri'>$ {home.price}</div>
                        <img src={home.images[0]} alt=''></img>
                        <div className='adress'>{home.stAdress}</div>
                        <div className='city'>{home.city},{home.state}.{home.zipCode}</div>
                        <div className='lotSize'>{home.lotSize} sq ft</div>
                        <div className='BB'>{home.beds} Bedrooms, {home.bath} Bathrooms</div>
                        <div className=''>{home.status}</div>
                    </div>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default HomePage