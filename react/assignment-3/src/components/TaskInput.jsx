import { useRef } from "react";
import { ReactElement } from "react";

/**
 * Takes user input for task text. Triggers 'props.addTask' on submit.
 * 
 * @param {object} props 
 * @param {(text: message) => void} props.addTask
 * @returns {ReactElement}
 */
function TaskInput({ addTask }) {
    const inputTextElement = useRef(null);

    const onTextSubmitHandler = () => {
        const trimmedText = inputTextElement.current.value.trim();

        if (!trimmedText) {
            return;
        }

        addTask(trimmedText);
        inputTextElement.current.value = "";
    }

    return (
        <div>
            <input
                placeholder="New Task"
                ref={inputTextElement}
            />
            <button onClick={onTextSubmitHandler}>
                Add
            </button>
        </div>
    )
}

export default TaskInput;