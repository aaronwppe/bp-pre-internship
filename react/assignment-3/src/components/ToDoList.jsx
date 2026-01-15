import { useState } from "react";
import TaskInput from "./TaskInput";
import Task from "./Task";
import { ReactElement } from "react";

/**
 * Displays a predefined set of tasks.
 * Allows user to add new tasks and delete existing tasks.
 * 
 * @returns {ReactElement}
 */
function ToDoList() {
    const [tasks, setTasks] = useState([
        {
            id: crypto.randomUUID(),
            text: "React assignments",
        },
        {
            id: crypto.randomUUID(),
            text: "Docker assignment",
        },
        {
            id: crypto.randomUUID(),
            text: "Express project",
        },
        {
            id: crypto.randomUUID(),
            text: "Deploy Express project",
        },
    ]);


    const addTask = (taskText) => {
        setTasks([
            ...tasks,
            {
                id: crypto.randomUUID(),
                text: taskText,
            }
        ]);
    };

    const onTaskChecked = (taskId) => {
        setTimeout(() => {
            setTasks(tasks.filter(task => task.id !== taskId));
        }, 100);
    };


    return (
        <>
            <TaskInput addTask={addTask} />
            <ol>
                {tasks.map(task => (
                    <Task
                        key={task.id}
                        text={task.text}
                        onChecked={() => onTaskChecked(task.id)}
                    />
                ))}
            </ol>
        </>
    )
}

export default ToDoList;