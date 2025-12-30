/* 
    Write a function called `calculateArea` that takes two parameters: `length` and `width`. 
    The function should return the area of a rectangle (i.e., `length * width`). 
    Call the function with different values for `length` and `width`, and log the results. 
*/

function performArithmeticOperations() {
    const number1 = 10;
    const number2 = 5;

    const divisionResult = number1 / number2;

    console.log(`${number1} + ${number2} = ${number1 + number2}`);
    console.log(`${number1} - ${number2} = ${number1 - number2}`);
    console.log(`${number1} * ${number2} = ${number1 * number2}`);
    console.log(`${number1} / ${number2} = ${divisionResult}`);

    if (divisionResult > 10) {
        console.log("The result of division is greater than 10.")
    } else if (divisionResult < 10) {
        console.log("The result of division is less than 10.")
    } else {
        console.log("The result of division is equal to 10.")
    }
}

performArithmeticOperations();