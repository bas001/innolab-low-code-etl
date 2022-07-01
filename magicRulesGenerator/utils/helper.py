from model import Parameter
from model import IfElseRule

def stripStrings(arr):
    return [item.strip() for item in arr]

def getInputParams(params:Parameter):
    return list(filter(lambda param :  not param.output, params))

def getOutputParams(params:Parameter):
    return list(filter(lambda param :  param.output, params))

def getInputParamsName(params:Parameter):
    return list(map(lambda x: x.paramName, getInputParams(params)))

def getOutputParamsName(params:Parameter):
    return list(map(lambda x: x.paramName, getOutputParams(params)))

def getIfElseConditions(rules:IfElseRule):
    return list(map(lambda x: x.condition, rules))

def getIfElseReturnValues(rules:IfElseRule):
    return list(map(lambda x: x.returnValue, rules))

def paramsToString(params:Parameter):
    return ', '.join(params)

def concatParams(params:Parameter, delimiter):
    concatString = " + " + delimiter + " + "
    return concatString.join(params)

def extractIfElseRule(ruleString):
    extractedIfElseRules = []
    for r in stripStrings(ruleString.lstrip('(').rstrip(')').split(',')):
        ruleEntries = stripStrings(r.split('->'))
        extractedIfElseRules.append(IfElseRule(ruleEntries[0], ruleEntries[1].strip('"')))
    return extractedIfElseRules

def extractCustomRule(ruleString):
    return ruleString[1:-1]

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