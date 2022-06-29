
file1 = open('test.rm', 'r')
Lines = file1.readlines()
  
def parseName(nameLine) :
    return nameLine.split('name:')[1].strip()

def parseAction(actionLine):
    rule = actionLine.split('action:')[1].strip()
    if rule == 'concat':
        return Actions.CONCAT
    elif rule == 'if-else':
        return Actions.IF_ELSE
    elif rule == 'group by':
        return Actions.GROUP_BY
    elif rule == 'summation':
        return Actions.SUMMATION
    else:
        return Actions.UNKOWN

def stripStrings(arr):
    return [item.strip() for item in arr]

def extractParams(str):
    rawParams =  stripStrings(str.split('->'))
    extractedParams = []

    for i in range(2):
        output = False if i == 0 else True

        for p in stripStrings(rawParams[i].split(',')):
            pSplit = stripStrings(p.split(':'))
            extractedParams.append(Parameter(pSplit[0], pSplit[1], output))
       
    return extractedParams

def parseAttributes(attributesLine):
    return extractParams(attributesLine.split('attributes:')[1].strip())


def parseRule(ruleLine):
    return ruleLine.split('rule:')[1].strip()

def parseOptions(optionLine):
    return optionLine.split('options:')[1].strip()

class Actions:
    UNKOWN      = 0
    CONCAT      = 1
    GROUP_BY    = 2
    IF_ELSE     = 3
    SUMMATION   = 4

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



lastKeyword = ''
name=''
action=''
attributes=''
rule=''
options=''
rules=[]
for line in Lines:
    if line.startswith('name:') : 
        if lastKeyword in ('attributes','rule', 'options'):
            rules.append(Rule(name,action,attributes,rule, options))
        elif lastKeyword not in (''):
            throwError('File is not correct!')
        lastKeyword='name'
        name = parseName(line)
    elif line.startswith('action:'):
        lastKeyword='action'
        action = parseAction(line)
    elif line.startswith('attributes:'):
        lastKeyword='attributes'
        attributes = parseAttributes(line)
    elif line.startswith('rule:'):
        lastKeyword='rule'
        rule = parseRule(line)
    elif line.startswith('options:'):
        lastKeyword='options'
        options = parseOptions(line)
    else:
        if line not in ('\n', ' '):
            print('Only the following keywords are allowed: name, action, attributes, rule, options. However, another word is used in the line:' + line)

rules.append(Rule(name,action,attributes,rule, options))

def createFunction(rule:Rule):
    if rule.action == Actions.CONCAT:
        writeFile(rule.name, createConcat(rule))
    elif rule.action == Actions.GROUP_BY:
        writeFile(rule.name, createGroupBy(rule))
    elif rule.action == Actions.SUMMATION:
        writeFile(rule.name, createSummation(rule))

def getInputParams(params:[Parameter]):
    return list(map(lambda x: x.paramName, filter(lambda param :  not param.output, params)))

def getOutputParams(params:[Parameter]):
    return list(map(lambda x: x.paramName, filter(lambda param :  param.output, params)))

def paramsToString(params:[Parameter]):
    return ', '.join(params)

def concatParams(params:[Parameter], delimiter):
    concatString = " + " + delimiter + " + "
    return concatString.join(params)

def createSummation(rule:Rule):
    inputParams = getInputParams(rule.attributes)
    outputParams = getOutputParams(rule.attributes)
    if len(inputParams) > 1:
        throwError("Action 'summation' accecpt just one input param.")
    if len(outputParams) > 1:
        throwError("Action 'summation' accecpt just one output param.")
    inputParam = inputParams[0]
    outputParam = outputParams[0]

    return f'''
    const summation = ({inputParam}) => {{
        return [{{ ['{outputParam}'] : {inputParam}.reduce((accumulator, curr) => accumulator + curr, 0)}}]
    }}
    '''

def createGroupBy(rule:Rule) :
    inputParams = getInputParams(rule.attributes)
    outputParams = getOutputParams(rule.attributes)
    if len(inputParams) > 1:
        throwError("Action 'Group by' accecpt just one input param.")
    if len(outputParams) > 1:
        throwError("Action 'Group by' accecpt just one output param.")
    inputParam = inputParams[0]
    outputParam = outputParams[0]
    return f'''
    const groupBy = ({inputParam}) => {{
    return [{{ ['{outputParam}'] : [...new Set({inputParam})].map(key => ({{ [key]: {inputParam}.filter(e => e === key).length }}))}}]
    }}
    '''

def throwError(message):
     print(message)
     quit()

def extractDelimiter(optionString):
    if 'delimiter' in optionString:
        return optionString[optionString.index("'"):optionString.rindex("'")+1]
    else:
        return "' '"

def createConcat(rule:Rule):
    delimiter="' '"
    inputParams = getInputParams(rule.attributes)
    outputParams = getOutputParams(rule.attributes)

    outputParam = outputParams[0]
    delimiter= extractDelimiter(rule.options)
   
    return f'''
    const {rule.name} = ({paramsToString(inputParams)}) => {{
        return [{{['{outputParam}'] : {concatParams(inputParams, delimiter)} }}]
    }}
    '''

def writeFile(name, function):
    f = open(name + ".js", "w")
    f.write(function)
    f.close()   
    


for rule in rules:
    createFunction(rule)


