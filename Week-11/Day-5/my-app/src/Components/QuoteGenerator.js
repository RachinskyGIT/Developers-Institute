import React, { useState, useEffect } from 'react';
import quotes from './quotes';

const QuoteGenerator = () => {
    
  let color = useState(getRandomColor())
  const [quote, setQuote] = useState(getRandomQuote());
  const [textColor, setTextColor] = color;
  const [pageBackgroundColor, setPageBackgroundColor] = color;
  const [isTransitioning, setIsTransitioning] = useState(false);

  useEffect(() => {
    document.body.style.backgroundColor = pageBackgroundColor;
    setIsTransitioning(true);
    const transitionTimeout = setTimeout(() => {
      setIsTransitioning(false);
    }, 500);

    return () => clearTimeout(transitionTimeout);
  }, [pageBackgroundColor]);

  function getRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
  }

  function getRandomColor() {
    const randomColor = Math.floor(Math.random() * 16777215).toString(16);
    return `#${randomColor}`;
  }

  function generateNewQuote() {
    let newQuote = getRandomQuote();

    // Ensure the new quote is different from the current one
    while (newQuote.quote === quote.quote) {
      newQuote = getRandomQuote();
    }

    setQuote(newQuote);
    setTextColor(getRandomColor());
    setPageBackgroundColor(getRandomColor());
  }

  return (
    <div
      style={{
        backgroundColor: '#fff',
        padding: '20px',
        borderRadius: '5px',
        textAlign: 'center',
        transition: isTransitioning ? 'background-color 0.5s ease' : '',
      }}
    >
      <h1 style={{ color: textColor }}>{quote.quote}</h1>
      <p>- {quote.author}</p>
      <button
        style={{ backgroundColor: textColor, color: '#fff' }}
        onClick={generateNewQuote}
      >
        Generate New Quote
      </button>
    </div>
  );
};

export default QuoteGenerator;
