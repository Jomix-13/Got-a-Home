import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import homesReducer from '../../store/home'
import {fetchAllHomes} from '../../store/home'

import './homepage.css'



function HomePage() {
    const homes = useSelector(state => state.homesReducer.homes)
    console.log('CCCCCCCCCCC',homes)
    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(fetchAllHomes())
    },[dispatch])

    return (
        <div className='allHomes'>
            {homes.map((home)=>(
                <div className='oneHome' key={home.id}>
                    <div>{home.price} $</div>
                    <div>{home.image}</div>
                    <div>{home.stAdress}</div>
                    <div>{home.city},{home.state}.{home.zipCode}</div>
                    <div>{home.lotSize} sq ft</div>
                    <div>Bedrooms:{home.beds}   Bathrooms:{home.bath}</div>
                    <div>{home.status}</div>
                </div>
            ))}
        </div>
    )
}

export default HomePage