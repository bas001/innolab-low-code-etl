import TableRows from "./TableRows"
import {useState} from "react";
import Runner from "./Runner";

function AddDeleteTableRows(props) {


    const [rowsData, setRowsData] = useState([]);

    const addTableRows = () => {

        const rowsInput = {
            input1: '',
            input2: '',
            input3: '',
            input4: '',
            expectedOutput: ''
        }
        setRowsData([...rowsData, rowsInput])

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
            <div className="row">
                <div className="col-sm-8">

                    <table className="table">
                        <thead>
                        <tr>
                            <th>Input 1</th>
                            <th>Input 2</th>
                            <th>Input 3</th>
                            <th>Input 4</th>
                            <th>Expected Output</th>
                            <th>Actual Output</th>
                        </tr>
                        </thead>
                        <tbody>

                        <TableRows rowsData={rowsData} deleteTableRows={deleteTableRows} handleChange={handleChange}/>

                        </tbody>
                    </table>
                    <button className="btn btn-outline-success" onClick={addTableRows}>+</button>

                </div>
                <div className="col-sm-4">

                </div>
            </div>
            <Runner code={props.code} tests={rowsData} setTestResult={setTestResult}/>
        </div>
    )

}

export default AddDeleteTableRows