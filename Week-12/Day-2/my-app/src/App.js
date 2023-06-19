import React from 'react';
import TransactionForm from './Components/TransactionForm';
import TransactionList from './Components/TransactionList';

const App = () => {
  return (
    <div>
      <h1>Redux Financial Transactions App</h1>
      <TransactionForm />
      <TransactionList />
    </div>
  );
};

export default App;
