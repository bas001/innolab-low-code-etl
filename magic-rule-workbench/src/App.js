import logo from './hat.png';
import TestEditor from "./components/TestEditor";
import {useState} from "react";
import TestCase from "./model";
import RuleEditor from "./components/RuleEditor";


function App() {

    const [functions, setFunctions] = useState([]);

    function parseFunctions(content) {
        const funArray = content.split('// magic-rule ¯\\_(ツ)_/¯');
        const functions = funArray.map(fun => {
            const start = fun.indexOf("metainformation-start") + "metainformation-start".length
            const end = fun.indexOf("metainformation-end")
            const metaString = fun.substring(start, end)
            const meta = JSON.parse(metaString);
            return new TestCase(meta.name, meta.inputs, meta.output, fun);
        })

        setFunctions(functions)
    }

    const changeHandler = async (event) => {
        const content = await event.target.files[0].text();
        parseFunctions(content);
    };

    return (
        <div>
            <nav className="navbar navbar-light bg-light">
                <a className="navbar-brand" href="#" style={{display: "-webkit-flex"}}>
                    <img src={logo} width="150" height="200" className="d-inline-block align-top" alt="">
                    </img>
                    <h2 style={{"display": "-webkit-flex", "alignItems": "center", "marginLeft": "20px"}}>Magic Rules Workbench</h2>
                </a>
            </nav>
            <br/>
            <div className="container">
                <h2>Import</h2>
                <input className="btn btn-outline-success" type="file" name="file" onChange={changeHandler}/>
            </div>
            <br/>
            <RuleEditor onSave={parseFunctions}/>
            <br/>
            <TestEditor functions={functions}/>
        </div>
    );
}

export default App;