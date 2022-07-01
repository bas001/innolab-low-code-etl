class Actions:
    CONCAT      = 'concat'
    GROUP_BY    = 'group-by'
    IF_ELSE     = 'if-else'
    SUMMATION   = 'summation'
    SPLITTING   = 'splitting'
    CUSTOM      = 'custom'

class ParameterTypes:
    STRING      = 'String'
    NUMBER      = 'Number'
    ARRAY       = 'Array'
    OBJECT      = 'Object'

class Parameter:
    def __init__(self, paramName, paramType, output:bool):
        self.paramName = paramName
        self.paramType = paramType
        self.output = output

    def toString(self):
        return f'''{{"type": "{self.paramType}", "name": "{self.paramName}"}}'''

class Rule:
    def __init__(self, name, action: [Actions], attributes: [Parameter], rule, options):
        self.name = name
        self.action = action
        self.attributes = attributes
        self.rule = rule
        self.options = options
    
    def toString(self):
        return self.name + ' ' + str(self.action) + ' ' + str(self.attributes) + ' ' + self.options + ' ' 

class IfElseRule:
    def __init__(self, condition, returnValue):
        self.condition = condition
        self.returnValue = returnValue