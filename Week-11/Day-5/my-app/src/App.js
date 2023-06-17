import React from 'react';
import QuoteGenerator from './Components/QuoteGenerator';
import './App.css';
import TodoList from './Components/TodoList';


// // Random Quote Generator
// const App = () => {
//   return (
//     <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
//       <QuoteGenerator />
//     </div>
//   );
// };


// ToDo list
function App() {
  return (
    <div className="App">
        <TodoList/>
    </div>
  );
}

export default App;
