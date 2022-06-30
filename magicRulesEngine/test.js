
    /*
    metainformation-start
    {
    "name": "Fullname",
    "inputs": [{"type": "String", "name": "client_id"},{"type": "String", "name": "sex"}],
    "outputs": [{"type": "String", "name": "sex"}]
    }
    metainformation-end
    */
    
    const Fullname = (client_id, sex) => {
        return [{['sex'] : client_id + ' ' + sex }]
    }


    // magic-rule ¯\_(ツ)_/¯
    /*
    metainformation-start
    {
    "name": "IfElseTest",
    "inputs": [{"type": "String", "name": "sex"}],
    "outputs": [{"type": "String", "name": "gender"}]
    }
    metainformation-end
    */
    
   const IfElseTest = (sex) => {
    if (sex === 'Male') {
        return [{['gender']: 'M'}]
    } else if (sex === 'Female') {
        return [{['gender']: 'F'}]
    } else if (sex === 'Divers') {
        return [{['gender']: 'D'}]
    } else {
        return [{['gender']: 'Unknown'}]
    }
}


    // magic-rule ¯\_(ツ)_/¯
    /*
    metainformation-start
    {
    "name": "SplitAdress",
    "inputs": [{"type": "String", "name": "address_1"}],
    "outputs": [{"type": "Number", "name": "housenumber"},{"type": "String", "name": "street"}]
    }
    metainformation-end
    */
    
   const SplitAdress = (address_1) => {
    const splittedInput = address_1.split(' ')
    const outputParamNames = ['housenumber', 'street']
    const output = []
    for (let i = 0; i < outputParamNames.length ; i++) {
        if (i == outputParamNames.length - 1) {
            output.push({[outputParamNames[i]] : splittedInput.slice(i).join(' ')})
        } else {
            output.push({[outputParamNames[i]] : splittedInput[i]})
        }
    }
    return output
}
   // magic-rule ¯\_(ツ)_/¯
    /*
    metainformation-start
    {
    "name": "GroupBy",
    "inputs": [{"type": "Array", "name": "testArray"}],
    "outputs": [{"type": "Object", "name": "testOutput"}]
    }
    metainformation-end
    */
    
   const GroupBy = (testArray) => {
    return [{ ['testOutput'] : [...new Set(testArray)].map(key => ({ [key]: testArray.filter(e => e === key).length }))}]
    }

// magic-rule ¯\_(ツ)_/¯
    /*
    metainformation-start
    {
    "name": "summation",
    "inputs": [{"type": "Array", "name": "summationInput"}],
    "outputs": [{"type": "Number", "name": "summationOutput"}]
    }
    metainformation-end
    */
    
   const summation = (summationInput) => {
    return [{ ['summationOutput'] : summationInput.reduce((accumulator, curr) => accumulator + curr, 0)}]
}

