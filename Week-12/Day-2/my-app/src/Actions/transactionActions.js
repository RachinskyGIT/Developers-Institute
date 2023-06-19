export const insertTransaction = (transaction) => {
    return {
      type: 'INSERT',
      payload: transaction,
    };
  };
  
  export const updateTransaction = (index, transaction) => {
    return {
      type: 'UPDATE',
      payload: { index, transaction },
    };
  };
  
  export const deleteTransaction = (idx) => {
    return {
      type: 'DELETE',
      payload: idx,
    };
  };
  
  export const updateIndex = (index) => {
    return {
      type: 'UPDATE-INDEX',
      payload: index,
    };
  };
  