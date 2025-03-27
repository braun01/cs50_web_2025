function showPetInfo(petId) {
    // open whatever element on the html will exist, and then put the info in
    console.log("clicked on ", petId);
    divElem = document.getElementById("pet_info");

    fetch(`info/${petId}`)
    .then(response => response.json())
    .then(pet => {
        pet = pet.pet
        divElem.innerHTML= `
            <div>
                <h4>${pet.name}</h4>
                <div>
                    <p>Species: ${pet.species}</p>
                    <p>Age: ${pet.age + pet.age_unit}</p>
                    <p>Gender: ${pet.gender}</p>
                </div>
                <div>
                    <p>${pet.description}<p>

                </div>
            </div>
        `;
        console.log(divElem.innerHTML)
    })
    .catch(error => console.log(error));
}

// Get pet info onto the screen
function loadPets() {
    console.log("loading pets");
    // TODO: grab the appropriate element from index.html where you will add all the pet info
    availablePetsHtml = document.getElementById("available_card_div");
    
    // TODO: 
    // 1. hit your api to get available pets. Display their info on the screen.
    // 2. for each pet you get back, add the appropriate DOM elements. Be sure to set the dataset property for petId
    // 3. add an event listener to pull up specific pet info by id on click of the DOM element you added. 
    //      You may find it helpful to move some of this into a helper
    fetch("available")
    .then(response => response.json())
    .then(pets => {
        pets = pets.pets

        pets.forEach(pet => {
            // create our divs etc
            const card = document.createElement("div");
            card.classList.add("card");

            // set the html the user will see
            // Sneak peek: this is gross! React will make it nicer :)
            card.innerHTML = 
            `<div class="card-body">
                <h5 class="card-title">${pet.name}</h5>
                <p class="card-text">${pet.species}, ${pet.age}${pet.age_unit}</p>
            </div>`

            // set the data-ETC property so we can leverage it in the UI
            card.dataset.petId = pet.id;

            // add an event listener to pull up specific pet info by id on click
            // note that arrow functions do not have their own 'this' context. If you want to use an arrow function, 
            // pass in e which will be an object representing the event. Then you determine the correct target
            card.addEventListener("click", function() {
                // unhighlight any other element
                document.querySelectorAll(".card").forEach(item => {
                    if (!item.isEqualNode(this)) {
                        item.style.backgroundColor = "";
                    }
                });

                this.style.backgroundColor = "lightblue";

                showPetInfo(this.dataset.petId);
            });

            availablePetsHtml.append(card);
        });
    })
    .catch(error => console.log(error));
}

// Add an event listener to only run this logic once the page has loaded
document.addEventListener("DOMContentLoaded",  () => {
    loadPets();
});