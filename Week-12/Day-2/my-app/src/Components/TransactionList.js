import React from 'react';
import { connect } from 'react-redux';
import { updateIndex, deleteTransaction } from '../Actions/transactionActions';

const TransactionList = ({ transactions, updateIndex, deleteTransaction }) => {
  const handleEdit = (index) => {
    updateIndex(index);
  };

  const handleDelete = (id) => {
    deleteTransaction(id);
  };

  return (
    <div>
      <h2>Transaction List</h2>
      <table>
        <thead>
          <tr>
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
              <td>{transaction.accountNumber}</td>
              <td>{transaction.FSC}</td>
              <td>{transaction.name}</td>
              <td>{transaction.amount}</td>
              <td>
                <button onClick={() => handleEdit(index)}>Edit</button>
                <button onClick={() => handleDelete(transaction.id)}>Delete</button>
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
