import React from 'react';
import _ from 'lodash';


function Runner(props) {

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

    async function loadScript(file, test) {
        var exec = await file.text();
        let func = new Function("in1", "in2", "in3", "in4", exec + "return " + file.name.replace(".js", "") + "(in1, in2, in3, in4)");
        try {
            let out = func.apply(null, [parse(test.input1), parse(test.input2), parse(test.input3), parse(test.input4)]);
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

        let changedTests = props.tests;
        changedTests.forEach(async function (test, i) {
            let result = await loadScript(props.code, test);
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

export default Runner;