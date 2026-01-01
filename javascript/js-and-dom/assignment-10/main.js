/* 
    - Create an image element on the page. 
    - Create a button labeled "Change Image". 
    - When the button is clicked, change the `src` attribute of the image to a different image URL. 
    - Bonus : Change the button's text to "Image Changed" after the click. 
*/

// References:
// - https://stackoverflow.com/questions/511761/js-function-to-get-filename-from-url

const IMAGE_FOLDER = "images/"
const IMAGES = ["1.jpg", "2.jpg", "3.jpg"]

function changeImage() {
    const imageElement = document.getElementById("image");

    const currentImageUrl = new URL(imageElement.src);
    const currentFileName = currentImageUrl.pathname.split("/").pop()

    const currentFileIndex = IMAGES.indexOf(currentFileName);
    let newFileIndex = 0;

    if (currentFileIndex !== -1) {
        newFileIndex = (currentFileIndex + 1) % IMAGES.length;
    }

    imageElement.src = `images/${IMAGES[newFileIndex]}`;
    document.getElementById("button").innerText = "Image Changed";
}   