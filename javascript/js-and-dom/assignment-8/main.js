/* 
    - Create an HTML page with a `<div>` that has a class `box` 
    (with a default background color like lightblue). 

    - Create a button labeled "Toggle Color". 

    - When the button is clicked, toggle the class `highlight` on the `<div>`, changing its background color 
    (e.g., change to red when the class is added and back to lightblue when removed). 

    - Use JavaScript to manipulate the class of the `<div>`. 
*/

let previousTextboxClass = null;

function toggleTextboxColor() {
    const highlightClass = "highlight";
    const bodyElement = document.getElementsByTagName("body")[0];
    const textboxDiv = document.getElementById("textbox");

    previousTextboxClass = previousTextboxClass ?? textboxDiv.className;

    if (textboxDiv.className == previousTextboxClass) {
        textboxDiv.className = highlightClass;
        bodyElement.className = previousTextboxClass;
    } else {
        textboxDiv.className = previousTextboxClass;
        bodyElement.className = highlightClass;
    }
}