function UserFavoriteColors(props) {
    const { favAnimals } = props;
  
    return (
      <div>
        <h3>User Favorite Animals:</h3>
        <ul>
          {favAnimals.map((animal, index) => (
            <li key={index}>{animal}</li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default UserFavoriteColors;
  