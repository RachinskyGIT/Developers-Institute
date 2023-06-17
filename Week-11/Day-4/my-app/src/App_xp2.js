import React from 'react';
import data from './Components/data_xp2.json';
import PostList from './Components/PostList';

function App() {
  return (
    <div className="App">
      <PostList data={data} />
    </div>
  );
}

export default App;
