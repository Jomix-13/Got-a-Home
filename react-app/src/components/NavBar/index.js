
import React,{useState} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { login } from '../../store/session';
import LoginFormModal from '../loginModal'
import SignupFormModal from '../signupModal'


import './Navbar.css'

const NavBar = () => {
    const user = useSelector(state => state.session.user)
    console.log(user)
    const dispatch = useDispatch()

    const history = useHistory()

    const [search, setSearch] = useState('')

    const homes = useSelector(state => state.homesReducer.homes)
    const searchHomes = homes.filter(home => home.stAddress.toLowerCase().includes(search.toLowerCase()));
    const searchCity= homes.filter(home => home.city.toLowerCase().includes(search.toLowerCase()));

    const dempButton = (e) => {
        e.preventDefault();
        dispatch(login('Demo@email.com','demo'));
        history.push('./homes')

    };

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
    <nav>
      <div className='navbar'>
        <div className='homeButton'>
          <NavLink to='/homes' exact={true} activeClassName='active'>
            <div className='home'>
              HOME
            </div>
            {/* <img src='https://i.imgur.com/vZ0TUsl.png' alt=""/> */}
          </NavLink>
        </div>
        <div className='searchnavbar'>
        <div className='io'>
            <i class="fas fa-search" onClick={onSubmit}></i>
          {/* <NavLink to='/' exact={true} activeClassName='active'> */}
            {/* <img src='https://i.imgur.com/Rine4Vb.png'/> */}
          {/* </NavLink> */}
          </div>
          <div className='i2'>
            <div className='searchbar2'>
                <form onSubmit={onSubmit}>
                    <input
                        id="myInput2"
                        className='nav-search-input2'
                        type='text'
                        name='search'
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        placeholder='Search...'>
                    </input>
                    {search &&
                        <select className='search-results2' onChange={toPage} size={searchHomes.length + searchCity.length + 2}>
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
        
        </div>
        {!user ?
        <div className='notloggedin'>
            <div>
            {/* <NavLink to='/login' exact={true} activeClassName='active'>
                Login
            </NavLink> */}
            <LoginFormModal className='d '></LoginFormModal>
            </div>
            <div>
                <button className='d pointer' onClick={dempButton}>
                    Demo
                </button>
            </div>
            <div>
            {/* <NavLink to='/sign-up' exact={true} activeClassName='active'>
                Sign Up
            </NavLink> */}
            <SignupFormModal className='d'></SignupFormModal>
            </div>
        </div> :
        <div className='loggedin'>
          <div className='pp'>
          <div>
            {user.username}
          </div>
          <div>
            <img src={user.profilepic} alt='' />
          </div>
          </div>
            <div>
            <LogoutButton className='d '/>
            </div>
        </div> }
      </div>
      <div className="hwrap">
        <div className="hmove">
        <div className="hitem">
            <NavLink to='/buyhomes' alt=''>Buy</NavLink>

            <NavLink to='/renthomes' alt=''>Rent</NavLink>
            {!user ? null :
            <NavLink to='/sellhomes' alt=''>Sell</NavLink>
            }
        </div>
      </div>
      </div>
    </nav>
  );
}

export default NavBar;

