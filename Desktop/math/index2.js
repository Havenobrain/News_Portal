const isPrime = (number) => {
    if (number <= 1 || number > 1000) {
        console.log("Данные неверны");
        return;
    }

    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime) {
        console.log(number + " - простое число");
    } else {
        console.log(number + " - не простое число");
    }
};


isPrime(0);  
isPrime(1); 
isPrime(2);  
isPrime(17); 
isPrime(25); 
isPrime(1001);