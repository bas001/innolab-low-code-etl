from utils.errorHandler import throwError
from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName

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
