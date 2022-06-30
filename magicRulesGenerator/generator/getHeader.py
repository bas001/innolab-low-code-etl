from model import Rule
from utils.helper import getInputParams
from utils.helper import getOutputParams

 
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
