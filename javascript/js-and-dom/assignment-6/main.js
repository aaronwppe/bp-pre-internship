/* 
    - Create a webpage that includes a button labeled "Add Item". 

    - When the button is clicked, dynamically create a new list item (`<li>`) 
      and append it to an existing unordered list (`<ul>`). 

    - The new list item should contain the text "Item X" 
      where X is the number of items currently in the list (e.g., "Item 1", "Item 2" etc.). 
*/

// References:
// - https://stackoverflow.com/questions/20040825/check-how-many-li-there-are-in-a-ul-with-javascript
// - https://www.w3schools.com/jsref/dom_obj_htmlcollection.asp


function onAddItemButtonClick() {
    const listElement = document.getElementById("list");
    const currentListLength = listElement.getElementsByTagName("li").length;

    listElement.innerHTML += `
        <li>Item ${currentListLength + 1}</li>
    `;
}

function onPopItemButtonClick() {
    const listElement = document.getElementById("list");
    const itemsElement = listElement.getElementsByTagName("li");
    const lastItemElement = itemsElement.item(itemsElement.length - 1);

    if (!lastItemElement) {
        return;
    }

    lastItemElement.remove();
}