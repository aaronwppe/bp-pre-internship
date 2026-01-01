/* 
    Create an HTML file with a `<div>` that has the text "Hello, World!". 
    Create a button that, when clicked, changes the text of the `<div>` to: "You clicked the button!". 
    Use JavaScript to attach an event listener to the button that triggers the text change. 
*/

// References:
// - https://stackoverflow.com/questions/3847121/how-can-i-disable-all-settimeout-events


let globalState = {
    previousTextboxColor: null,
    previousTextboxText: null,
    previousTimeout: null,
    buttonClickCount: 0,
}


function onButtonClicked() {
    const clickedText = "You clicked the button!";
    const clickedColor = "yellow";
    const textboxElement = document.getElementById("textbox");

    globalState.buttonClickCount += 1;

    globalState.previousTextboxText = globalState.previousTextboxText ?? textboxElement.textContent;
    globalState.previousTextboxColor = globalState.previousTextboxColor ?? textboxElement.style.backgroundColor;

    setTextbox(clickedText, clickedColor);

    if (globalState.buttonClickCount > 1) {
        textboxElement.textContent += ` (x${globalState.buttonClickCount})`;
    }

    if (globalState.previousTimeout) {
        clearTimeout(globalState.previousTimeout);
    }

    globalState.previousTimeout = setTimeout(onButtonClickedTimeout, 3000);
}

function setTextbox(text, backgroundColor) {
    const textboxElement = document.getElementById("textbox");
    textboxElement.textContent = text;
    textboxElement.style.backgroundColor = backgroundColor;
}

function onButtonClickedTimeout() {
    setTextbox(globalState.previousTextboxText, globalState.previousTextboxColor);
    globalState.buttonClickCount = 0;
}