from errorHandler import throwError
from model import Rule
from model import Parameter
from helper import getInputParams
from helper import getOutputParams
from helper import getInputParamsName
from helper import getOutputParamsName
from helper import extractDelimiter
from helper import concatParams
from helper import paramsToString

def createSummation(rule:Rule):
    inputParams = getInputParamsName(rule.attributes)
    outputParams = getOutputParamsName(rule.attributes)
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
    inputParams = getInputParamsName(rule.attributes)
    outputParams = getOutputParamsName(rule.attributes)
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
    inputParams = getInputParamsName(rule.attributes)
    outputParams = getOutputParamsName(rule.attributes)

    outputParam = outputParams[0]
    delimiter= extractDelimiter(rule.options)

    return f'''
    const {rule.name} = ({paramsToString(inputParams)}) => {{
        return [{{['{outputParam}'] : {concatParams(inputParams, delimiter)} }}]
    }}
    '''

def createSplitting(rule:Rule):
    delimiter= extractDelimiter(rule.options)
    inputParams = getInputParamsName(rule.attributes)
    outputParams = getOutputParamsName(rule.attributes)

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


def getHeader(rule:Rule):
    return f'''
    /*
    metainformation-start
    {{
    "name": "{rule.name}",
    "inputs": [{ ",".join(list(map(lambda x: x.toString(), getInputParams(rule.attributes))))}],
    "output": [{ ",".join(list(map(lambda x: x.toString(), getOutputParams(rule.attributes))))}]
    }}
    metainformation-end
    */
    '''
