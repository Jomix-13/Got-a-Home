import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { Redirect, useHistory } from "react-router-dom"
import Errors from '../errors'


import { fetchEditHome } from "../../store/home"

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


const EditHomeForm = () => {

    const home = useSelector(state => state.homesReducer.home)

    const [price, setPrice] = useState(home.price)
    const [stAddress, setStAddress] = useState(home.stAddress)
    const [city, setCity] = useState(home.city)
    const [state, setState] = useState(home.state)
    const [zipCode, setZipCode] = useState(home.zipCode)
    const [latitude, setLatitude] = useState(home.latitude)
    const [longitude, setLongitude] = useState(home.longitude)
    const [lotSize, setLotSize] = useState(home.lotSize)
    const [beds, setBeds] = useState(home.beds)
    const [bath, setBath] = useState(home.bath)
    const [status, setStatus] = useState(home.status)
    const [image, setImage] = useState(home.images[0])

    const dispatch = useDispatch()
    const history = useHistory()

    const onSubmit = (e) => {
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
        dispatch(fetchEditHome(payload,home.id))
        history.push(`/homes/${home.id}`)
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label>Price</label>
                <input
                    type='text'
                    value={price}
                    onChange={e=>setPrice(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>Street Address</label>
                <input
                    type='text'
                    value={stAddress}
                    onChange={e=>setStAddress(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>City</label>
                <input
                    type='text'
                    value={city}
                    onChange={e=>setCity(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>State</label>
                <select
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
            <div>
                <label>Zip Code</label>
                <input
                    type='number'
                    value={zipCode}
                    onChange={e=>setZipCode(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>Latitude</label>
                <input
                    type='number'
                    value={latitude}
                    onChange={e=>setLatitude(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>Longitude</label>
                <input
                    type='number'
                    value={longitude}
                    onChange={e=>setLongitude(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>No. Beds</label>
                <input
                    type='number'
                    value={beds}
                    onChange={e=>setBeds(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>No. Bath</label>
                <input
                    type='number'
                    value={bath}
                    onChange={e=>setBath(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>Lot Size</label>
                <input
                    type='number'
                    value={lotSize}
                    onChange={e=>setLotSize(e.target.value)}
                >
                </input>
            </div>
            <div>
                <label>Status</label>
                <select
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
            <div>
                <label>Image</label>
                <input
                    type='text'
                    value={image}
                    onChange={e=>setImage(e.target.value)}
                >
                </input>
            </div>
            <button type="submit">Submit</button>
        </form>

    )
}

export default EditHomeForm