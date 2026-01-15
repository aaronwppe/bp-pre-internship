import { ReactElement } from "react";

/**
 * Displays 'props.text' and triggers 'props.onChecked' when checkbox is toggled.
 * 
 * @param {object} props 
 * @param {string} props.text 
 * @param {() => void} props.onChecked
 * @returns {ReactElement}
 */
function Task({ text, onChecked }) {
    return (
        <li>
            <input
                type="checkbox"
                onChange={onChecked}
            />
            {text}
        </li>
    );
}

export default Task;