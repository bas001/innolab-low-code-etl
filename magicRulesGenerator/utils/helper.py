from model import Parameter
from model import IfElseRule

def getInputParams(params:[Parameter]):
    return list(filter(lambda param :  not param.output, params))

def getOutputParams(params:[Parameter]):
    return list(filter(lambda param :  param.output, params))

def getInputParamsName(params:[Parameter]):
    return list(map(lambda x: x.paramName, getInputParams(params)))

def getOutputParamsName(params:[Parameter]):
    return list(map(lambda x: x.paramName, getOutputParams(params)))

def getIfElseConditions(rules:[IfElseRule]):
    return list(map(lambda x: x.condition, rules))

def getIfElseReturnValues(rules:[IfElseRule]):
    return list(map(lambda x: x.returnValue, rules))

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

def extractIfElseNoMatch(optionString):
    if 'no-match' in optionString:
        return optionString[optionString.index("'"):optionString.rindex("'")+1]
    else:
        return None