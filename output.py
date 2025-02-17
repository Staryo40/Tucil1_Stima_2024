from solution import *
import os

def printOutputAll(out: BreachProtocolOutput): # belum handle tidak ada solusi
    print("\nOriginal matrix:")
    for row in (out.matrix):
        print(row)
    print(f"\nMax value: {out.sequenceValue}")
    print(f"Execution time: {out.executionTime}\n")
    for i in range(len(out.sequence)):
        print(f"Sequence {i+1}: {out.sequence[i]}")
        print(f"Coordinates {i+1}: {out.coordinateList[i]}\n")

def printOutputSingle(out: BreachProtocolOutput): # belum handle tidak ada solusi
    print("\nOriginal matrix:")
    for row in (out.matrix):
        print(row)
    print(f"\nMax value: {out.sequenceValue}")
    print(f"Execution time: {out.executionTime}\n")
    print(f"Maximum Sequence: {out.sequence[0]}")
    print(f"Coordinates: {out.coordinateList[0]}")

def get_next_output_file():
    # Check if the 'outputs' directory exists
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    # Get a list of all files in the 'outputs' directory
    existing_files = os.listdir('outputs')
    output_files = [f for f in existing_files if f.startswith('output') and f.endswith('.txt')]

    # Find the highest existing file number
    max_number = 0
    for file in output_files:
        # Extract the number from the filename
        try:
            number = int(file[6:-4])  # Get the number from 'output<xx>.txt'
            max_number = max(max_number, number)
        except ValueError:
            continue
    
    # The next output file will be max_number + 1
    return f'outputs/output{max_number + 1}.txt'

def exportTextOutputAll(out: BreachProtocolOutput):
    output_filename = get_next_output_file()

    with open(output_filename, 'w') as f:
        f.write("Original matrix:\n")
        for row in out.matrix:
            f.write(str(row) + '\n')
        f.write(f"\nMax value: {out.sequenceValue}\n")
        f.write(f"Execution time: {out.executionTime}\n")
        
        for i in range(len(out.sequence)):
            f.write(f"Sequence {i+1}: {out.sequence[i]}\n")
            f.write(f"Coordinates {i+1}: {out.coordinateList[i]}\n\n")

    print(f"Output written to {output_filename}")

def exportTextOutputSingle(out: BreachProtocolOutput):
    output_filename = get_next_output_file()

    with open(output_filename, 'w') as f:
        f.write("Original matrix:\n")
        for row in out.matrix:
            f.write(str(row) + '\n')
        f.write(f"\nMax value: {out.sequenceValue}\n")
        f.write(f"Execution time: {out.executionTime}\n")
        
        f.write(f"Maximum Sequence: {out.sequence[0]}\n")
        f.write(f"Coordinates: {out.coordinateList[0]}\n")

    print(f"Output written to {output_filename}")


read = readTextBreachProtocolInput("test1.txt")
resultSingle = breachProtocol(read, "all")
exportTextOutputAll(resultSingle)