import {useState} from "react";

function RuleEditor({onSave}) {

    const [rules, setRules] = useState('');

    function getTextareaStyle() {
        return {resize: "both", width: "300px", height: "500px"};
    }

    function postRules() {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'text/plain' },
            body: rules
        };
        fetch('http://localhost:5000/convert', requestOptions)
            .then(response => response.text())
            .then(data => onSave(data));
    }

    return (
        <div className="container">
            <h2>Rule Editor</h2>
            <textarea value={rules} name="ruleInput"
                      key="ruleInput"
                      className="form-control" style={getTextareaStyle()}/>
            <br/>
            <button className="btn btn-outline-success" onClick={postRules}>Save</button>
        </div>
    )


}

export default RuleEditor;