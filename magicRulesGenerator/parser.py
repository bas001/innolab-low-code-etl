
import utils.fileHelper as fileHelper
from model import Rule
from model import Parameter
from model import Actions
from model import IfElseRule
from utils.errorHandler import throwError
from generator.createGroupBy import createGroupBy
from generator.createSummation import createSummation
from generator.createConcat import createConcat
from generator.createSplitting import createSplitting
from generator.createIfElse import createIfElse
from generator.getHeader import getHeader


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

def extractParams(str):
    rawParams =  stripStrings(str.split('->'))
    extractedParams = []

    for i in range(2):
        output = False if i == 0 else True

        for p in stripStrings(rawParams[i].split(',')):
            pSplit = stripStrings(p.split(':'))
            extractedParams.append(Parameter(pSplit[0], pSplit[1], output))
       
    return extractedParams

def extractIfElseRule(ruleString):
    extractedIfElseRules = []
    for r in stripStrings(ruleString.lstrip('(').rstrip(')').split(',')):
        ruleEntries = stripStrings(r.split('->'))
        extractedIfElseRules.append(IfElseRule(ruleEntries[0], ruleEntries[1].strip('"')))
    return extractedIfElseRules

def parseAttributes(attributesLine):
    return extractParams(attributesLine.split('attributes:')[1].strip())

def parseRule(ruleLine, action):
    ruleString = ruleLine.split('rule:')[1].strip()
    if action != Actions.IF_ELSE:
        return ruleString
    return extractIfElseRule(ruleString)

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
        rule = parseRule(line, action)
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
    elif rule.action == Actions.IF_ELSE:
        result+= createIfElse(rule)     
    return result

result=[]
for rule in rules:
    result.append(createFunction(rule))

fileHelper.writeFile("test",  "\n// magic-rule ¯\\_(ツ)_/¯".join(result))
