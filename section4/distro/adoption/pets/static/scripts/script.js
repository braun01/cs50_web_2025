// Get pet info onto the screen
function loadPets() {
    console.log("loading pets");
    // TODO: grab the appropriate element from index.html where you will add all the pet info
    
    
    // TODO: 
    // 1. hit your api to get available pets. Display their info on the screen.
    // 2. for each pet you get back, add the appropriate DOM elements. Be sure to set the dataset property for petId
    // 3. add an event listener to pull up specific pet info by id on click of the DOM element you added. 
    //      You may find it helpful to move some of this into a helper
    fetch("available")
    .then(response => response.json())
    .then(pets => {

    })
    .catch(error => console.log(error));
}

// Add an event listener to only run this logic once the page has loaded
document.addEventListener("DOMContentLoaded",  () => {
    loadPets();
});