import React, { useState, useEffect } from 'react';
import Card from './Card';
import superheroesData from './superheroes.json';
import './GameBoard.css';

const GameBoard = () => {
  const [superheroes, setSuperheroes] = useState(superheroesData.superheroes);
  const [score, setScore] = useState(0);
  const [topScore, setTopScore] = useState(0);
  const [selectedHeroes, setSelectedHeroes] = useState([]);


  useEffect(() => {
    shuffleCards();
  }, []);

  const shuffleCards = () => {
    const shuffledSuperheroes = [...superheroes];
    for (let i = shuffledSuperheroes.length - 1; i > 0; i--) {
      const randomIndex = Math.floor(Math.random() * (i + 1));
      [shuffledSuperheroes[i], shuffledSuperheroes[randomIndex]] = [
        shuffledSuperheroes[randomIndex],
        shuffledSuperheroes[i],
      ];
    }
    setSuperheroes(shuffledSuperheroes);
  };

  const handleCardClick = (clickedId) => {
    const clickedSuperhero = superheroes.find((superhero) => superhero.id === clickedId);
    console.log('Clicked ID:', clickedSuperhero.id); // Print the clicked ID in the console


    if (!clickedSuperhero.clicked) 
     {
      setSuperheroes((prevSuperheroes) =>
        prevSuperheroes.map((superhero) => {
          if (superhero.id === clickedId) {
            return { ...superhero, clicked: true };
          }
          return superhero;
        })
      );
      setScore((prevScore) => prevScore + 1);

      if ((!selectedHeroes.includes(clickedId)) && (score + 1 > topScore)) {
        setTopScore((prevTopScore) => prevTopScore + 1);
      }   
    
      if (!selectedHeroes.includes(clickedId)) {
        setSelectedHeroes((prevSelectedHeroes) => [...prevSelectedHeroes, clickedId]); // Add the clickedId to the selectedHeroes list if it's not already present
        console.log('Selected Heroes:', selectedHeroes); // Print the selected heroes list in the console
      } else {
        console.log('This hero is already selected.'); // Print a message if the hero is already selected
        setScore(0);
        setSelectedHeroes([]);
      }
    }

    shuffleCards();
  };

  return (
    <div className="game-board">
      <h1>Superheroes React Memory Game</h1>
      <div className="score-board">
        <span>Current Score: {score}</span>
        <br />
        <span>Top Score: {topScore}</span>
      </div>
      <div className="card-grid">
        {superheroes.map((superhero) => (
          <Card 
          key={superhero.id} 
          superhero={superhero} 
          onClick={() => handleCardClick(superhero.id)}
          />
        ))}
      </div>
    </div>
  );
};

export default GameBoard;
