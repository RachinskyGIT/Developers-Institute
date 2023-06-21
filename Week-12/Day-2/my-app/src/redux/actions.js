export const INSERT = 'INSERT';
export const UPDATE = 'UPDATE';
export const DELETE = 'DELETE';
export const UPDATE_INDEX = 'UPDATE_INDEX';

//trx - short name for transaction
export const insert_trx = (trx) => {
    return{
      type: 'INSERT',
      payload: trx
    }
}

export const update_trx = (trx) => {
    return{
      type: 'UPDATE',
      payload: trx   
    }
}

export const delete_trx = (indx) => {
    return{
      type: 'DELETE',
      payload: indx
    }
}

export const update_indx = (indx) => {
    return{
      type: 'UPDATE_INDEX',
      payload: indx
    }
}