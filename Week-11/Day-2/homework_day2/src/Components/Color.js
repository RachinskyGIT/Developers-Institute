import React from 'react';

class Color extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteColor: 'red',
    };
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({ favoriteColor: 'yellow' });
    }, 5000);
  }

  changeColor = () => {
    this.setState({ favoriteColor: 'blue' });
  };

  render() {
    return (
      <div>
        <h2>Favorite Color: {this.state.favoriteColor}</h2>
        <button onClick={this.changeColor}>Change Color</button>
      </div>
    );
  }
}

export default Color;
