import { useEffect } from 'react'
import { NavLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import {fetchRentHomes} from '../../store/home'

import './buyrent.css'



function BuyHomes() {
    const homes = useSelector(state => state.homesReducer.homes)
    console.log(homes)
    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(fetchRentHomes())
    },[dispatch])

    return (
        <div className='allHomes'>
            {homes.map((home)=>(
                <NavLink key={home.id} to={`/homes/${home.id}`}>
                <div className='oneHome' >
                    <div>{home.price} $</div>
                    <img src={home.images[0]} alt=''></img>
                    <div>{home.stAdress}</div>
                    <div>{home.city},{home.state}.{home.zipCode}</div>
                    <div>{home.lotSize} sq ft</div>
                    <div>{home.beds} Bedrooms, {home.bath} Bathrooms</div>
                    <div>{home.status}</div>
                </div>
                </NavLink>
            ))}
        </div>
    )
}

export default BuyHomes