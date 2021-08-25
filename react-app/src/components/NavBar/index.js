
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { login } from '../../store/session';
import LoginFormModal from '../loginModal'
import SignupFormModal from '../signupModal'


import './Navbar.css'

const NavBar = () => {
    const user = useSelector(state => state.session.user)
    const dispatch = useDispatch()

    const dempButton = (e) => {
        e.preventDefault();
        dispatch(login('Demo@email.com','demo'));
    };

  return (
    <nav>
      <div className='navbar'>
        <div className='homeButton'>
          <NavLink to='/' exact={true} activeClassName='active'>
            <img src='https://i.imgur.com/O6He0KH.png' alt=""/>
          </NavLink>
        </div>
        {!user ?
        <div className='notloggedin'>
            <div>
            {/* <NavLink to='/login' exact={true} activeClassName='active'>
                Login
            </NavLink> */}
            <LoginFormModal></LoginFormModal>
            </div>
            <div>
                <button onClick={dempButton}>
                    Demo
                </button>
            </div>
            <div>
            {/* <NavLink to='/sign-up' exact={true} activeClassName='active'>
                Sign Up
            </NavLink> */}
            <SignupFormModal></SignupFormModal>
            </div>
        </div> :
        <div className='loggedin'>
            <div>
            <NavLink to='/users' exact={true} activeClassName='active'>
                Users
            </NavLink>
            </div>
            <div>
            <LogoutButton />
            </div>
        </div> }
      </div>
      <div className="hwrap"><div className="hmove">
        {/* <div class="hitem">
            <NavLink to='/homes' alt=''>Buy</NavLink>
        </div>
        <div class="hitem">
            <NavLink to='/homes' alt=''>Rent</NavLink>
        </div>
        <div class="hitem">
            <NavLink to='/homes' alt=''>Sell</NavLink>
        </div> */}
        <div className="hitem">
            <NavLink to='/homes' alt=''>Buy</NavLink>

            <NavLink to='/homes' alt=''>Rent</NavLink>

            <NavLink to='/homes' alt=''>Sell</NavLink>
        </div>

        
    </div></div>
    </nav>
  );
}

export default NavBar;

