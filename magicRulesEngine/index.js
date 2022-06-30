tableName= 's_client'
functionCall='Fullname'

parameters=['sex', 'day', 'month', 'age']

let jsonData = require('./input_small.json');

function throwError(message) {
    process.on('exit', function (){
        console.error(message);
        process.exit()
      });
}


if(jsonData[tableName] == undefined){
    throwError("Table name '" + tableName + "' not found")
}

if(jsonData[tableName].length == 0) {
    throwError("Table name'" + tableName + "' is empty")
}

parameters.forEach(parameter => {
    if(jsonData[tableName][0][parameter] == undefined){
        throwError("Input parameter '" + parameter + "' not found in data!")
    }
});


const fs = require('fs');
let content = fs.readFileSync('./test.js', {encoding: 'utf8'});


function getMeta(jsonString) {
    const start = jsonString.indexOf("metainformation-start") + "metainformation-start".length
    const end = jsonString.indexOf("metainformation-end")
    const metaString = jsonString.substring(start, end)
    return JSON.parse(metaString);
}

function getInputParamValues(data, inputNames) {
    return inputNames.map(name => data[name])
}

const funArray = content.split('// magic-rule ¯\\_(ツ)_/¯');
const result=[]
for(let dataIndex = 0; dataIndex < jsonData[tableName].length; dataIndex++ ) {
    const test={}
    const functions = funArray.map(fun => {
        meta = getMeta(fun)
        
    
        inputNames= meta.inputs.map(input => input.name)
        outputNames= meta.outputs.map(output => output.name)

        let callableFunc = new Function(inputNames, fun + "return " + meta.name + `(${inputNames})`);
        data = jsonData[tableName][dataIndex]
       
        const outputs = callableFunc.apply(null, getInputParamValues(data, inputNames))
       
        for(let i = 0; i < outputs.length; i++) {
            outputName = outputNames[i]
            test[outputName]= outputs[i][outputName] 
        }
     })
     
    result.push(test)
}


fs.writeFileSync("output.json", JSON.stringify(result, null, 2))



