import React from 'react';
import ErrorBoundary from './Components/ErrorBoundary';
import Car from './Components/Car';

const listCars = [
  {
    id: 1,
    brand: "ford",
    name: "ford torino",
    year: "1970-01-01",
    origin: "USA"
  },
  {
    id: 2,
    brand: "vespe",
    name: "vespe galaxie 500",
    year: "1970-01-01",
    origin: "USA"
  },
  {
    id: 2,
    brand: "chevrolet",
    name: "chevrolet vega 2300",
    year: "1971-01-01",
    origin: "USA"
  },
]

class App extends React.Component {
  constructor() {
    super();
  }

  render() {
    return (
      <div className="box" >
        <ErrorBoundary>
          <Car listCars={listCars} />
        </ErrorBoundary>
      </div>
    )
  }
}

export default App;