import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { Redirect, useHistory, useParams } from "react-router-dom"
import {fetchOneHome,fetchDeleteHome} from '../../store/home'
import homesReducer from "../../store/home"

import './onehome.css'


const OneHome = () => {
    const {id} = useParams()
    const dispatch = useDispatch()
    const history = useHistory()

    const home = useSelector(state => state.homesReducer.home)
    const user = useSelector(state => state.session.user)
    console.log('cccccccc',home)
    console.log(id)

    useEffect(()=>{
        dispatch(fetchOneHome(id))
    },[dispatch,id])

    const deleteHome = (e,id)=>{
        e.preventDefault()
        dispatch(fetchDeleteHome(id))
        // history.push('/')
    }
    return (
        <div className='all'>
            {user?.id === home?.userId ?
            <div>
                <button>Modify</button>
                <button onClick={e=>deleteHome(e,home.id)}>Sold</button>
            </div>
             : null }
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
                        <div className='adress'>{home.stAddress}</div>
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