// import React from 'react';
// import ErrorBoundary from './Components/ErrorBoundary';
// import Counter from './Components/BuggyCounter';

// function App() {
//   return (
//     <div>
//       <p>
//         <b>
//           Click on the numbers to increase the counters.<br />
//           The counter is programmed to throw an error when it reaches 5. This simulates a JavaScript error in a component.
//         </b>
//       </p>
//       <hr />
//       <ErrorBoundary>
//         <p>
//           These two counters are inside the same error boundary. If one crashes, the error boundary will replace both of them.
//         </p>
//         <Counter />
//         <Counter />
//       </ErrorBoundary>
//       <hr />
//       <p>
//         These two counters are each inside of their own error boundary. So if one crashes, the other is not affected.
//       </p>
//       <ErrorBoundary>
//         <Counter />
//       </ErrorBoundary>
//       <ErrorBoundary>
//         <Counter />
//       </ErrorBoundary>
//       <hr />
//       <p>
//         This counter is not inside of a boundary. So if it crashes, all other components are deleted.
//       </p>
//       <Counter />
//     </div>
//   );
// }

// export default App;


import React from 'react';
import BuggyCounter from './Components/BuggyCounter';
import ErrorBoundary from './Components/ErrorBoundary';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Simulation 1:</h1>
        <ErrorBoundary>
          <BuggyCounter />
          <BuggyCounter />
        </ErrorBoundary>

        <h1>Simulation 2:</h1>
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>

        <h1>Simulation 3:</h1>
        <BuggyCounter />
      </div>
    );
  }
}

export default App;
