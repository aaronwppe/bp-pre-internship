import { useState, ReactElement } from "react";
import "./counter.css";

/**
 * Contains a button. 
 * When clicked increments the counters state - starting from 0.
 * 
 * @returns {ReactElement}
 */
function Counter() {
    const [count, setCount] = useState(0);
    const onIncrement = () => {
        setCount(count + 1);
    };

    return <div className="counter">
        {count}
        <button onClick={onIncrement}>Increment</button>
    </div>;
}

export default Counter;