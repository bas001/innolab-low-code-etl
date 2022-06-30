from utils.errorHandler import throwError
from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName
from utils.helper import getIfElseConditions
from utils.helper import getIfElseReturnValues
from utils.helper import extractIfElseNoMatch

def createIfElse(rule:Rule):
    inputParams = getInputParamsName(rule.attributes)
    outputParams = getOutputParamsName(rule.attributes)
    if len(inputParams) > 1:
        throwError("Action 'If Else' accecpt just one input param.")
    if len(outputParams) > 1:
        throwError("Action 'If Else' accecpt just one output param.")
    inputParam = inputParams[0]
    outputParam = outputParams[0]
    conditions = getIfElseConditions(rule.rule)
    returnValues = getIfElseReturnValues(rule.rule)

    jsIfElseString = ''
    for i in range(len(conditions)):
        if i == 0:
            jsIfElseString+= f'''if ({conditions[i]}) {{
            return [{{['{outputParam}']: {returnValues[i]}}}]
        }} '''
        else:
            jsIfElseString+= f'''else if ({conditions[i]}) {{
            return [{{['{outputParam}']: {returnValues[i]}}}]
        }} '''
    
    noMatch = extractIfElseNoMatch(rule.options)
    if noMatch != None:
        jsIfElseString+=f'''else {{
            return [{{['{outputParam}']: {noMatch}}}]
        }}'''

    return f'''
    const {rule.name} = ({inputParam}) => {{
        {jsIfElseString}
    }}
    '''