//Задание 3
const createAdder = (x) => {
    return (y) => {
        return x + y;
    };
};

const adder = createAdder(7);

console.log(adder(30)); 