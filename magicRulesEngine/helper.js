function getMeta(jsonString) {
    const start = jsonString.indexOf("metainformation-start") + "metainformation-start".length
    const end = jsonString.indexOf("metainformation-end")
    const metaString = jsonString.substring(start, end)
    return JSON.parse(metaString);
}

function getInputParamValues(data, inputNames) {
    return inputNames.map(name => data[name])
}

function getParameters(funArray) {
    parameters=[]
    funArray.map(fun => {
        meta = getMeta(fun)
        meta.inputs.map(input => parameters.push(input.name))
    }) 
    return parameters
} 
function throwError(message) {
    process.on('exit', function (){
        console.error(message);
        process.exit()
      });
}

function validateInput(dataset, tableName, parameters) {
    if(dataset == undefined){
        helper.throwError("Table name '" + tableName + "' not found")
    }

    if(dataset.length == 0) {
        helper.throwError("Table name'" + tableName + "' is empty")
    }

    parameters.forEach(parameter => {
        if(dataset[0][parameter] == undefined){
            helper.throwError("Input parameter '" + parameter + "' not found in data!")
        }
    });
}

module.exports = {
     throwError,
    getMeta,
    validateInput,
    getInputParamValues,
    getParameters
}