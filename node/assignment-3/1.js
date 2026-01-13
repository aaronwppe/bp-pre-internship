class Calculator {
    constructor(start_num = 0) {
        this.accumulator = start_num;
    }

    add(num) {
        this.accumulator += num;
        return this;
    }

    subtract(num) {
        this.accumulator -= num;
        return this;
    }

    multiply(num) {
        this.accumulator *= num;
        return this;
    }

    divide(num) {
        if (num == 0) {
            throw Error("Cannot divide zero");
        }

        this.accumulator /= num;
        return this;
    }

    getResult() {
        return this.accumulator;
    }
}

const calc = new Calculator();

// method chaining
const result = calc.add(5)
    .subtract(2)
    .multiply(3)
    .divide(2)
    .getResult();

console.log(result);
