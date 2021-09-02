import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { NavLink, Redirect, useHistory } from "react-router-dom"
import Errors from '../errors'


import { fetchEditHome, fetchOneHome } from "../../store/home"

const STATES =[
    "--",
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]

const options = ["--","For Sale","For Rent","Pending Sale"]


const EditHomeForm = ({setShowModal}) => {

    const home = useSelector(state => state.homesReducer.home)
    

    const [price, setPrice] = useState(home.price)
    const [stAddress, setStAddress] = useState(home.stAddress)
    const [city, setCity] = useState(home?.city)
    const [state, setState] = useState(home?.state)
    const [zipCode, setZipCode] = useState(home?.zipCode)
    const [latitude, setLatitude] = useState(home?.latitude)
    const [longitude, setLongitude] = useState(home?.longitude)
    const [lotSize, setLotSize] = useState(home?.lotSize)
    const [beds, setBeds] = useState(home?.beds)
    const [bath, setBath] = useState(home?.bath)
    const [status, setStatus] = useState(home?.status)
    const [image, setImage] = useState(home?.images)

    const dispatch = useDispatch()
    const history = useHistory()
    const id = home.id

    useEffect(()=>{
        dispatch(fetchOneHome(id))
        // dispatch(fetchAllQuestions())
    },[dispatch,id])
    
    const onSubmit = async(e) => {
        e.preventDefault()
        const payload = {
            price,
            stAddress,
            city,
            state,
            zipCode,
            latitude,
            longitude,
            lotSize,
            beds,
            bath,
            status,
            image,
        }
        // const success = await dispatch(fetchEditHome(payload,home.id))
        // if (success){
            //     history.push(`/homes/${home.id}`)
            // }
        // dispatch(fetchOneHome(home.id))
        const success = await dispatch(fetchEditHome(payload,home.id))

        if (success){
            // history.push(`/homes/${home.id}`)
            setShowModal(false);
        }
        // await fetchOneHome(home.id)
    }

    return (
        <div className='form-div'>
        <form onSubmit={onSubmit}>
            <div className='form-content'>
            <div className='form-all-inputs-container'>
            <div className='form-h3-container'>
                {/* <h3 className='form-h3'>Login</h3> */}
            </div>
            <div >
                <Errors></Errors>
            <div className='form-input-container'>
                <label className='form-label' >Price</label>
                <input
                    className='form-input'type='text'
                    value={price}
                    onChange={e=>setPrice(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >Street Address</label>
                <input
                    className='form-input'
                    type='text'
                    value={stAddress}
                    onChange={e=>setStAddress(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >City</label>
                <input
                    className='form-input'
                    type='text'
                    value={city}
                    onChange={e=>setCity(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >State</label>
                <select
                    className='form-input form-select'
                    value={state}
                    onChange={(e) => setState(e.target.value)}
                    >
                    {STATES.map(state => (
                        <option
                        key={state}
                        >
                        {state}
                    </option>
                    ))}
                </select>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >Zip Code</label>
                <input
                    className='form-input'
                    type='number'
                    value={zipCode}
                    onChange={e=>setZipCode(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >Latitude</label>
                <input
                    className='form-input'
                    type='number'
                    value={latitude}
                    onChange={e=>setLatitude(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >Longitude</label>
                <input
                    className='form-input'
                    type='number'
                    value={longitude}
                    onChange={e=>setLongitude(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >No. Beds</label>
                <input
                    className='form-input'
                    type='number'
                    value={beds}
                    onChange={e=>setBeds(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >No. Bath</label>
                <input
                    className='form-input'
                    type='number'
                    value={bath}
                    onChange={e=>setBath(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >Lot Size</label>
                <input
                    className='form-input'
                    type='number'
                    value={lotSize}
                    onChange={e=>setLotSize(e.target.value)}
                >
                </input>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >Status</label>
                <select
                    className='form-input form-select'
                    value={status}
                    onChange={(e) => setStatus(e.target.value)}
                    >
                    {options.map(op => (
                        <option 
                        key={op}
                        >
                        {op}
                    </option>
                    ))}
                </select>
            </div>
            <div className='form-input-container'>
                <label className='form-label' >Image</label>
                <input
                    className='form-input'
                    type='text'
                    value={image}
                    onChange={e=>setImage(e.target.value)}
                >
                </input>
            </div>
            <button className='button' type="submit">Submit</button>
            {/* <NavLink to={`/homes/${home.id}`}> */}
            <button className='button' onClick={()=> {setShowModal(false)}} >Cancel</button>
            {/* </NavLink> */}
            </div>
        </div>
        </div>
        </form>
        </div>
    )
}

export default EditHomeForm