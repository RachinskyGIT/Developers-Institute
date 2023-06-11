// Exercise4.js

import React from 'react';
import './Exercise4.css'; 

const style_header = {
  color: 'white',
  backgroundColor: 'DodgerBlue',
  padding: '10px',
  fontFamily: 'Arial'
};

function Exercise4() {
  return (
    <div>
      <h1 style={style_header}>Exercise 4</h1>
      <p className="para">This is a paragraph.</p> {/* Apply the CSS class */}
      <a href="https://example.com">Link</a>
      <form>
        <input type="text" placeholder="Enter your name" />
        <button type="submit">Submit</button>
      </form>
      <img src="image.jpg" alt="Example" />
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
    </div>
  );
}

export default Exercise4;
