/* 
    Declare the following variables: 
        - A string containing your name. 
        - A number representing your age. 
        - A boolean indicating whether you are a student or not. 
        - An array of your favorite hobbies. 
        - An object containing your name, age, and hobbies. 

    Log each variable to the console with a description of what it holds. 
*/

function declareVariables() {
    const name = "Aaron";
    const age = 22;
    const isStudent = true;
    const hobbies = ["Singing", "Reading"];

    console.log(`Name <${typeof name}>: ${name}`);
    console.log(`Age <${typeof age}>: ${age}`);
    console.log(`Is a Student <${typeof isStudent}>: ${isStudent}`);
    console.log(`Hobbies <${typeof hobbies}>: [${hobbies}]`);

    const person = { name, age, hobbies };
    console.log(`Person <${typeof person}>: ${person.name, person.age, [person.hobbies]}`);
}

declareVariables();