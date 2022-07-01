from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName
from utils.helper import paramsToString

def createCustom(rule:Rule) :
    inputParams = getInputParamsName(rule.attributes)
    outputParams = getOutputParamsName(rule.attributes)
    return f'''
    const {rule.name} = ({paramsToString(inputParams)}) => [{{['{outputParams[0]}'] : {rule.rule}}}]
    '''