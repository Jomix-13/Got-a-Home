import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import {fetchOneHome} from '../../store/home'
import homesReducer from "../../store/home"


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
        <div>
            <div>
                {home.price}
            </div>
        </div>

    )
}

export default OneHome