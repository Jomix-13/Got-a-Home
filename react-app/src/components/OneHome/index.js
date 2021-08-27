import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { NavLink, Redirect, useHistory, useParams } from "react-router-dom"
import {fetchOneHome,fetchDeleteHome} from '../../store/home'
import homesReducer from "../../store/home"

import './onehome.css'


const OneHome = () => {
    const {id} = useParams()
    const dispatch = useDispatch()
    const history = useHistory()

    const home = useSelector(state => state.homesReducer.home)
    const user = useSelector(state => state.session.user)

    useEffect(()=>{
        dispatch(fetchOneHome(id))
    },[dispatch,id])
    
    const deleteHome = async(e,id)=>{
        e.preventDefault()
        await dispatch(fetchDeleteHome(id)).then(history.push('/'))
        
    }
    return (
        <div className='all'>
            {user?.id === home?.userId ?
            <div>
                <NavLink to={`/update/${home.id}`} alt="">
                    <button>
                        Modify
                    </button>
                </NavLink>
                <button onClick={e=>deleteHome(e,home.id)}>Sold</button>
            </div>
             : null }
            <div className='photos'>
                {home?.images?.map((image)=>(
                    <img key={image.id} src={image}></img>
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
                {home?.questions?.map((question)=>(
                    <div key={question.id} className='qu'>{question}</div>
                    ))}
                </div>
            </div>
        </div>

    )
}

export default OneHome