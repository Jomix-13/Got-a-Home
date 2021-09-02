
import React from 'react';
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

    const dempButton = (e) => {
        e.preventDefault();
        dispatch(login('Demo@email.com','demo'));
        history.push('./homes')

    };

  return (
    <nav>
      <div className='navbar'>
        <div className='homeButton'>
          <NavLink to='/homes' exact={true} activeClassName='active'>
            <img src='https://i.imgur.com/vZ0TUsl.png' alt=""/>
          </NavLink>
        </div>
        <div className='io'>
          <NavLink to='/' exact={true} activeClassName='active'>
            <img src='https://i.imgur.com/Xc4j024.png' alt=''></img>
          </NavLink>
        </div>
        {!user ?
        <div className='notloggedin'>
            <div>
            {/* <NavLink to='/login' exact={true} activeClassName='active'>
                Login
            </NavLink> */}
            <LoginFormModal className='d'></LoginFormModal>
            </div>
            <div>
                <button className='d' onClick={dempButton}>
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
            <LogoutButton className='d'/>
            </div>
        </div> }
      </div>
      <div className="hwrap"><div className="hmove">
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

