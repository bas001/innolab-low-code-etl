#!/bin/bash 

magicRulesEnginePath=../magicRulesEngine
outputGenRmFile=/../$magicRulesEnginePath/gen/rules

while getopts f:i:t:o: flag
do
    case "${flag}" in
        f) rmFile=${OPTARG};;
        i) inputFile=${OPTARG};;
        t) tableName=${OPTARG};;
        o) outputFileName=${OPTARG};;
    esac
done

# generate js file
python ../magicRulesGenerator/parser.py -f $magicRulesEnginePath/$rmFile -o $outputGenRmFile

# execute transformation
node index.js -t $tableName -f gen/rules.js -i $inputFile -o $outputFileName
