// import React, { useState } from 'react';

// class Counter extends React.Component {
//   constructor() {
//       super()
//       this.state = {
//           counter: 0
//       }
//   }

//   handleClickCounter = () => {
//       this.setState({counter: this.state.counter + 1}, () => {
//           if (this.state.counter >= 5) {
//               throw new Error("I crashed")
//           }
//       })
      
//   }

//   render() {
//       return (
//           <div>
//               <p>{this.state.counter}</p>
//               <button onClick={this.handleClickCounter}>Increment</button>
//           </div>
//       )
//   }
// }
// export default Counter;



import React, { Component } from 'react';

class BuggyCounter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 0
    };
  }

  handleClick = () => {
    const { counter } = this.state;
    this.setState({ counter: counter + 1 });
    if (counter === 4) {
      throw new Error('I crashed!');
    }
  };

  render() {
    const { counter } = this.state;
    return (
      <div>
        <h1 onClick={this.handleClick}>{counter}</h1>
      </div>
    );
  }
}

export default BuggyCounter;
