import Sender from './components/Sender';
import './App.css';
import { useState, ReactElement } from 'react';
import Receiver from './components/Receiver';

/**
 * Implements sending and receiving messages between siblings.
 * 
 * @returns {ReactElement}
 */
function App() {
    const [message, setMessage] = useState("");

    return (
        <div className='app-container'>
            <Sender setMessage={setMessage} />
            <Receiver message={message} />
        </div>
    );
}

export default App;
