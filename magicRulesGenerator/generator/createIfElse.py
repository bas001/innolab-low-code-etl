from model import Rule
from utils.helper import getInputParamsName
from utils.helper import getOutputParamsName
from utils.helper import getIfElseConditions
from utils.helper import getIfElseReturnValues
from utils.helper import extractIfElseNoMatch

def createIfElse(rule:Rule):
    inputParam = getInputParamsName(rule.attributes)[0]
    outputParam = getOutputParamsName(rule.attributes)[0]
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