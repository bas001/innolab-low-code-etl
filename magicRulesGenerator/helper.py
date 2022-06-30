from model import Parameter

def getInputParams(params:[Parameter]):
    return list(filter(lambda param :  not param.output, params))

def getOutputParams(params:[Parameter]):
    return list(filter(lambda param :  param.output, params))

def getInputParamsName(params:[Parameter]):
    return list(map(lambda x: x.paramName, getInputParams(params)))

def getOutputParamsName(params:[Parameter]):
    return list(map(lambda x: x.paramName, getOutputParams(params)))

def paramsToString(params:[Parameter]):
    return ', '.join(params)

def concatParams(params:[Parameter], delimiter):
    concatString = " + " + delimiter + " + "
    return concatString.join(params)

def extractDelimiter(optionString):
    if 'delimiter' in optionString:
        return optionString[optionString.index("'"):optionString.rindex("'")+1]
    else:
        return "' '"
