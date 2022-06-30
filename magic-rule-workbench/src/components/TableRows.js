function TableRows({rowsData, deleteTableRows, handleChange}) {


    function cssColor(status) {
        switch (status) {
            case 'green':
                return '#d2fac3'
            case 'yellow':
                return '#faf8b6'
            case 'red':
                return '#ff7177'
            default:
                return '#f5f4ed'
        }
    }

    return (

        rowsData.map((data, index) => {
            const {input1, input2, input3, input4, expectedOutput, actualOutput, status} = data;
            return (

                <tr key={index}>
                    <td><textarea value={input1} onChange={(evnt) => (handleChange(index, evnt))} name="input1"
                                  className="form-control" style={{resize: "both"}}/></td>
                    <td><textarea value={input2} onChange={(evnt) => (handleChange(index, evnt))} name="input2"
                                  className="form-control" style={{resize: "both"}}/></td>
                    <td><textarea value={input3} onChange={(evnt) => (handleChange(index, evnt))} name="input3"
                                  className="form-control" style={{resize: "both"}}/></td>
                    <td><textarea value={input4} onChange={(evnt) => (handleChange(index, evnt))} name="input4"
                                  className="form-control" style={{resize: "both"}}/></td>
                    <td><textarea value={expectedOutput} onChange={(evnt) => (handleChange(index, evnt))} name="expectedOutput"
                                  className="form-control" style={{resize: "both"}}/></td>
                    <td><textarea value={actualOutput} onChange={(evnt) => (handleChange(index, evnt))} name="actualOutput"
                                  disabled={true} style={{backgroundColor: cssColor(status), resize:"both"}} className="form-control"/></td>
                    <td>
                        <button className="btn btn-outline-danger" onClick={() => (deleteTableRows(index))}>x</button>
                    </td>
                </tr>

            )
        })

    )

}

export default TableRows;