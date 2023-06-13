import React from 'react';
import Garage from './Garage';

class Car extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      color: 'blue',
    };
  }

  render() {
    const { name, model } = this.props.carInfo;
    const { color } = this.state;
    return (
      <div>
        <h1>This car is {color} {name} {model}</h1>
        <Garage size="small" />
      </div>
    );
  }
}

export default Car;
