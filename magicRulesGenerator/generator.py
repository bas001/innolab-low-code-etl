from errorHandler import throwError
from model import Rule
from model import Parameter

def getInputParams(params:[Parameter]):
    return list(map(lambda x: x.paramName, filter(lambda param :  not param.output, params)))

def getOutputParams(params:[Parameter]):
    return list(map(lambda x: x.paramName, filter(lambda param :  param.output, params)))

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

def createSummation(rule:Rule):
    inputParams = getInputParams(rule.attributes)
    outputParams = getOutputParams(rule.attributes)
    if len(inputParams) > 1:
        throwError("Action 'summation' accecpt just one input param.")
    if len(outputParams) > 1:
        throwError("Action 'summation' accecpt just one output param.")
    inputParam = inputParams[0]
    outputParam = outputParams[0]

    return f'''
    const {rule.name} = ({inputParam}) => {{
        return [{{ ['{outputParam}'] : {inputParam}.reduce((accumulator, curr) => accumulator + curr, 0)}}]
    }}
    '''

def createGroupBy(rule:Rule) :
    inputParams = getInputParams(rule.attributes)
    outputParams = getOutputParams(rule.attributes)
    if len(inputParams) > 1:
        throwError("Action 'Group by' accecpt just one input param.")
    if len(outputParams) > 1:
        throwError("Action 'Group by' accecpt just one output param.")
    inputParam = inputParams[0]
    outputParam = outputParams[0]
    return f'''
    const {rule.name} = ({inputParam}) => {{
    return [{{ ['{outputParam}'] : [...new Set({inputParam})].map(key => ({{ [key]: {inputParam}.filter(e => e === key).length }}))}}]
    }}
    '''

def createConcat(rule:Rule):
    delimiter="' '"
    inputParams = getInputParams(rule.attributes)
    outputParams = getOutputParams(rule.attributes)

    outputParam = outputParams[0]
    delimiter= extractDelimiter(rule.options)

    return f'''
    const {rule.name} = ({paramsToString(inputParams)}) => {{
        return [{{['{outputParam}'] : {concatParams(inputParams, delimiter)} }}]
    }}
    '''

def createSplitting(rule:Rule):
    delimiter= extractDelimiter(rule.options)
    inputParams = getInputParams(rule.attributes)
    outputParams = getOutputParams(rule.attributes)

    if len(inputParams) > 1:
        throwError("Action 'Splitting' accecpt just one input param.")

    return f'''
    const {rule.name} = ({paramsToString(inputParams)}) => {{
        const splittedInput = {inputParams[0]}.split({delimiter})
        const outputParamNames = {outputParams}
        const output = []

        for (i = 0; i < outputParamNames.length ; i++) {{
            if (i == outputParamNames.length - 1) {{
                output.push({{[outputParamNames[i]] : splittedInput.slice(i).join({delimiter})}})
            }} else {{
                output.push({{[outputParamNames[i]] : splittedInput[i]}})
            }}
        }}

        return output
    }}
    '''