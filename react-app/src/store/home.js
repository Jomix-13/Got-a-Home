const GET_ALL_HOMES = 'homes/getAllHomes'

const getAllHomes = (homes) =>{
    return {
        type : GET_ALL_HOMES,
        homes
    }
}

export const fetchAllHomes = () => async (dispatch) => {
    const res = await fetch('/api/homes/')

    if(res.ok) {
        const homes = await res.json()
        console.log('TTTTTTTTTTT',homes)
        dispatch(getAllHomes(homes))
    }
}

const intialstate = {
    homes : []
}

const homesReducer = (state = intialstate,action)=>{
    switch(action.type) {
        case GET_ALL_HOMES:
            return { 
                ...state,
                ...action.homes
            }
        default:
            return state
    }
}

export default homesReducer