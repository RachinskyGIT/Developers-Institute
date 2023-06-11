import './Hello.css'
import HelloClass from './HelloClass.js'
import robots from './Components/users.json' 

// console.log(robots[1].name)

const Hello = () => {
    const user = {
        name: 'Mary',
        email: 'kokoko@koko.com'
    }

    const users = [
        {
        name: 'Mary',
        email: 'kokoko@koko.com'
        },
        {
        name: 'John',
        email: '123@koko.com'
        },
        {
        name: 'Pasha',
        email: '0000@koko.com'
        },
    ]


    return (
        <div className = 'title'>
            <h1>
                Hello,
            </h1>
            <h2>
                {
                    robots.map(item => {
                        return (
                            <div key={item.id}> 
                                <img src={`https://robohash.org/${item.id}?size=150x150`} alt="logo" />
                                <h1>
                                    Hello, {item.name}
                                </h1>
                            </div>
                                )
                            }

                    )
                }
                </h2>
            <p>
                {user.email}
            </p>
                <HelloClass></HelloClass>
        </div>
    )

}

export default Hello