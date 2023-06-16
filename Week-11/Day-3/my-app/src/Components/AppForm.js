import React from 'react';
import './eyepopping.css'; // Import the custom CSS file

class AppForm extends React.Component {
  constructor() {
    super();
    this.state = {
      firstname: '',
      lastname: '',
      age: '',
      color: '',
      gender: '',
      vegan: false,
      noNuts: false,
      lactoseFree: false,
    };

    this.formRef = React.createRef();
  }

  handleSubmit = (e) => {
    e.preventDefault();
    const { firstname, lastname, age, color, gender, vegan, noNuts, lactoseFree } = this.state;

    // Perform validation if age is positive
    if (age && age <= 0) {
      alert('Please enter a valid age.');
      return;
    }

    // Perform any necessary operations with the form data

    // Update the URL with the form data if there are any values
    const searchParams = new URLSearchParams();
    if (firstname) searchParams.append('firstname', firstname);
    if (lastname) searchParams.append('lastname', lastname);
    if (age) searchParams.append('age', age);
    if (color) searchParams.append('color', color);
    if (gender) searchParams.append('gender', gender);
    if (vegan) searchParams.append('vegan', vegan);
    if (noNuts) searchParams.append('noNuts', noNuts);
    if (lactoseFree) searchParams.append('lactoseFree', lactoseFree);

    const newUrl = searchParams.toString() ? `${window.location.pathname}?${searchParams.toString()}` : window.location.pathname;
    window.history.pushState(null, '', newUrl);

    // Reset the form
    this.formRef.current.reset();
    this.setState({
      firstname: '',
      lastname: '',
      age: '',
      color: '',
      gender: '',
      vegan: false,
      noNuts: false,
      lactoseFree: false,
    });
  };

  handleChange = (e) => {
    const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value;
    this.setState({ [e.target.name]: value });
  };

  render() {
    const { firstname, lastname, age, color, gender, vegan, noNuts, lactoseFree } = this.state;

    return (
      <>
        <h1>Form</h1>
        <form ref={this.formRef} onSubmit={this.handleSubmit}>
          <div className="input-wrapper">
            First Name: <input type="text" name="firstname" onChange={this.handleChange} value={firstname} />
          </div>
          <div className="input-wrapper">
            Last Name: <input type="text" name="lastname" onChange={this.handleChange} value={lastname} />
          </div>
          <div className="input-wrapper">
            Age: <input type="number" name="age" onChange={this.handleChange} value={age} />
          </div>

          <div className="input-wrapper">
            <label>
              <input type="radio" name="gender" value="Male" onChange={this.handleChange} checked={gender === 'Male'} /> Male
            </label>
            <label>
              <input type="radio" name="gender" value="Female" onChange={this.handleChange} checked={gender === 'Female'} /> Female
            </label>
          </div>

          <div className="input-wrapper">
            Favorite Color: <br />
            <select name="color" onChange={this.handleChange} value={color}>
              <option value="">Select color</option>
              <option value="red">Red</option>
              <option value="blue">Blue</option>
              <option value="green">Green</option>
            </select>
          </div>

          <div className="input-wrapper">
            Is Vegan: <input type="checkbox" name="vegan" onChange={this.handleChange} checked={vegan} />
          </div>
          <div className="input-wrapper">
            Lactose-free: <input type="checkbox" name="lactoseFree" onChange={this.handleChange} checked={lactoseFree} />
          </div>
          <div className="input-wrapper">
            Nuts free: <input type="checkbox" name="noNuts" onChange={this.handleChange} checked={noNuts} />
          </div>

          <button type="submit">Submit</button>
        </form>

        <div id="info-section">
          <h2>Entered information:</h2>
          <p>
            <span className="info-label">Your name:</span> {firstname} {lastname}
            <br />
            <span className="info-label">Your age:</span> {age}
            <br />
            <span className="info-label">Your gender:</span> {gender}
            <br />
            <span className="info-label">Your favorite color:</span> {color}
            <br />
            <span className="info-label">Your dietary restrictions:</span>
            <br />
            <span className="info-label">Vegan meal:</span> {vegan ? 'Yes' : 'No'}
            <br />
            <span className="info-label">Lactose-free:</span> {lactoseFree ? 'Yes' : 'No'}
            <br />
            <span className="info-label">Nuts free:</span> {noNuts ? 'Yes' : 'No'}
          </p>
        </div>
      </>
    );
  }
}

export default AppForm;
