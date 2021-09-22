import { useState } from "react"
import { useDispatch } from "react-redux"
import { NavLink, useHistory } from "react-router-dom"
import Errors from '../errors'
import './AddHome_form.css'
import Geocode from "react-geocode";



import { fetchAddHome } from "../../store/home"

Geocode.setApiKey("AIzaSyAgdlEtqn59K7XpcMGDwsM1Ub8IlhtSruw");


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

const options = ["--","For Sale","For Rent","Sale Pending"]


const AddHomeForm = () => {    

    const [price, setPrice] = useState('')
    const [stAddress, setStAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipCode, setZipCode] = useState('')
    // const [latitude, setLatitude] = useState('')
    // const [longitude, setLongitude] = useState('')
    const [lotSize, setLotSize] = useState(STATES[0])
    const [beds, setBeds] = useState('')
    const [bath, setBath] = useState('')
    const [status, setStatus] = useState(options[0])
    const [image, setImage] = useState('')
    const [homeErrors, setHomeErrors] = useState(false);


    const dispatch = useDispatch()
    const history = useHistory()

    const onSubmit = async(e) => {
        e.preventDefault()
        let address= (stAddress + ' ' + city + ' '  + state + ' ' + zipCode)
        let res = await Geocode.fromAddress(address);
        console.log(res)
        console.log(res.results[0].geometry.location)
        const { lat: latitude, lng: longitude } = res.results[0].geometry.location;

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
        const success = await dispatch(fetchAddHome(payload))
        if (success){
            history.push('/homes')
        }else{
            setHomeErrors(true)
        }
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
                {homeErrors ? <Errors></Errors> : null }
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
            {/* <div className='form-input-container'>
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
            </div> */}
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
                <label className='form-label' >Image URL</label>
                <input
                    className='form-input'
                    type='text'
                    value={image}
                    onChange={e=>setImage(e.target.value)}
                >
                </input>
            </div>
            <button className='button' type="submit">Submit</button>
            <NavLink to={`/homes`}>
                <button className='button' >Cancel</button>
            </NavLink>
            </div>
        </div>
        </div>
        </form>
        </div>
    )
}

export default AddHomeForm