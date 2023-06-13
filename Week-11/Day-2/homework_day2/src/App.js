// App.js

import React from 'react';
import Car from './Components/Car';

const carInfo = {
  name: 'Ford',
  model: 'Kek',
};

function App() {
  return (
    <div>
      <Car carInfo={carInfo} />
    </div>
  );
}

export default App;
