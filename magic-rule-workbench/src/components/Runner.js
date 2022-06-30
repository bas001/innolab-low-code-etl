import React from 'react';


function Runner(props) {

    async function loadScript(file, test) {
        var exec = await file.text();

        let func = new Function("in1", exec + "return asdf(in1)");
        let out = func.apply(null, [test.input1, test.input2, test.input3, test.input4]);
        if (out !== test.expectedOutput) {
            return {status: 'red', actualOutput: out}
        } else {
            return {status: 'green', actualOutput: out}
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
            <button className="btn-outline-success" style={{"width": "200px", "height":"50px"}} onClick={run}>
                Run Test
            </button>
        </div>
    );
}

export default Runner;