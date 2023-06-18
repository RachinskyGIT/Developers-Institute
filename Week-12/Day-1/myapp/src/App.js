import React from 'react';
import { connect } from 'react-redux';
import MovieList from './components/MovieList';
import MovieDetails from './components/MovieDetails';
import './App.css';


class App extends React.Component {
  render() {
    return (
      <div className="App">
        <h1>Redux Movies</h1>
        <div className="container">
          <div className="left-column">
            <MovieList />
          </div>
          <div className="right-column">
            <MovieDetails />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
