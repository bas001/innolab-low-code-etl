from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName

def createSummation(rule:Rule):
    inputParam = getInputParamsName(rule.attributes)[0]
    outputParam = getOutputParamsName(rule.attributes)[0]

    return f'''
    const {rule.name} = ({inputParam}) => {{
        return [{{ ['{outputParam}'] : {inputParam}.reduce((accumulator, curr) => accumulator + curr, 0)}}]
    }}
    '''
