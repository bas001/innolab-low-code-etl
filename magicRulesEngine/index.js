const { program } = require('commander');
const fs = require('fs');
const helper = require('./helper.js')


program
  .requiredOption('-t, --table [string]', 'exported table')
  .requiredOption('-f, --jsFile [js]', 'js file with functions')
  .requiredOption('-i, --inputFile [json]', 'input json file')
  .requiredOption('-o, --outputFile [json]', 'output json file');

program.parse(process.argv);
const opts = program.opts()
tableName = opts.table


let content = fs.readFileSync('./' + opts.jsFile, {encoding: 'utf8'});
const funArray = content.split('// magic-rule ¯\\_(ツ)_/¯');
let jsonData = require('./' + opts.inputFile);


helper.validateInput(jsonData[tableName], tableName, helper.getParameters(funArray))

const result=[]
for(let dataIndex = 0; dataIndex < jsonData[tableName].length; dataIndex++ ) {
    const test={}
    const functions = funArray.map(fun => {
        meta = helper.getMeta(fun)
        
    
        inputNames= meta.inputs.map(input => input.name)
        outputNames= meta.outputs.map(output => output.name)

        let callableFunc = new Function(inputNames, fun + "return " + meta.name + `(${inputNames})`);
        data = jsonData[tableName][dataIndex]
       
        const outputs = callableFunc.apply(null, helper.getInputParamValues(data, inputNames))
       
        for(let i = 0; i < outputs.length; i++) {
            outputName = outputNames[i]
            test[outputName]= outputs[i][outputName] 
        }
     })
     
    result.push(test)
}


fs.writeFileSync(opts.outputFile, JSON.stringify(result, null, 2))



