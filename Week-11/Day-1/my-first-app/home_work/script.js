// xp1_1
// Create an <h1> element without JSX
const element = document.createElement('h1');
element.textContent = 'I do not use JSX';

// Render the element to the document body
document.body.appendChild(element);

// xp1_2
// Create a constant variable with JSX
const myelement = <h1>Hello World!</h1>;

// Render the JSX element to the document body
ReactDOM.render(myelement, document.getElementById('root'));

// Create a constant variable named sum
const sum = 5 + 5;

// Render the JSX element and the sum on the page
ReactDOM.render(
  <div>
    {myelement}
    <p>React is {sum} times better with JSX</p>
  </div>,
  document.getElementById('root')
);

// xp1_3
import UserFavoriteColors from './Components/UserFavoriteColors';

function UserDetails() {
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
  };

  return (
    <div>
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <UserFavoriteColors favAnimals={user.favAnimals} />
    </div>
  );
}

