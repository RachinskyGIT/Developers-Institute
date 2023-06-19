import React from 'react';
import { connect } from 'react-redux';
import { updateIndex, deleteTransaction } from '../Actions/transactionActions';

const TransactionList = ({ transactions, updateIndex, deleteTransaction }) => {
  const handleEdit = (index) => {
    updateIndex(index);
  };

  const handleDelete = (idx) => {
    deleteTransaction(idx);
  };

  return (
    <div>
      <h2>Transaction List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Account Number</th>
            <th>FSC</th>
            <th>Name</th>
            <th>Amount</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((transaction, index) => (
            <tr key={index}>
              <td>{transaction.id}</td>
              <td>{transaction.accountNumber}</td>
              <td>{transaction.FSC}</td>
              <td>{transaction.name}</td>
              <td>{transaction.amount}</td>
              <td>
                <button onClick={() => handleEdit(index)}>Edit</button>
                <button onClick={() => handleDelete(transaction.idx)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    transactions: state.list,
  };
};

const mapDispatchToProps = {
  updateIndex,
  deleteTransaction,
};

export default connect(mapStateToProps, mapDispatchToProps)(TransactionList);
