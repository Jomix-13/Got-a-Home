import { useEffect } from 'react'
import { NavLink } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import {fetchAllHomes} from '../../store/home'
import Map from '../googlemap'
import CurrencyFormat from 'react-currency-format';


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
                        <div className='ho'>
                        <div className='pri'>
                        <CurrencyFormat value={home.price} displayType={'text'} thousandSeparator={true} prefix={'$'} />
                            {/* $ {home.price} */}
                            </div>
                        <img src={home.images[0]} alt=''></img>
                        <div className='adressh'>{home.stAddress},</div>
                        <div className='cityh'>{home.city}, {home.state}  {home.zipCode}</div>
                        <div className='lotSizeh'>{home.lotSize} sq ft</div>
                        <div className='BBh'>{home.beds} Bedrooms, {home.bath} Bathrooms</div>
                        <div className='statush'>{home.status}</div>
                        </div>
                    </div>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default HomePage