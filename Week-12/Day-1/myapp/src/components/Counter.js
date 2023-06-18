import {useState} from 'react';
import {connect, useSelector, useDispatch} from 'react-redux';
import {incrementCounter,decrementCounter} from '../redux/actions'

const Counter = (props) => {
  // const [count, setCount] = useState(0)
  const count = useSelector((state)=> state.count);
  const dispatch = useDispatch()
  return (
    <>
      <button onClick={()=>dispatch(incrementCounter())}> + </button>
      {count}
      <button onClick={()=>dispatch(decrementCounter())}> - </button>
    </>
  )
}
export default Counter;


// const mapStateToProps = state => {
//   return {
//     count: state.count
//   }
// }
// const mapDispatchToProps = dispatch => {
//   return {
//     handleIncrement: () => dispatch(incrementCounter()),
//     handleDecrement: () => dispatch(decrementCounter())
//   }
// }

// export default connect(mapStateToProps,mapDispatchToProps)(Counter)
