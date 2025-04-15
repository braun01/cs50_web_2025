const min = 1;
const max = 10000;


document.addEventListener("DOMContentLoaded", () => {

    const num = Math.floor(Math.random() * (max - min) + min);

    const guess_input = document.getElementById("guess");

    document.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            
            const feedback_div = document.getElementById("feedback");
            const guess = parseInt(guess_input.value);

            if (guess === num) {
                document.getElementById("guess_div").style.display = "none";
                feedback_div.style.display = "none";
                document.getElementById("won").style.display = "block";
                return;
            }

            guess_input.classList.add("wrong");
            guess_input.value = "";
            
            feedback_div.style.display = "block";

            let feedback = "Too High"
            if (guess < num) {
                feedback = "Too Low"
            }

            feedback_div.innerHTML = `<h3>${feedback}</h3>`;

        }
    })

    guess_input.onanimationend = () => {
        guess_input.classList.remove("wrong");
    }

})