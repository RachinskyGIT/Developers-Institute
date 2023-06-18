export const changePropOne = (value) => {
  return {
    type:'PROP_ONE',
    payload: value
  }
}

export const changePropTwo = value => {
  return{
    type:'PROP_TWO'
  }
}

export const incrementCounter = () => {
  return {
    type:'INCREMENT_COUNTER'
  }
}

export const decrementCounter = () => {
  return {
    type:'DECREMENT_COUNTER'
  }
}
