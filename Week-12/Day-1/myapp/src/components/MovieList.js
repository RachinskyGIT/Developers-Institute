import React from 'react';
import { connect } from 'react-redux';
import { selectMovie } from '../actions';

const MovieList = (props) => {
  const handleClick = (movie) => {
    props.selectMovie(movie);
  };

  return (
    <div>
      <h2>Movie List</h2>
      {props.movies.map((movie) => (
        <div key={movie.title}>
          <h3>{movie.title}</h3>
          <button onClick={() => handleClick(movie)}>Select</button>
        </div>
      ))}
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    movies: state.movies
  };
};

export default connect(mapStateToProps, { selectMovie })(MovieList);
