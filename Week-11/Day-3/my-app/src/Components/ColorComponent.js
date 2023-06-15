import React, { Component } from 'react';

class ColorComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteColor: 'red'
    };
  }

  componentDidMount() {
    setTimeout(() => {
        this.setState({ favoriteColor: 'yellow'});
    }, 3000);
  }


  componentDidUpdate() {
    console.log('after update');
  }

  getSnapshotBeforeUpdate() {
    console.log('in getSnapshotBeforeUpdate');
    return null;
  }
  
  shouldComponentUpdate() {
    return true;
  }

  changeColor = () => {
    this.setState({ favoriteColor: 'blue' });
  };

  render() {
    const { favoriteColor } = this.state;
    return (
      <div>
        <h1 style={{ color: favoriteColor }}>My Favorite Color is {favoriteColor}</h1>
        <button onClick={this.changeColor}>Change Color</button>
      </div>
    );
  }
}

export default ColorComponent;
