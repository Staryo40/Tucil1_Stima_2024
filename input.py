from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class BreachProtocolInput:
    buffer: Optional[int] = None
    matrixWidth: Optional[int] = None
    matrixHeight: Optional[int] = None
    matrix: Optional[List[List[str]]] = None
    sequenceNumber: Optional[int] = None
    sequenceList: Optional[List[Tuple[List[str], int]]] = None

def readTextBreachProtocolInput(filename: str) -> BreachProtocolInput:
    res = BreachProtocolInput()

    with open(filename, 'r') as file:
        res.buffer = int(next(file).strip())
        res.matrixWidth, res.matrixHeight = map(int, next(file).strip().split(' ', 1))
        res.matrix = [next(file).strip().split(' ') for _ in range(res.matrixHeight)]
        res.sequenceNumber = int(next(file).strip())
        res.sequenceList = [
            (next(file).strip().split(' '), int(next(file).strip()))
            for _ in range(res.sequenceNumber)
        ]

    return res

# test = readTextBreachProtocolInput("test1.txt")

# print("Buffer:", test.buffer)
# print("Width, Height:", test.matrixWidth, test.matrixHeight)
# print("Matrix:")
# for row in test.matrix:
#     print(row)
# print("Sequence Number:", test.sequenceNumber)
# print("Sequence List:", test.sequenceList)