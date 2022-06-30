from utils.errorHandler import throwError
from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName

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
