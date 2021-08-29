import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/loginModal/LoginForm';
import SignUpForm from './components/signupModal/SignUpForm';
import NavBar from './components/NavBar';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import HomePage from './components/HomePage';
import OneHome from './components/OneHome';
import AddHomeForm from './components/AddHome';
import EditHomeForm from './components/EditHome';
import SplashPage from './components/SplashPage'

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        {/* <Route path='/login' exact={true}>
          <LoginForm />
        </Route> */}
        {/* <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route> */}
        {/* <Route path='/users' exact={true} >
          <UsersList/>
        </Route> */}
        {/* <Route path='/users/:userId' exact={true} >
          <User />
        </Route> */}
        <Route path='/' exact={true} >
          <SplashPage></SplashPage>
        </Route>
        <Route path='/homes'>
        <HomePage></HomePage>
        </Route>
        <Route path='/homes/:id'>
          <OneHome></OneHome>
        </Route>
        <Route path='/sellhomes'>
          <AddHomeForm></AddHomeForm>
        </Route>
        <Route path='/update/:id'>
          <EditHomeForm></EditHomeForm>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
