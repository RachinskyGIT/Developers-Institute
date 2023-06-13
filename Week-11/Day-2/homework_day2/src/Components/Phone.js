import React from 'react';

class Phone extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      brand: 'Samsung',
      model: 'Galaxy S20',
      color: 'black',
      year: 2020,
    };
  }

  changeColor = () => {
    this.setState({ color: 'blue' });
  };

  render() {
    const { brand, model, color, year } = this.state;
    return (
      <div>
        <h2>Phone Details:</h2>
        <p>Brand: {brand}</p>
        <p>Model: {model}</p>
        <p>Color: {color}</p>
        <p>Year: {year}</p>
        <button onClick={this.changeColor}>Change Color</button>
      </div>
    );
  }
}

export default Phone;
