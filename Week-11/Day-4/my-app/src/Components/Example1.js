import React from 'react';
import data from './data_xp3.json';

class Example1 extends React.Component {
  render() {
    const { SocialMedias } = data;

    return (
      <div>
        <h3>Example1 start</h3>
        <h1>Social Media Links:</h1>
        <ul>
          {SocialMedias.map((link, index) => (
            <li key={index}>
              <a href={link}>{link}</a>
            </li>
          ))}
        </ul>
        <h3>Example1 end</h3>
      </div>
    );
  }
}

export default Example1;
