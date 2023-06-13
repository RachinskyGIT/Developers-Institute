import Reqct from 'react'
import User from './User';


class UsersListC extends React.Componentmponent {
    constructor(){
        super();
        this.state = {
            arr:[]
        }
    }
    handleclick = () => {
        // console.log('hi');
        fetch('./users.json')
        .then(res => res.json())
        .then(data => {
            console.log(data);
            this.setState({arr:data})
        })
        .catch(err => {
            console.log(err);
        })
    }
    
    componentDidMount = () => {
        this.handleclick()
    }
    render(){
        return(
            <div>
            <button onClick={this.handleClick}>Get Users</button>
            {
                arr.map(item => {
                    return <User userinfo={item} key={item.id}/>
                })
            }
            </div>
        )
    }
}

export default UsersListC