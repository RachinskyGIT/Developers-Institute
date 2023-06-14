import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(prevCount => prevCount + 1);
    if (count === 4) {
      throw new Error("I crashed!");
    }
  };

  return (
    <div>
      <h1 onClick={handleClick}>{count}</h1>
    </div>
  );
};

export default Counter;
