import React from 'react';

const PostList = ({ data }) => {
  return (
    <div>
      <h1>Post List</h1>
      {data.map((post) => (
        <div key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
          <p>-{post.date}-</p>
        </div>
      ))}
    </div>
  );
};

export default PostList;
