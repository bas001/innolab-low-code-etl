from utils.errorHandler import throwError
from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName

def createGroupBy(rule:Rule) :
    inputParam = getInputParamsName(rule.attributes)[0]
    outputParam = getOutputParamsName(rule.attributes)[0]
    return f'''
    const {rule.name} = ({inputParam}) => {{
        return [{{ ['{outputParam}'] : [...new Set({inputParam})].map(key => ({{ [key]: {inputParam}.filter(e => e === key).length }}))}}]
    }}
    '''
