import React from'react'
import {connect} from 'react-redux';
import Counter from './components/Counter'
import Test from './components/Test'
import {changePropOne} from './redux/actions'

import './App.css'
class App extends React.Component {
  constructor() {
    super();
    this.state = {
      property_one:'text one'
    }
  }
  render(){
    return (
        <div className="App">
          <header className="App-header">
            {/* <Test/> */}
            <Counter/>
          </header>
        </div>
      );
  }
}

const mapStateToProps = (state) => {
  // console.log('store=>',state);
  return {
    a:state.property_one
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    one: (e) => dispatch(changePropOne(e.target.value))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App)




















// import {useState} from 'react'
// import Test from './components/Test'
//
// import './App.css';
//
// function App() {
//   const [title, setTitle] = useState('My title')
//   return (
//     <div className="App">
//       <header className="App-header">
//         <Test title={title} setTitle={setTitle}/>
//       </header>
//     </div>
//   );
// }
//
// export default App;
