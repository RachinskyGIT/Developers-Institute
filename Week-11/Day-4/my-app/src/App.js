import React from 'react';

const App = () => {
  const postData = async () => {
    try {
      const url = 'https://webhook.site/647abb1b-9ef0-4b1e-96a5-546a3e0046ad';
      const data = {
        key1: 'myusername',
        email: 'mymail@gmail.com',
        name: 'Isaac',
        lastname: 'Doe',
        age: 27,
      };

      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const responseData = await response.json();
        console.log(responseData);
      } else {
        console.error('Error:', response.status);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <button onClick={postData}>Send Request</button>
    </div>
  );
};

export default App;
