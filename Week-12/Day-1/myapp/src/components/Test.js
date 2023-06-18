import { connect } from 'react-redux';
import { changePropOne } from '../redux/actions';

const Test = (props) => {
  return (
    <>
      <h1>{props.b} {props.c}</h1>
      <button onClick={() => props.changePropOne('Test Title')}>
        Change Title
      </button>

      <div>
        <button onClick={props.changePropOne}>Change Prop One</button>
      </div>
    </>
  );
};

const mapStateToProps = state => {
  return {
    b: state.property_two.toString(), // Преобразуйте в строку, если не является строкой
    c: state.property_one.toString() // Преобразуйте в строку, если не является строкой
  };
};

const mapDispatchToProps = dispatch => {
  return {
    changePropOne: (title) => dispatch(changePropOne(title))
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Test);
