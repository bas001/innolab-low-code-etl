function TableRows({rowsData, header, deleteTableRows, handleChange}) {


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

    function getTextareaStyle() {
        return {resize: "both", width: "150px", height: "200px"};
    }

    return (

        rowsData.map((data, index) => {
            const {expectedOutput, actualOutput, status} = data;
            return (
                <tr key={index}>
                    {header.map(h => h.name).map(h => (<td><textarea value={data[h]} onChange={(evnt) => (handleChange(index, evnt))} name={h}
                                                    className="form-control" style={getTextareaStyle()}/></td>))}
                    <td><textarea value={expectedOutput} onChange={(evnt) => (handleChange(index, evnt))} name="expectedOutput"
                                  className="form-control" style={getTextareaStyle()}/></td>
                    <td><textarea value={actualOutput} onChange={(evnt) => (handleChange(index, evnt))} name="actualOutput"
                                  disabled={true} style={{backgroundColor: cssColor(status), ...getTextareaStyle()}} className="form-control"/></td>
                    <td>
                        <button className="btn btn-outline-danger" onClick={() => (deleteTableRows(index))}>x</button>
                    </td>
                </tr>

            )
        })

    )

}

export default TableRows;