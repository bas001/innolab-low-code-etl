class TestCase {
    constructor(name, inputs, output, funcAsString) {
        this._name = name;
        this._inputs = inputs;
        this._output = output;
        this._funcAsString = funcAsString;
    }

    get name() {
        return this._name;
    }

    get inputs() {
        return this._inputs;
    }

    get output() {
        return this._output;
    }

    get funcAsString() {
        return this._funcAsString;
    }
}

export default TestCase