// xp_3

import React from 'react';

class Child extends React.Component {
  componentWillUnmount() {
    alert('Child component is about to be unmounted!');
  }

  render() {
    return <h1>Hello World!</h1>;
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      show: true,
    };
  }

  handleDelete = () => {
    this.setState({ show: false });
  };

  render() {
    return (
      <div>
        {this.state.show && <Child />}
        <button onClick={this.handleDelete}>Delete header</button>
      </div>
    );
  }
}

export default App;
