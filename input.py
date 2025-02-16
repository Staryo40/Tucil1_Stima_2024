from dataclasses import dataclass
from typing import List, Optional, Tuple
import random

@dataclass
class BreachProtocolInput:
    buffer: Optional[int] = None
    matrixWidth: Optional[int] = None
    matrixHeight: Optional[int] = None
    matrix: Optional[List[List[str]]] = None
    sequenceNumber: Optional[int] = None
    sequenceList: Optional[List[Tuple[List[str], int]]] = None

def readTextBreachProtocolInput(filename: str) -> BreachProtocolInput: # belum handle format salah
    res = BreachProtocolInput()

    with open(filename, 'r') as file:
        res.buffer = int(next(file).strip())
        res.matrixWidth, res.matrixHeight = map(int, next(file).strip().split(' ', 1)) # belum handle lebih dari 2 angka
        res.matrix = [next(file).strip().split(' ') for _ in range(res.matrixHeight)] # belum handle kalau input lebih/kurang
        res.sequenceNumber = int(next(file).strip())
        res.sequenceList = [ # belum handle kalau sequence kurang dari sequence number
            (next(file).strip().split(' '), int(next(file).strip()))
            for _ in range(res.sequenceNumber)
        ]

    return res

def generateRandomBPMatrix(width:int, height: int, tokens: list[str]) -> list[list[str]]:
    matrix = [['x' for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            matrix[i][j] = random.choice(tokens)
    
    return matrix

def generateRandomBPSequenceList(sequenceNumber: int , maxSequenceSize: int, tokens: list[str]) -> list[tuple[list[str], int]]:
    sequences = []
    i = 0

    while (i != sequenceNumber):
        length = random.randint(1, maxSequenceSize)

        sequence = []
        for _ in range(length):
            sequence.append(random.choice(tokens))
        
        if any(seq == sequence for seq, _ in sequences):
            continue
        else:
            sequenceValue = random.randint(length, maxSequenceSize + 2) * 5
            sequences.append((sequence, sequenceValue))
            i += 1

    return sequences


def readKeyboardBreachProtocolInput() -> BreachProtocolInput: # belum handle format salah
    res = BreachProtocolInput()

    tokenNumber = int(input("Number of unique tokens: "))
    while True:
        tokens = input(f"Enter {tokenNumber} unique tokens (separated by spaces): ").strip().split()
        if len(tokens) == tokenNumber:
            break  # Exit the loop if the number of tokens is correct
        else:
            print(f"Please enter exactly {tokenNumber} tokens. You entered {len(tokens)}.")

    res.buffer = int(input("Buffer size: "))
    res.matrixWidth, res.matrixHeight = map(int, input("Enter matrix size (width, height): ").strip().split(' '))
    res.sequenceNumber = int(input("Number of sequence: "))
    maxSequenceSize = int(input("Maximum size of sequence: "))

    res.matrix = generateRandomBPMatrix(res.matrixWidth, res.matrixHeight, tokens)
    res.sequenceList = generateRandomBPSequenceList(res.sequenceNumber, maxSequenceSize, tokens)

    return res
    

# test = readTextBreachProtocolInput("test1.txt")
# test = readKeyboardBreachProtocolInput()

# print("\nBuffer:", test.buffer)
# print("Width, Height:", test.matrixWidth, test.matrixHeight)
# print("Matrix:")
# for row in test.matrix:
#     print(row)
# print("Sequence Number:", test.sequenceNumber)
# print("Sequence List:", test.sequenceList)