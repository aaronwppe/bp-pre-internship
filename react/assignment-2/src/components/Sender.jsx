import "./Sender.css";
import { ReactElement } from 'react';

/**
 * Contains an input tag. Tracks user input.
 * Updates parent of change via 'props.setMessage'.
 * 
 * @param {object} props 
 * @param {(message: string) => void} props.setMessage
 * @returns {ReactElement}
 */
function Sender({ setMessage }) {
    const onMessageChange = (event) => {
        setMessage(event.target.value);
    };

    return (
        <div className="sender-container">
            <h2>Sender</h2>
            <input
                placeholder="Message"
                onChange={onMessageChange}
            />
        </div>
    );
}

export default Sender;