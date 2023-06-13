import React from 'react';

class Events extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isToggleOn: true,
    };
  }

  clickMe = () => {
    alert('I was clicked');
  };

  handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      alert('You pressed Enter');
    }
  };

  toggleState = () => {
    this.setState((prevState) => ({
      isToggleOn: !prevState.isToggleOn,
    }));
  };

  render() {
    const { isToggleOn } = this.state;
    return (
      <div>
        <button onClick={this.clickMe}>Click Me</button>
        <input type="text" onKeyDown={this.handleKeyDown} />
        <button onClick={this.toggleState}>
          Toggle: {isToggleOn ? 'ON' : 'OFF'}
        </button>
      </div>
    );
  }
}

export default Events;
