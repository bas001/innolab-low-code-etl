import AddDeleteTableRows from "./components/AddDeleteTableRows";
import {useState} from "react";
import logo from './hat.png';


function App() {

    const [selectedFile, setSelectedFile] = useState();
    const [isFileSelected, setIsSelected] = useState(false);

    const changeHandler = (event) => {
        setSelectedFile(event.target.files[0]);
        setIsSelected(true);
    };

    return (
        <div>
            <nav className="navbar navbar-light bg-light">
                <a className="navbar-brand" href="#">
                    <img src={logo} width="60" height="70" className="d-inline-block align-top" alt="">
                        </img>
                    <h2  className="d-inline-block"  >Magic Rules Workbench</h2>
                </a>
            </nav>
            <div className="container">

                <input className="btn btn-outline-success"  type="file" name="file" onChange={changeHandler}/>
            </div>
            <AddDeleteTableRows code={selectedFile}/>
        </div>
    );
}

export default App;