import React from 'react'

class CounterC extends React.Component {
    constructor() {
        super()
        this.count = 11;
        console.log(1, 'constructor')

    }
    handleClick = () => {
        // this.setState({count: this.state.count +1})
        this.count++
        console.log(this.count)
    }
    componentDidMount = () => {
        console.log(3, 'componentDidMount')
    }

    render(){
        return(
            <div>
            <h1>Counter</h1>
            <h2>{this.count}</h2>
            <button onClick={this.handleClick}>Add</button>
            </div>
        )
    }
}

export default CounterC