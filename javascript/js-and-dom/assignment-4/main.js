/* 
    Create an array of 10 random integers between 1 and 100. 

    Write a function that: 
        - Finds and logs the largest number in the array. 
        - Finds and logs the smallest number in the array. 
        - Calculates and logs the average of the numbers in the array. 
*/

// References:
// - https://www.w3schools.com/jsref/jsref_random.asp
// - https://www.geeksforgeeks.org/javascript/how-to-create-an-array-with-random-values-with-the-help-of-javascript/


function generateResults() {
    const generateInteger = () => Math.floor((Math.random() * 100) + 1);
    const nums = Array.from({ length: 10 }, generateInteger);

    let minElement = Infinity;
    let maxElement = -Infinity;
    let sum = 0;

    for (let element of nums) {
        sum += element;

        if (maxElement < element) {
            maxElement = element;
        }

        if (minElement > element) {
            minElement = element;
        }
    }

    console.log(`Random Array: ${nums}`);
    console.log(`Max = ${maxElement}`);
    console.log(`Min = ${minElement}`);
    console.log(`Average = ${sum / nums.length}`);
}

generateResults();