import TestCase from "./TestCase";
import {useState} from "react";

function TestRunner({functions}) {

    const [result, setResult] = useState({});
    const [resultRender, setResultRender] = useState({});
    const reportResult = (report) => {
        result[report.name] = report.result
        const resultArr = Object.entries(result).map(([key, value]) => value.join())

        var countOfResult = resultArr.reduce((p, c) => {
            var name = c;
            if (!p.hasOwnProperty(name)) {
                p[name] = 0;
            }
            p[name]++;
            return p;
        }, {});
        setResultRender(countOfResult)
    };

    return (
        <div>
            <div className="container">
                <h2>Tests</h2>
            </div>
            <div className="container" align="right">
                {Object.keys(resultRender).length !== 0 ? <h3>Test Summary</h3> : <h3/>}
                {Object.entries(resultRender).map(([key, value]) => <div><span>{key}: {value}</span></div>)}
            </div>
            {functions.map(fun => {
                return (
                    <div>
                        <TestCase testCase={fun} reportResult={reportResult}/>
                        <br/>
                        <br/>
                    </div>
                )
            })}
        </div>);

}

export default TestRunner;