from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName
from utils.helper import extractDelimiter
from utils.helper import concatParams
from utils.helper import paramsToString

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
