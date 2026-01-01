/* 
    Create an HTML page with a `<p>` element with some text. 

    Create two buttons: 
        - One that changes the text color of the `<p>` to blue. 
        - Another that changes the text color of the `<p>` to red. 

    Use JavaScript to modify the inline styles of the `<p>` element. 
*/

function changeTextboxTextColor(element, color) {
    const buttons = document.getElementsByName("textColorButton");
    const textboxElement = document.getElementById("textbox");

    for (let b of buttons) {
        b.disabled = false;
    }

    textboxElement.style.color = color;
    element.disabled = true;
}   