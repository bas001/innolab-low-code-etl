import logo from './hat.png';
import TestEditor from "./components/TestEditor";
import {useState} from "react";


function App() {

    const [functions, setFunctions] = useState([]);

    const changeHandler = async (event) => {
        const content = await event.target.files[0].text();

        var a = content.split('// magic-rule ¯\\_(ツ)_/¯')
        var funcs = a.map(x => {
            return {name: x.substring(0, x.indexOf('=')).replaceAll("const", "").trim(), funcAsString: x.replaceAll("\\n", "")}
        })

        setFunctions(funcs)
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