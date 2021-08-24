
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { login } from '../../store/session';
import LoginFormModal from '../loginModal'


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
            <NavLink to='/sign-up' exact={true} activeClassName='active'>
                Sign Up
            </NavLink>
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
    </nav>
  );
}

export default NavBar;

