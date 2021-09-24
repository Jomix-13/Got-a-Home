
import { useDispatch, useSelector } from 'react-redux'
import './splashpage.css'
import { fetchAllHomes } from '../../store/home'
import { useEffect, useState } from 'react'

import './splashpage.css'
import { useHistory } from 'react-router'
const SplashPage = () =>{

    const [search, setSearch] = useState('')


    const homes = useSelector(state => state.homesReducer.homes)
    const searchHomes = homes.filter(home => home.stAddress.toLowerCase().includes(search.toLowerCase()));
    const searchCity= homes.filter(home => home.city.toLowerCase().includes(search.toLowerCase()));
    // const searchZip = homes.filter(home => home.zipCode.includes(search));


    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(()=>{
        dispatch(fetchAllHomes())
    },[dispatch])

    const onSubmit = (e) => {
        e.preventDefault()
    }

    const toPage = (e) => {
        e.preventDefault();
        if (e.target.value.includes('Results')){
            return
        } else if (e.target.value.includes('home')) {
            setSearch('')
            const homeId = (e.target.value.slice(4))
            return history.push(`/homes/${homeId}`);
        } else {
            setSearch('')
            return history.push(`/spots/${e.target.value}`);
        }
    }

    return (
        <>
        <div className='All'>
            <div className="hwrap2">
                <div className="hmove2">
                <div className="hitem2">
                    <div>
                        THE WAY YOU FIND YOUR HOME.
                    </div>
                </div>
                </div>
            </div>
        </div>
        <div className='i'>
            {/* <img src='https://webassets.inman.com/wp-content/uploads/2018/01/shutterstock_752498263-1400x621.jpg' alt=""/> */}
            <div className='searchbar'>
                {/* <input type="text"  onkeyup="myFunction()" placeholder="Search... "/> */}
                <form onSubmit={onSubmit}>
                    <input
                        id="myInput"
                        className='nav-search-input'
                        type='text'
                        name='search'
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        placeholder='Search...'>
                    </input>
                    {search &&
                        <select className='search-results' onChange={toPage} size={searchHomes.length + searchCity.length + 2}>
                                <option className='search-results-title'>({searchHomes.length + searchCity.length} results)</option>
                            {searchHomes.map(home => (
                                <option key={home.id} value={'home' + home.id}>{home.stAddress}, {home.city}, {home.state}, {home.Zipcode}</option>
                            ))}
                                {/* <option className='search-results-title'>Search Cities Results ({searchCity.length})</option> */}
                            {searchCity.map(home => (
                                <option key={home.id} value={'home' + home.id}>{home.stAddress}, {home.city}, {home.state}, {home.Zipcode}</option>
                            ))}
                        </select>
                    }
                </form>
            </div>
        </div>
        </>
    )
}

export default SplashPage