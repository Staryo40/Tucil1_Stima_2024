from input import *
from dataclasses import dataclass
from typing import List, Optional, Tuple

import time

@dataclass
class BreachProtocolOutput:
    matrix: Optional[List[List[str]]] = None
    sequence: Optional[list[list[str]]] = None
    sequenceValue: Optional[List[Tuple[List[str], int]]] = None
    coordinateList: Optional[list[list[tuple[int, int]]]] = None
    executionTime: Optional[int] = None

def breachProtocol(input: BreachProtocolInput) -> BreachProtocolOutput:
    startTime = time.time()

    sequences = listOfSequences(input.matrix, input.buffer)

    maxSeqs = []
    maxCoords = []
    maxValue = 0
    for seq in sequences:
        val = sequenceValue(seq[0], input.sequenceList)
        if (val > maxValue):
            maxSeqs = [seq[0]]
            maxCoords = [seq[1]]
            maxValue = val
        elif (val == maxValue and val != 0):
            if (seq[0] not in maxSeqs):
                maxSeqs = maxSeqs + [seq[0]]
                maxCoords = maxCoords + [seq[1]]
    endTime = time.time()

    executionTime = (endTime - startTime) * 1000  # Convert seconds to milliseconds
    executionTime = round(executionTime, 4)  # Round to 4 decimal places

    output = BreachProtocolOutput(matrix=input.matrix, 
                                  sequence=maxSeqs,
                                  sequenceValue=maxValue,
                                  coordinateList=maxCoords,
                                  executionTime=executionTime)

    return output

def listOfSequences(m: list[list[str]], buffer:int) -> List[Tuple[list[str], list[Tuple[int, int]]]]:
    sequences = []

    for i in range(len(m[0])):
        sequences += listOfSequencesRecur([m[0][i]], [(0, i)], False, m, buffer)

    return sequences

def listOfSequencesRecur(sequence: list[str], listOfCoordinate: list[Tuple[int, int]], horizontal: bool, m: list[list[str]], buffer: int) -> List[Tuple[list[str], list[Tuple[int, int]]]]:
    if len(sequence) == buffer:
        return [(sequence, listOfCoordinate)]
    
    res = [(sequence, listOfCoordinate)]
    lastCoordinate = listOfCoordinate[-1]  
    
    if horizontal:
        for i in range(len(m[0])):
            if i != lastCoordinate[1]:  
                newSequence = sequence + [m[lastCoordinate[0]][i]]  
                newCoord = listOfCoordinate + [(lastCoordinate[0], i)]  
                res += listOfSequencesRecur(newSequence, newCoord, False, m, buffer)
    else:
        for i in range(len(m)):
            if i != lastCoordinate[0]:  
                newSequence = sequence + [m[i][lastCoordinate[1]]]  
                newCoord = listOfCoordinate + [(i, lastCoordinate[1])] 
                res += listOfSequencesRecur(newSequence, newCoord, True, m, buffer)

    return res

def sequenceValue(seq: list[str], targetSeqList: List[Tuple[List[str], int]]) -> int:
    value = 0

    # Iterate through each target sequence and its corresponding value
    for tarSeq, seqValue in targetSeqList:
        count = 0
        
        for i in range(len(seq) - len(tarSeq) + 1): 
            if seq[i:i+len(tarSeq)] == tarSeq:
                count += 1
        
        value += seqValue * count

    return value
            
read = readTextBreachProtocolInput("test1.txt")
sequences = listOfSequences(read.matrix, read.buffer)
result = breachProtocol(read)

for seq in sequences:
    if (seq[0] == ['7A', 'BD', '7A', 'BD', '1C', 'BD', '55']):
        print(seq)
# print("Original matrix:")
# for row in (result.matrix):
#     print(row)
# print(f"Max value: {result.sequenceValue}")
# print(f"Execution time: {result.executionTime}")
# print("Max sequences:")
# for seq in result.sequence:
#     print(seq)
# print("Max coordinates:")
# for coord in result.coordinateList:
#     print(coord)
