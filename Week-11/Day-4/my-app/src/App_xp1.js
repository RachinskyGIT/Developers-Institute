import logo from './logo.svg';
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom'
import "bootstrap/dist/css/bootstrap.min.css";
import ErrorBoundary from './ErrorBoundary';

class HomeScreen extends React.Component{
  constructor(){
    super()
  }

  render(){
    return(
      <h1>Home</h1>
    )
  }
}

class ProfileScreen extends React.Component{
  constructor(){
    super()
  }

  render(){
    return(
      <h1>Profile Screen</h1>
    )
  }
}

class Shop extends React.Component{
  constructor(){
    super()
  }

  render(){

    throw Error('An error has occurred')
    
    return(
      <>
      <h1>Shop</h1>
      </>
    )
  }
}

//Exercise 1
function App() {
  return (
      <Router>
      <div className="App">
        <nav className='navbar-nav navbar-brand'>
          <ul>
            <li className='nav-item'><NavLink to='/'>Home</NavLink></li>
            <li className='nav-item'><NavLink to='/profile'>Profile</NavLink></li>
            <li className='nav-item'><NavLink to='/shop'>Shop</NavLink></li>
          </ul>          
        </nav>
      </div>
      <Routes>
        <Route path='/' element={<ErrorBoundary><HomeScreen/></ErrorBoundary>}/>
        <Route path='/profile' element={<ErrorBoundary><ProfileScreen/></ErrorBoundary>}/>
        <Route path='/shop' element={<ErrorBoundary><Shop/></ErrorBoundary>}/>
      </Routes>
    </Router>   
  );
}


export default App;