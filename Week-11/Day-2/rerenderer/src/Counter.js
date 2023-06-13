import { useState, useEffect } from 'react';


const Counter = (props) => {
    // let count = 0;
    const [count, setCount] = useState(10)
    // const [state, setState]

    useEffect(()=>{
        console.log(count)
    // }, [name, props.count])
    }, [])

    const handleClick = () => {
        // count++
        // console.log(count);
        setCount(count+1)
    }
    return(
        <div>
        <h1>Counter</h1>
        <h2>{count}</h2>
        {/* <input type="text" onChange={(e)=>setName(e.target.value)}/> */}
        <button onClick={handleClick}>Add</button>
        </div>
    )
}

export default Counter