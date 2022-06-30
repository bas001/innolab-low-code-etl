import React from 'react';
import _ from 'lodash';


function TestRunner(props) {

    function parse(input, type) {

        switch (type) {
            case "Number":
                return parseInt(input);
            case "String":
                return input;
            case "Object":
            case "Array":
                return JSON.parse(input)
            default:
        }

        let number = parseInt(input);
        if (!isNaN(number)) {
            return number;
        }

        try {
            return JSON.parse(input);
        } catch (i) {
        }

        return input;
    }

    function stringify(out) {
        if (
            typeof out === 'object' &&
            out !== null
        ) {
            return JSON.stringify(out)
        } else {
            return out;
        }
    }

    function testFunction(testCase, inOut) {
        let inputNames = testCase.inputs.map(input => input.name);
        let callableFunc = new Function(inputNames, testCase.funcAsString + ";return " + testCase.name + `(${inputNames})`);
        try {
            let out = callableFunc.apply(null, testCase.inputs.map(input => parse(inOut[input.name], input.type)));
            if (_.isEqual(out, parse(inOut.expectedOutput))) {
                return {status: 'green', actualOutput: stringify(out)}
            } else {
                return {status: 'yellow', actualOutput: stringify(out)}
            }
        } catch (ex) {
            return {status: 'red', actualOutput: ex}
        }

    }

    function run() {
        props.inOutData.forEach(async function (inOut, i) {
            let result = await testFunction(props.testCase, inOut);
            props.setTestResult(i, result)
        })
    }

    return (
        <div>
            <br/>
            <button className="btn-outline-success" style={{"width": "200px", "height": "50px"}} onClick={run}>
                Run Tests
            </button>
        </div>
    );
}

export default TestRunner;