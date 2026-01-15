import { useRef } from 'react';
import { ReactElement } from "react";

/**
 * Displays textbox and a button. When button is clicked, the cursor focuses on the textbox.
 * 
 * @returns {ReactElement}
 */
function App() {
  const textInput = useRef(null);
  const onClickHandler = () => {
    textInput.current.focus();
  };

  return (
    <div>
      <input ref={textInput} />

      <button onClick={onClickHandler}>Click</button>
    </div>
  )
}

export default App;
