import TableRows from "./TableRows"
import {useState} from "react";
import TestRunner from "./TestRunner";

function AddDeleteTableRows({testCase}) {

    const [rowsData, setRowsData] = useState([]);

    const addTableRows = () => {
        setRowsData([...rowsData, {}])
    }

    const deleteTableRows = (index) => {
        const rows = [...rowsData];
        rows.splice(index, 1);
        setRowsData(rows);
    }

    const handleChange = (index, evnt) => {

        const {name, value} = evnt.target;
        const rowsInput = [...rowsData];
        rowsInput[index][name] = value;
        setRowsData(rowsInput);


    }
    let setTestResult = (index, result) => {
        rowsData[index].status = result.status;
        rowsData[index].actualOutput = result.actualOutput;
        setRowsData([...rowsData]);
    };

    return (
        <div className="container">
            <h3>{testCase.name} Testsuite</h3>
            <div className="row">

                <table className="table">
                    <thead>
                    <tr>
                        {testCase.inputs.map(input => (<th>{input.name}</th>))}
                        <th>Expected Output</th>
                        <th>Actual Output</th>
                    </tr>
                    </thead>
                    <tbody>

                    <TableRows rowsData={rowsData} header={testCase.inputs} deleteTableRows={deleteTableRows} handleChange={handleChange}/>

                    </tbody>
                </table>

            </div>

            <div className="col-sm-4">
                <button className="btn btn-outline-success" onClick={addTableRows}>+</button>
            </div>
            <TestRunner testCase={testCase} inOutData={rowsData}
                        setTestResult={setTestResult}/>
        </div>
    )

}

export default AddDeleteTableRows