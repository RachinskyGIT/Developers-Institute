import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import { insertTransaction, updateTransaction } from '../Actions/transactionActions';

const TransactionForm = ({ currentIndex, currentTransaction, insertTransaction, updateTransaction }) => {
  const [formData, setFormData] = useState({
    accountNumber: '',
    FSC: '',
    name: '',
    amount: '',
  });

  useEffect(() => {
    if (currentTransaction && currentTransaction.id) {
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
      insertTransaction(formData);
    } else {
      // Update transaction
      updateTransaction(currentIndex, formData);
    }

    setFormData({
      accountNumber: '',
      FSC: '',
      name: '',
      amount: '',
    });
  };

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
