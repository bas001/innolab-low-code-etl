from model import Actions
from model import ParameterTypes
from model import Parameter
from utils.errorHandler import throwError

ALLOWED_ACTION_ATTRIBUTES = {
    Actions.CONCAT : { 
        'inputCount' : 100, 
        'inputTypes' : [ParameterTypes.STRING, ParameterTypes.NUMBER], 
        'outputCount' : 1, 
        'outputTypes' : [ParameterTypes.STRING] 
    },
    Actions.GROUP_BY : { 
        'inputCount' : 1, 
        'inputTypes' : [ParameterTypes.ARRAY], 
        'outputCount' : 1, 
        'outputTypes' : [ParameterTypes.OBJECT] 
    },
    Actions.SUMMATION : { 
        'inputCount' : 1, 
        'inputTypes' : [ParameterTypes.ARRAY], 
        'outputCount' : 1, 
        'outputTypes' : [ParameterTypes.NUMBER]
    },
    Actions.SPLITTING : { 
        'inputCount' : 1, 
        'inputTypes' : [ParameterTypes.STRING], 
        'outputCount' : 100, 
        'outputTypes' : [ParameterTypes.STRING] 
    },
    Actions.IF_ELSE : { 
        'inputCount' : 1, 
        'inputTypes' : [ParameterTypes.STRING, ParameterTypes.NUMBER, ParameterTypes.ARRAY, ParameterTypes.OBJECT], 
        'outputCount' : 1, 
        'outputTypes' : [ParameterTypes.STRING, ParameterTypes.NUMBER, ParameterTypes.ARRAY, ParameterTypes.OBJECT] 
    },
        Actions.CUSTOM : { 
        'inputCount' : 100, 
        'inputTypes' : [ParameterTypes.STRING, ParameterTypes.NUMBER, ParameterTypes.ARRAY, ParameterTypes.OBJECT], 
        'outputCount' : 1, 
        'outputTypes' : [ParameterTypes.STRING, ParameterTypes.NUMBER, ParameterTypes.ARRAY, ParameterTypes.OBJECT] 
    }
}

def validateParamType(param:Parameter, action:Actions):
    if param.output == True:
        if param.paramType not in ALLOWED_ACTION_ATTRIBUTES[action]['outputTypes']:
            throwError("Parameter type '" + param.paramType + "' is not allowed as output for action '" + action + "'!")
    else:
        if param.paramType not in ALLOWED_ACTION_ATTRIBUTES[action]['inputTypes']:
            throwError("Parameter type '" + param.paramType + "' is not allowed as input for action '" + action + "'!")

def validateParamCount(paramList, action:Actions):
    inputCount = len(list(filter(lambda p : not p.output, paramList)))
    outputCount = len(list(filter(lambda p : p.output, paramList)))
    if inputCount > ALLOWED_ACTION_ATTRIBUTES[action]['inputCount']:
        throwError("Action '" + action + "' accepts at maximum '" + str(ALLOWED_ACTION_ATTRIBUTES[action]['inputCount']) + "' input parameter!")
    if outputCount > ALLOWED_ACTION_ATTRIBUTES[action]['outputCount']:
        throwError("Action '" + action + "' accepts at maximum '" + str(ALLOWED_ACTION_ATTRIBUTES[action]['outputCount']) + "' output parameter!")


