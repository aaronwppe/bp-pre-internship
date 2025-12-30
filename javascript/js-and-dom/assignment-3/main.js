/* 
    Write a function called `calculateArea` that takes two parameters: `length` and `width`. 
    The function should return the area of a rectangle (i.e., `length * width`). 
    Call the function with different values for `length` and `width`, and log the results. 
*/

function generateResults() {
    console.log("Rectangle");

    let length = 5, width = 2;
    console.log(`Length = ${length}; Width = ${width};  Area = ${calculateArea(length, width)}`);

    length = 20;
    width = 10;
    console.log(`Length = ${length}; Width = ${width};  Area = ${calculateArea(length, width)}`);
}

function calculateArea(length, width) {
    return length * width;
}

generateResults();