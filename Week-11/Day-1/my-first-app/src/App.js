import logo from './logo.svg';
import './App.css';
import Hello from './Hello';
import User from './Components/User.js'
import robots from './Components/users.json' 
import UserClass from './Components/UserClass'

console.log(robots[1].name)
function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <Hello />
        <User name="John" email = "ololo@gmail.com" />
        <User name="Marry" email = "marry@gmail.com" />
        <img src={logo} className="App-logo" alt="logo" /> */}
        {
          robots.map((item,indx) => {
            return <UserClass userinfo={item} key={indx}/>
          })
        }
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
