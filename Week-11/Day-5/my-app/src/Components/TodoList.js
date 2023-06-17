import React from 'react'


class TodoList extends React.Component{
  constructor(){
    super()

    this.state = {
      tasks:[],
      value: ''
    }
  }

  handleSubmit = (event) => {
    event.preventDefault()
    const newItem = {
      id: this.state.tasks.length,
      text: event.target.task.value
    }
    this.setState(prevState => ({
      tasks: [...prevState.tasks, newItem]
    }))
  }

  render(){
    return(
      <>
      <form onSubmit={this.handleSubmit}>
        Enter a new task: <input name='task'></input>
        <input type='submit' value='Add new task'></input>
      </form>
      {this.state.tasks.map((item) => (
         <div className='task' key={item.id}>
          {item.text}<br/>
          <button className='addtask' key={item.id} onClick={
            ()=>{
              const indexToRemove = this.state.tasks.findIndex(itemRem=>itemRem.id == item.id)
              this.state.tasks.splice(indexToRemove,1);
              this.setState({value:''});
            }
          }>
            Remove
          </button>
        </div>
      ))}
      </>
    )
  }
}




export default TodoList;