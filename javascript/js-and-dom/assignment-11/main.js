/* 
    - Create a countdown timer that starts from 10 seconds. 
    - Display the remaining time on the page (using a `<p>` or `<span>` element). 
    - Once the timer reaches 0, display a message saying "Time's up!". 
*/

let timeRemaining = 0;
let currentIntervalId = null;

function startTimer() {
    timeRemaining = 10;

    if (currentIntervalId) {
        clearInterval(currentIntervalId);
    }

    currentIntervalId = setInterval(runAtInterval, 1000);
}

function runAtInterval() {
    const textboxElement = document.getElementById("textbox");

    if (timeRemaining < 0) {
        textboxElement.innerText = "Time's up!";
        clearInterval(currentIntervalId);
        return;
    }

    textboxElement.innerText = timeRemaining;
    timeRemaining -= 1;
}