import AddDeleteTableRows from "./AddDeleteTableRows";

function TestRunner({functions}) {

    return functions.map(fun => {
        return (
            <div>
                <AddDeleteTableRows key={fun.name} testCase={fun}/>
                <br/>
                <br/>
            </div>
        )
    });

}

export default TestRunner;