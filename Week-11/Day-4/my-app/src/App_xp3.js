import React from 'react';
import Example1 from './Components/Example1';
import Example2 from './Components/Example2';
import Example3 from './Components/Example3';

class App extends React.Component {
  render() {
    return (
      <div>
        <Example1 />
        <Example2 />
        <Example3 />
      </div>
    );
  }
}

export default App;
