const GET_ALL_HOMES = 'homes/getAllHomes'
const GET_ONE_HOME = 'homes/getOneHomes'

const getAllHomes = (homes) =>{
    return {
        type : GET_ALL_HOMES,
        homes
    }
}

const getOneHome = (home) =>{
    return {
        type : GET_ONE_HOME,
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

export const fetchOneHome = (id) => async (dispatch) => {
    const res = await fetch(`/api/homes/${id}`)

    if(res.ok) {
        const home = await res.json()
        console.log('ttttttttttt',home)
        dispatch(getOneHome(home))
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
        case GET_ONE_HOME:
            return {
                ...state,
                home : action.home
            }
        default:
            return state
    }
}

export default homesReducer