import React from 'react';
import ColorComponent from './Components/ColorComponent';
import ErrorBoundary from './Components/ErrorBoundary';

class App extends React.Component {
  render() {
    return (
      <div>
        <h2>Simulation 1:</h2>
        <ErrorBoundary>
          <ColorComponent />
          <ColorComponent />
        </ErrorBoundary>

        <h2>Simulation 2:</h2>
        <ErrorBoundary>
          <ColorComponent />
        </ErrorBoundary>
        <ErrorBoundary>
          <ColorComponent />
        </ErrorBoundary>

        <h2>Simulation 3:</h2>
        <ColorComponent />
      </div>
    );
  }
}

export default App;
