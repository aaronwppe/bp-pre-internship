/* 
    Create a button labeled "Show Modal". 
    When the button is clicked, display a hidden modal (`<div>`) on the page. 
    The modal should contain a message and a "Close" button. 
    When the "Close" button is clicked, hide the modal again. 
*/

function showModal() {
    document.getElementById("modal").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}