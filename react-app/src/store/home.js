import { setErrors } from "./errors";

const GET_ALL_HOMES = 'homes/getAllHomes'
const GET_20_HOMES = 'homes/get20Homes'
const GET_BUY_HOMES = 'homes/getBuyHomes'
const GET_RENT_HOMES = 'homes/getRentHomes'
const GET_ONE_HOME = 'homes/getOneHome'
const ADD_ONE_HOME = 'homes/addOneHome'
const DELETE_ONE_HOME = 'homes/deleteOneHome'
const EDIT_ONE_HOME = 'homes/editOneHome'

const getAllHomes = (homes) =>{
    return {
        type : GET_ALL_HOMES,
        homes
    }
}
const get20Homes = (homes) =>{
    return {
        type : GET_20_HOMES,
        homes
    }
}
const getBuyHomes = (homes) =>{
    return {
        type : GET_BUY_HOMES,
        homes
    }
}
const getRentHomes = (homes) =>{
    return {
        type : GET_RENT_HOMES,
        homes
    }
}

const getOneHome = (home) =>{
    return {
        type : GET_ONE_HOME,
        home
    }
}

const addOneHome = (home) =>{
    return {
        type : ADD_ONE_HOME,
        home
    }
}

const deleteOneHome = (homeid) =>{
    return {
        type : DELETE_ONE_HOME,
        homeid
    }
}

const editOneHome = (home) =>{
    return {
        type : EDIT_ONE_HOME,
        home
    }
}

export const fetchAllHomes = () => async (dispatch) => {
    const res = await fetch('/api/homes/')

    if(res.ok) {
        const homes = await res.json()
        dispatch(getAllHomes(homes))
    }
}

export const fetch20Homes = () => async (dispatch) => {
    const res = await fetch('/api/homes/splash')

    if(res.ok) {
        const homes = await res.json()
        dispatch(get20Homes(homes))
    }
}

export const fetchBuyHomes = () => async (dispatch) => {
    const res = await fetch('/api/homes/buy')

    if(res.ok) {
        const homes = await res.json()
        dispatch(getBuyHomes(homes))
    }
}
export const fetchRentHomes = () => async (dispatch) => {
    const res = await fetch('/api/homes/rent')

    if(res.ok) {
        const homes = await res.json()
        dispatch(getRentHomes(homes))
    }
}

export const fetchOneHome = (id) => async (dispatch) => {
    const res = await fetch(`/api/homes/${id}`)

    if(res.ok) {
        const home = await res.json()
        dispatch(getOneHome(home))
    }
}

export const fetchAddHome = (payload) => async (dispatch) => {

    const res = await fetch(`/api/homes/sell`,{
        method:'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    })
    const home = await res.json()
    
    if(res.ok) {
        dispatch(addOneHome(home))
        return home
    } else {
        // const home = await res.json()
        dispatch(setErrors(home));
      }
}

export const fetchDeleteHome = (homeid) => async (dispatch) => {

    const res = await fetch(`/api/homes/${homeid}`,{
        method:'DELETE',
        headers: { "Content-Type": "application/json" },
    })
    
    const home = await res.json()
    if(res.ok) {
        // const home = await res.json()
        dispatch(deleteOneHome(home))
    } 
}

export const fetchEditHome = (payload,id) => async (dispatch) => {

    const res = await fetch(`/api/homes/edit/${id}`,{
        method:'PUT',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    })
    
    const home = await res.json()
    
    if(res.ok) {
        dispatch(editOneHome(home))
        return home
    } else {
        // const home = await res.json()
        dispatch(setErrors(home));
    }
}


const intialstate = {
    homes : [],
    home : {}
}

const homesReducer = (state = intialstate,action)=>{
    switch(action.type) {
        case GET_ALL_HOMES:
            return { 
                ...state,
                ...action.homes
            }
        case GET_20_HOMES:
            return { 
                ...state,
                ...action.homes
            }
        case GET_BUY_HOMES:
            return { 
                ...state,
                ...action.homes
            }
        case GET_RENT_HOMES:
            return { 
                ...state,
                ...action.homes
            }
        case GET_ONE_HOME:
            return {
                ...state,
                home : action.home
            }
        case ADD_ONE_HOME:
            return {
                ...state,
                homes : [action.home,...state.homes]
            }
        case DELETE_ONE_HOME:
            // const deleteHome = {
            //     homes : [...state.homes.filter((home) => home.id !== action.homeid)],
            //     home : {...state.home}
            // }
            // return 
            return {
                ...state,
                 homes : [...state.homes.filter((home) => home.id !== action.homeid)],
                 home : {...state.home}
            }
        case EDIT_ONE_HOME:
            return {
                ...state,
                homes : [...state.homes.filter((home) => home.id !== action.home.id),action.home],
                home : action.home
            }
        default:
            return state
    }
}

export default homesReducer