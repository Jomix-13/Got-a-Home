
import { useDispatch, useSelector } from 'react-redux'
import './splashpage.css'
import { fetch20Homes } from '../../store/home'
import { useEffect } from 'react'
import { useHistory } from 'react-router-dom'

import './splashpage.css'
const SplashPage = () =>{

    const homes20 = useSelector(state => state.homesReducer.homes)

    console.log(homes20)

    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(fetch20Homes())
    },[dispatch])

    return (
        <div className='All'>
            <div className='i'>
                {/* <img src='https://i.imgur.com/s44tGsV.png'></img> */}
                <img src='https://i.imgur.com/Xc4j024.png'></img>
                {/* <img src='https://i.imgur.com/vZ0TUsl.png'></img> */}
            </div>
            {/* <div className='container'>
                {homes20?.map((home)=>(
                    <div className='each' key={home.id}>
                        <img src={home.images[0]}/>
                    </div>
                ))}
            </div> */}
            <div className="hwrap2">
                <div className="hmove2">
                <div className="hitem2">
                    <div>
                        THE WAY YOU FIND YOUR HOME.
                    </div>
                    {/* <img src='https://i.imgur.com/Xc4j024.png'/> */}
                </div>
                </div>
            </div>
        </div>
    )
}

export default SplashPage