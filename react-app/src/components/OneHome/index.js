import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import {fetchOneHome} from '../../store/home'
import homesReducer from "../../store/home"

import './onehome.css'


const OneHome = () => {
    const {id} = useParams()
    const dispatch = useDispatch()

    const home = useSelector(state => state.homesReducer.home)
    console.log('cccccccc',home)
    console.log(id)

    useEffect(()=>{
        dispatch(fetchOneHome(id))
    },[dispatch,id])

    return (
        <div className='all'>
            <div className='photos'>
                {home?.images?.map((image)=>(
                    <img src={image}></img>
                ))}
            </div>
                <div>
                    <div className='price'>{home.price} $</div>
                </div>
                <div>
                    <div className='status'>{home.status}</div>
                </div>
                <div className='descriptions'>
                    <div>
                        <div className='adress'>{home.stAdress}</div>
                    </div>
                    <div>
                        <div className='city'>{home.city},{home.state}.{home.zipCode}</div>
                    </div>
                    <div>
                        <div className='lotSize'>Lot Size : {home.lotSize} sq ft</div>
                    </div>
                    <div>
                        <div className='BB'>{home.beds} Bedrooms, {home.bath} Bathrooms</div>
                    </div>
                </div>
            <div className='qupa'>
                <div>
                    Questions form
                </div>
                <div>
                {home?.questions?.map((questions)=>(
                    <div className='qu'>{questions}</div>
                    ))}
                </div>
            </div>
        </div>

    )
}

export default OneHome