import React from 'react'


class AppForm extends React.Component {
    constructor() {
        super();
        this.state = {
            firstname:'',
            lastname:'',
            color:'',
            isgo:''
        }
    }
}



handleSubmit = (e) => {
    e.preventDefault()
    const {firstname, lastname, color, isgo} = this.state;
}

handleChange = (e) => {
    console.log(e.target.value);
    const value = (e.target.type === 'checkbox') ? e.target.checked : e.target.value;
    this.setState({[e.target.name]:e.target.value})    
    // this.setState({firstname:e.target.value})
}
render(){
    return(
    <>
        <h1>My Form</h1>
        <form onSubmit={this.handleSubmit}>
            First Name: <input type="text" name="firstname" onChange={this.handleChange}/> <br/>
            Last Name: <input type="text" name="lastname" onChange={this.handleChange}/> <br/>

            <select name="color">
                <option value="1">Red</option>
                <option value="2">Blue</option>
                <option value="3">Green</option>
            </select>
            <br/>
            
            Is Going: <input type="checkbox" name="isgo" />

            <br/>
        </form>
    
    
    
    </>
    )
}