import "./Receiver.css";
import { ReactElement } from 'react';

/**
 * Displays the 'props.message' property.
 * 
 * @param {object} props
 * @param {string} props.message
 * @returns {ReactElement}
 */
function Receiver({ message }) {
    return (
        <div className="receiver-container">
            <h2>Receiver</h2>
            {message}
        </div>
    );
}

export default Receiver;