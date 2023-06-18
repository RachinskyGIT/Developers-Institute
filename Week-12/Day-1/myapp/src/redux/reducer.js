const initState = {
  property_one:'Hello from Store 111',
  property_two: 'hey',
  count: 100,
}


export const reducer = (state = initState, action={}) => {
  switch (action.type) {
    case 'PROP_ONE':
      return {...state, property_one:action.payload}
    case 'INCREMENT_COUNTER':
      console.log('INCREMENT_COUNTER');
      return {...state, count: state.count + 1}
    case 'DECREMENT_COUNTER':
      console.log('DECREMENT_COUNTER');
      return {...state, count: state.count - 1}
    default:
      return {...state}
  }
}
