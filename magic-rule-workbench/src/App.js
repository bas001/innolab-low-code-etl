import AddDeleteTableRows from "./components/AddDeleteTableRows";
import {useState} from "react";


function App() {

    const [selectedFile, setSelectedFile] = useState();
    const [isFileSelected, setIsSelected] = useState(false);

    const changeHandler = (event) => {
        setSelectedFile(event.target.files[0]);
        setIsSelected(true);
    };

    return (
        <div>
            <h2>Magic Rules Workbench</h2>
            <input type="file" name="file" onChange={changeHandler}/>
            <AddDeleteTableRows code={selectedFile}/>
        </div>
    );
}

export default App;