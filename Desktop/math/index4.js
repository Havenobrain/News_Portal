//Задание 4
const printNumbers = (start, end) => {
    let currentNumber = start;

    const intervalId = setInterval(() => {
        console.log(currentNumber);
        currentNumber++;

        if (currentNumber > end) {
            clearInterval(intervalId);
        }
    }, 1000);
}

printNumbers(5, 15);