import React from 'react';

class Garage extends React.Component {
  render() {
    const { size } = this.props;
    return <h2>Who lives in my {size} Garage?</h2>;
  }
}

export default Garage;
