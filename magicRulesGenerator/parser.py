
import fileHelper 
from model import Rule
from model import Parameter
from model import Actions
from errorHandler import throwError
from generator import createGroupBy
from generator import createSummation
from generator import createConcat
from generator import createSplitting
from generator import getHeader


def parseName(nameLine) :
    return nameLine.split('name:')[1].strip()

def parseAction(actionLine):
    rule = actionLine.split('action:')[1].strip()
    if rule == 'concat':
        return Actions.CONCAT
    elif rule == 'if-else':
        return Actions.IF_ELSE
    elif rule == 'group-by':
        return Actions.GROUP_BY
    elif rule == 'summation':
        return Actions.SUMMATION
    elif rule == 'splitting':
        return Actions.SPLITTING
    else:
        throwError("Action type '" + rule + "' is unknown!")

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


Lines = fileHelper.readLines("test.rm")

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
    result= getHeader(rule)
    if rule.action == Actions.CONCAT:
        result+= createConcat(rule)
    elif rule.action == Actions.GROUP_BY:
        result+= createGroupBy(rule)
    elif rule.action == Actions.SUMMATION:
        result+= createSummation(rule)
    elif rule.action == Actions.SPLITTING:
        result+= createSplitting(rule)        
    return result

result=[]
for rule in rules:
    result.append(createFunction(rule))

fileHelper.writeFile("test",  "\n// magic-rule ¯\\_(ツ)_/¯".join(result))
