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
  
  export const deleteTransaction = (id) => {
    return {
      type: 'DELETE',
      payload: id,
    };
  };
  
  export const updateIndex = (index) => {
    return {
      type: 'UPDATE-INDEX',
      payload: index,
    };
  };
  