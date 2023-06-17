import React from 'react';
import data from './data_xp3.json';

class Example2 extends React.Component {
  render() {
    const { Skills } = data;

    return (
      <div>
        <h3>Example2 start</h3>
        <h1>Skills:</h1>
        {Skills.map((skill, index) => (
          <div key={index}>
            <h3>{skill.Area}</h3>
            <ul>
              {skill.SkillSet.map((item, subIndex) => (
                <li key={subIndex}>
                  {item.Name} - {item.Hot ? 'Hot' : 'Not Hot'}
                </li>
              ))}
            </ul>
          </div>
        ))}
        <h3>Example2 end</h3>
      </div>
    );
  }
}

export default Example2;
