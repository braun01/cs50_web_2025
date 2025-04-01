function updateAnimation(animation) {
    console.log(animation);
    const div = document.getElementById("animate-me");

    if (div.classList.contains(animation) && animation !== "reset") {
        div.classList.remove(animation);
    }
    else {
        div.classList.remove(...div.classList);
        div.classList.add(animation);
    }
}

document.addEventListener("DOMContentLoaded", function() {
    console.log("hello");

    document.querySelectorAll("button").forEach(button => {
        button.onclick = function() {
            updateAnimation(this.dataset.animation);
        }
    })
});