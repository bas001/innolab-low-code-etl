from utils.errorHandler import throwError
from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName
from utils.helper import extractDelimiter
from utils.helper import paramsToString

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

        for (let i = 0; i < outputParamNames.length ; i++) {{
            if (i == outputParamNames.length - 1) {{
                output.push({{[outputParamNames[i]] : splittedInput.slice(i).join({delimiter})}})
            }} else {{
                output.push({{[outputParamNames[i]] : splittedInput[i]}})
            }}
        }}

        return output
    }}
    '''
