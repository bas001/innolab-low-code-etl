import AddDeleteTableRows from "./AddDeleteTableRows";

function TestRunner({functions}) {

    return functions.map(fun => {
        return (
            <div>
                <AddDeleteTableRows funcAsString={fun.funcAsString} name={fun.name}/>
                <br/>
                <br/>
            </div>
        )
    });

}

export default TestRunner;