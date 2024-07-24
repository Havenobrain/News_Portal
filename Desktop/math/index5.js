
//Задание 5
const count = (x, n) => {
    let result = x 
    for (let i = 1; i < n; i++){
        result *= x;
    }
    return result;
}

const result = count(3, 5)
console.log(result)

