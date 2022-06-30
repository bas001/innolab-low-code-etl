import logo from './hat.png';
import TestEditor from "./components/TestEditor";
import {useState} from "react";
import TestCase from "./model";


function App() {

    const [functions, setFunctions] = useState([]);

    const changeHandler = async (event) => {
        const content = await event.target.files[0].text();

        const funArray = content.split('// magic-rule ¯\\_(ツ)_/¯');
        const functions = funArray.map(fun => {
            const start = fun.indexOf("metainformation-start") + "metainformation-start".length
            const end = fun.indexOf("metainformation-end")
            const metaString = fun.substring(start, end)
            const meta = JSON.parse(metaString);
            return new TestCase(meta.name, meta.inputs, meta.output, fun);
        })

        setFunctions(functions)
    };

    return (
        <div>
            <nav className="navbar navbar-light bg-light">
                <a className="navbar-brand" href="#">
                    <img src={logo} width="60" height="70" className="d-inline-block align-top" alt="">
                    </img>
                    <h2 className="d-inline-block">Magic Rules Workbench</h2>
                </a>
            </nav>
            <br/>
            <div className="container">
                <input className="btn btn-outline-success" type="file" name="file" onChange={changeHandler}/>
            </div>
            <br/>
            <TestEditor functions={functions}/>
        </div>
    );
}

export default App;