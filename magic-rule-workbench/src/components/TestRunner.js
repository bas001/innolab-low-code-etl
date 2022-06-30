import React from 'react';
import _ from 'lodash';


function TestRunner(props) {

    function parse(input) {
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

    function testFunction(funcAsString, test, name) {
        let callableFunc = new Function("in1", "in2", "in3", "in4", funcAsString + "return " + name + "(in1, in2, in3, in4)");
        try {
            let out = callableFunc.apply(null, [parse(test.input1), parse(test.input2), parse(test.input3), parse(test.input4)]);
            if (_.isEqual(out, parse(test.expectedOutput))) {
                return {status: 'green', actualOutput: stringify(out)}
            } else {
                return {status: 'yellow', actualOutput: stringify(out)}
            }
        } catch (ex) {
            return {status: 'red', actualOutput: ex}
        }

    }

    function run() {
        let tests = props.tests;
        tests.forEach(async function (test, i) {
            let result = await testFunction(props.funcAsString, test, props.name);
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