class Actions:
    UNKOWN      = 0
    CONCAT      = 1
    GROUP_BY    = 2
    IF_ELSE     = 3
    SUMMATION   = 4
    SPLITTING   = 5

class Parameter:
    def __init__(self, paramName, paramType, output:bool):
        self.paramName = paramName
        self.paramType = paramType
        self.output = output

class Rule:
    def __init__(self, name, action, attributes: [Parameter], rule, options):
        self.name = name
        self.action = action
        self.attributes = attributes
        self.rule = rule
        self.options = options
    
    def toString(self):
        return self.name + ' ' + str(self.action) + ' ' + str(self.attributes) + ' ' + self.options + ' ' 