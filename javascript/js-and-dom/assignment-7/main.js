/* 
    Create a form with the following fields: 
        - Name (required) 
        - Email (required, should be a valid email) 
        - Age (optional, should be a number greater than 18) 

    On form submission, validate the following: 
        - The Name field should not be empty. 
        - The Email field should contain a valid email format. 
        - If the Age field is provided, it should be greater than 18. 

    Display error messages for each invalid field. 
    Prevent form submission if any of the fields are invalid. 
*/


function onFormSubmit(event) {
    const formElement = document.forms[0];

    const name = formElement.name.value;
    const email = formElement.email.value;
    const age = formElement.age.value;

    const nameErrorLabel = document.getElementById("nameErrorLabel");
    const emailErrorLabel = document.getElementById("emailErrorLabel");
    const ageErrorLabel = document.getElementById("ageErrorLabel");

    const nameErrorString = getNameValidationErrorString(name);
    const emailErrorString = getEmailValidationErrorString(email);
    const ageErrorString = getAgeValidationErrorString(age);

    nameErrorLabel.innerText = nameErrorString;
    emailErrorLabel.innerText = emailErrorString;
    ageErrorLabel.innerText = ageErrorString;

    if (nameErrorString || emailErrorString || ageErrorString) {
        event.preventDefault();
        return;
    }

    formElement.name.value = "";
    formElement.email.value = "";
    formElement.age.value = "";

    alert("Your form was submitted.");
}

function getNameValidationErrorString(name) {
    if (name.trim().length == 0) {
        return "Name empty!";
    }

    return "";
}

function getEmailValidationErrorString(email) {
    const trimmedEmail = email.trim();

    if (trimmedEmail.length == 0) {
        return "Email empty!";
    }

    const pattern = /^[a-zA-Z0-9_]+@[a-zA-z]+.[a-zA-Z]{2,}$/;

    if (!pattern.test(trimmedEmail)) {
        return "Invalid email!";
    }

    return "";
}

function getAgeValidationErrorString(age) {
    const trimmedAge = age.trim();

    if (trimmedAge.length == 0) {
        return "";
    }

    const ageInteger = parseInt(trimmedAge);

    if (Number.isNaN(ageInteger) || ageInteger < 0 || ageInteger > 150) {
        return "Invalid age!"
    }

    if (ageInteger <= 18) {
        return "Age must be above 18!"
    }

    return "";
}