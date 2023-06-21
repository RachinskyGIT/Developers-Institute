import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import { insertTransaction, updateTransaction } from '../Actions/transactionActions';

const TransactionForm = ({ currentIndex, currentTransaction, insertTransaction, updateTransaction }) => {
  const [formData, setFormData] = useState({
    accountNumber: '',
    id: null,
    FSC: '',
    name: '',
    amount: '',
  });

  const [lastId, setLastId] = useState(0);


  useEffect(() => {
    if (currentTransaction && currentTransaction.idx) {
      const { accountNumber, FSC, name, amount } = currentTransaction;
      setFormData({ accountNumber, FSC, name, amount });
    }
  }, [currentTransaction]);

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (currentIndex === -1) {
      // Insert transaction
      const newTransaction = { ...formData, id: lastId + 1 };
      insertTransaction(newTransaction);
      setLastId(lastId + 1);
    } else {
      // Update transaction
      updateTransaction(currentIndex, formData);
    }

    setFormData({
      id: null,
      accountNumber: '',
      FSC: '',
      name: '',
      amount: '',
    });
  };

  useEffect(() => {
    // Clear form fields when currentIndex changes to -1
    if (currentIndex === -1) {
      setFormData({
        accountNumber: '',
        FSC: '',
        name: '',
        amount: '',
      });
    }
  }, [currentIndex]);

  return (
    <div>
      <h2>Transaction Form</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Account Number:
          <input type="text" name="accountNumber" value={formData.accountNumber} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          FSC:
          <input type="text" name="FSC" value={formData.FSC} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Name:
          <input type="text" name="name" value={formData.name} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Amount:
          <input type="text" name="amount" value={formData.amount} onChange={handleInputChange} />
        </label>
        <br />
        <button type="submit">{currentIndex === -1 ? 'Add Transaction' : 'Update Transaction'}</button>
      </form>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    currentIndex: state.currentIndex,
    currentTransaction: state.list[state.currentIndex],
  };
};

const mapDispatchToProps = {
  insertTransaction,
  updateTransaction,
};

export default connect(mapStateToProps, mapDispatchToProps)(TransactionForm);
