const textarea = document.getElementById("writer");
const countdownDisplay = document.getElementById("countdown");

let timer;
let timeLeft = 5;

function resetTimer() {
    clearInterval(timer);
    timeLeft = 5;
    countdownDisplay.textContent = timeLeft;

    timer = setInterval(() => {
        timeLeft--;
        countdownDisplay.textContent = timeLeft;
        if (timeLeft === 0) {
            textarea.value = "";
            clearInterval(timer);
        }
    }, 1000);
}

textarea.addEventListener("input", resetTimer);