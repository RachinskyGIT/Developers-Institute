import React from 'react';
import data from './data_xp3.json';

class Example3 extends React.Component {
  render() {
    const { Experiences } = data;

    return (
      <div>
        <h3>Example3 start</h3>
        <h1>Experiences:</h1>
        {Experiences.map((experience, index) => (
          <div key={index}>
            <h3>{experience.companyName}</h3>
            <a href={experience.url}>
              <img src={experience.logo} alt={experience.companyName} />
            </a>
            {experience.roles.map((role, subIndex) => (
              <div key={subIndex}>
                <h4>{role.title}</h4>
                <p>{role.description}</p>
                <p>
                  {role.startDate} - {role.endDate}
                </p>
                <p>{role.location}</p>
              </div>
            ))}
          </div>
        ))}
        <h3>Example3 end</h3>
      </div>
    );
  }
}

export default Example3;
