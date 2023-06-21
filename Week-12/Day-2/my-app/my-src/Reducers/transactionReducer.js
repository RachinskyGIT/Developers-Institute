const initialState = {
    currentIndex: -1,
    list: JSON.parse(localStorage.getItem('transactions')) || [],
  };
  
  const transactionReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'INSERT':
        const newTransaction = { ...action.payload, idx: Date.now() };
        const updatedList = [...state.list, newTransaction];
        localStorage.setItem('transactions', JSON.stringify(updatedList));
        return { ...state, list: updatedList };
  
      case 'UPDATE':
        const updatedTransaction = { ...action.payload.transaction, idx: state.list[action.payload.index].idx };
        const updatedList2 = [...state.list];
        updatedList2[action.payload.index] = updatedTransaction;
        localStorage.setItem('transactions', JSON.stringify(updatedList2));
        return { ...state, list: updatedList2 };
  
      case 'DELETE':
        const filteredList = state.list.filter((transaction) => transaction.idx !== action.payload);
        localStorage.setItem('transactions', JSON.stringify(filteredList));
        return { ...state, list: filteredList };
  
      case 'UPDATE-INDEX':
        return { ...state, currentIndex: action.payload };
  
      default:
        return state;
    }
  };
  
  export default transactionReducer;
  