import utils.fileHelper as fileHelper
from model import Rule
from model import Parameter
from model import Actions
from model import IfElseRule
from model import ParameterTypes
from utils.errorHandler import throwError
from validator import validateParamType
from validator import validateParamCount
from generator.createGroupBy import createGroupBy
from generator.createSummation import createSummation
from generator.createConcat import createConcat
from generator.createSplitting import createSplitting
from generator.createIfElse import createIfElse
from generator.getHeader import getHeader
import getopt
import sys
from pathlib import Path

def parseName(nameLine) :
    return nameLine.split('name:')[1].strip()

def parseAction(actionLine):
    action = actionLine.split('action:')[1].strip()
    if action == 'concat':
        return Actions.CONCAT
    elif action == 'if-else':
        return Actions.IF_ELSE
    elif action == 'group-by':
        return Actions.GROUP_BY
    elif action == 'summation':
        return Actions.SUMMATION
    elif action == 'splitting':
        return Actions.SPLITTING
    else:
        throwError("Action type '" + action + "' is unknown!")

def stripStrings(arr):
    return [item.strip() for item in arr]

def parseParamType(paramType):
    if paramType == 'String':
        return ParameterTypes.STRING
    elif paramType == 'Number':
        return ParameterTypes.NUMBER
    elif paramType == 'Array':
        return ParameterTypes.ARRAY
    elif paramType == 'Object':
        return ParameterTypes.OBJECT
    else:
        throwError("Parameter type '" + paramType + "' is unkown!")

def extractParams(str, action):
    rawParams =  stripStrings(str.split('->'))
    extractedParams = []
    for i in range(2):
        output = False if i == 0 else True
        for p in stripStrings(rawParams[i].split(',')):
            paramName = stripStrings(p.split(':'))[0]
            paramType = parseParamType(stripStrings(p.split(':'))[1])
            extractedParam = Parameter(paramName, paramType, output)
            validateParamType(extractedParam, action)
            extractedParams.append(extractedParam)      
    validateParamCount(extractedParams, action)
    return extractedParams

def extractIfElseRule(ruleString):
    extractedIfElseRules = []
    for r in stripStrings(ruleString.lstrip('(').rstrip(')').split(',')):
        ruleEntries = stripStrings(r.split('->'))
        extractedIfElseRules.append(IfElseRule(ruleEntries[0], ruleEntries[1].strip('"')))
    return extractedIfElseRules

def parseAttributes(attributesLine, action):
    return extractParams(attributesLine.split('attributes:')[1].strip(), action)

def parseRule(ruleLine, action):
    ruleString = ruleLine.split('rule:')[1].strip()
    if action != Actions.IF_ELSE:
        return ruleString
    return extractIfElseRule(ruleString)

def parseOptions(optionLine):
    return optionLine.split('options:')[1].strip()

def createFunction(rule:Rule):
    result= getHeader(rule)
    if rule.action == Actions.CONCAT:
        result+= createConcat(rule)
    elif rule.action == Actions.GROUP_BY:
        result+= createGroupBy(rule)
    elif rule.action == Actions.SUMMATION:
        result+= createSummation(rule)
    elif rule.action == Actions.SPLITTING:
        result+= createSplitting(rule)
    elif rule.action == Actions.IF_ELSE:
        result+= createIfElse(rule)     
    return result

def main(argv):
    usage = '''usage: parser.py [options] -f <rm-filename> -o <output-filename>

    mandatory:
        -f, --rmFilename        rm filename
        -o, --outputFilename    output filename
    '''

    mandatory_params = dict.fromkeys(["rmFilename", "outputFilename"])
    

    try:
        opts,args = getopt.getopt(argv, "hf:o:",["help", "rmFilename", "outputFilename"])
    except getopt.GetoptError as error:
        print(error)
        print(usage)
        sys.exit(2)
    for opt,arg in opts:
        if opt in ("-h", "--help"):
            print(usage)
            sys.exit()
        elif opt in ("-f", "--rmFilename"):
            mandatory_params["rmFilename"] = arg 
        elif opt in ("-o", "--outputFilename"):
            mandatory_params["outputFilename"] = arg 

    result = generate(Path(mandatory_params["rmFilename"]).read_text())
    fileHelper.writeFile(str(mandatory_params["outputFilename"]),  result)


def generate(lines):   
    lastKeyword = ''
    name=''
    action=''
    attributes=''
    rule=''
    options=''
    rules=[]

    for line in lines.splitlines():     
        if line.startswith('name:') : 
            if lastKeyword in ('attributes','rule', 'options'):
                rules.append(Rule(name, action, attributes, rule, options))
            elif lastKeyword not in (''):
                throwError('File is not correct!')
            lastKeyword='name'
            name = parseName(line)
        elif line.startswith('action:'):
            lastKeyword='action'
            action = parseAction(line)
        elif line.startswith('attributes:'):
            lastKeyword='attributes'
            attributes = parseAttributes(line, action)
        elif line.startswith('rule:'):
            lastKeyword='rule'
            rule = parseRule(line, action)
        elif line.startswith('options:'):
            lastKeyword='options'
            options = parseOptions(line)
        else:
            if len(line) > 0:
                print('Only the following keywords are allowed: name, action, attributes, rule, options. However, another word is used in the line:' + line)

    rules.append(Rule(name,action,attributes,rule, options))
    result=[]
    for rule in rules:
        result.append(createFunction(rule))

    return "\n// magic-rule ¯\\_(ツ)_/¯".join(result)
    

if __name__ == "__main__":
        main(sys.argv[1:])
