import CPUcore.registers as registers
from bitarray import bitarray

# python -m CPUcore.Instructions.eightBitArithmeticLogicalInstructions

# Helper functions:

def binaryAddition(a, b, hcCheck=True):
    # Adds two binary numbers, a and b, together, and returns the result and whether there was a carry as a list.
    
    # Save unchanged versions of a and b in order to calculate whether 
    # the half-carry flag has to be set later.
    unchangedA = a
    unchangedB = b

    carryFlag = 0
    while b.count(1) > 0:
        partialSum = a ^ b # Sum of a and b, ignoring carries
    
        if (a & b)[0] == 1 and carryFlag == 0:
            # If the MSB of a & b == 1, then the carry flag must be set (if not already set),
            # since a 1 is about to be shifted left, off of the byte
            carryFlag = 1
    
        # Identifies where a and b are both 1,
        # which indicates where carries will occur.
        # Carries are then added to the partial sum again at the start of the loop
        carry = (a & b) << 1
    
        a = partialSum
        b = carry

    if hcCheck:
        return [a, carryFlag, halfCarryCheck(unchangedA, unchangedB)]
    else:
        # halfCarryCheck should not use the version of the function that returns halfCarryCheck,
        # because this will start recursion
        return [a, carryFlag]

def halfCarryCheck(a, b):
    # Uses bitmasks to check if a half-carry will occur during the addition of two binary numbers, a and b,
    # and returns this boolean value

    if (binaryAddition((a & bitarray('00001111')), (b & bitarray('00001111')), False)[0] & bitarray('00010000')) == bitarray('00010000'):
        return 1
    else:
        return 0

def binarySubtraction(a, b):
    # Subtracts b from a, two binary numbers, and returns the result and whether there was a carry as a list.

    # In order to perform subtraction, we will convert the value of b to a negative number using
    # Two's complement, and then add that to the value of a
    b = ~b # Inverting the bits of b
    c = bitarray('00000001') # c is used to add 1 to b to complete Two's complement in the following line
    b = binaryAddition(b, c)[0]

    return binaryAddition(a, b)

# Actual instructions:

def addToAFromRegister(r2):
    a = registers.registerFile[2] # Register A
    b = registers.registerFile[r2]

    additionResults = binaryAddition(a, b)
    a = additionResults[0] # additionResults[0] stores the result of the addition

    # additionResults[1] stores whether a carry resulted from the addition,
    # and this Boolean value is stored in the carry flag.
    registers.registerFile[3][3] = additionResults[1]

    # additionResults[2] stores whether a half-carry resulted from the addition,
    # and this Boolean value is stored in the half-carry flag.
    registers.registerFile[3][2] = additionResults[2]

    if a.count(1) == 0:
        # If a is zero as a result of the addition, then the zero flag must be set
        registers.registerFile[3][0] = True

    registers.registerFile[3][1] = False # Subtraction has not occurred, so the subtraction flag must be cleared

    registers.registerFile[2] = a # Store the result of addition in A

def addToAFromRegisterAndCarryFlag(r2):
    a = registers.registerFile[2]
    b = registers.registerFile[r2]
    carryFlag = bitarray(f'0000000{registers.registerFile[3][3]}') # Get the carry flag bit from the registerFile for use in the addition

    # First, add the values of a and the other register, store this value in a,
    # and update the carry/half-carry flags accordingly.
    tempAdditionResults = binaryAddition(a, b)
    a = tempAdditionResults[0]
    registers.registerFile[3][3] = tempAdditionResults[1]
    registers.registerFile[3][2] = tempAdditionResults[2]

    # Then, add the values of a and the carry flag, store this value in a,
    # and update the carry/half-carry flags only if they weren't already set by the first addition.
    fullAdditionResults = binaryAddition(a, carryFlag)
    a = fullAdditionResults[0]
    if fullAdditionResults[1] == 1 and registers.registerFile[3][3] == 0:
        registers.registerFile[3][3] = fullAdditionResults[1]
    if fullAdditionResults[2] == 1 and registers.registerFile[3][2] == 0:
        registers.registerFile[3][2] = tempAdditionResults[2]

    if a.count(1) == 0:
        registers.registerFile[3][0] = True

    registers.registerFile[3][1] = False # Set subtraction flag to false

    registers.registerFile[2] = a # Store the result of addition in A

def subRegisterFromA(r2):
    a = registers.registerFile[2]
    b = registers.registerFile[r2]

    subtractionResults = binarySubtraction(a, b) # binarySubtraction returns the same list structure as binaryAddition
    a = subtractionResults[0]
    registers.registerFile[3][3] = subtractionResults[1]
    registers.registerFile[3][2] = subtractionResults[2]
    
    if a.count(1) == 0:
        # If a is zero as a result of the subtraction, then the zero flag must be set
        registers.registerFile[3][0] = True
    
    registers.registerFile[3][1] = True # Subtraction has occurred, so the subtraction flag must be set
    
    registers.registerFile[2] = a # Store the result of subtraction in A

def subRegisterAndCarryFlagFromA(r2):
    a = registers.registerFile[2]
    b = registers.registerFile[r2]
    carryFlag = bitarray(f'0000000{registers.registerFile[3][3]}') # Get the carry flag bit from the registerFile for use in the subtraction
    
    # First, subtract the value of the other register from a, store this value in a,
    # and update the carry/half-carry flags accordingly.
    tempSubtractionResults = binarySubtraction(a, b)
    print(tempSubtractionResults)
    a = tempSubtractionResults[0]
    registers.registerFile[3][3] = tempSubtractionResults[1]
    registers.registerFile[3][2] = tempSubtractionResults[2]

    # Then, subtract the value of the carry flag from a, store this value in a,
    # and set the carry/half-carry flags only if they weren't already set by the first subtraction.
    fullSubtractionResults = binarySubtraction(a, carryFlag)
    a = fullSubtractionResults[0]
    if fullSubtractionResults[1] == 1 and registers.registerFile[3][3] == 0:
        registers.registerFile[3][3] = fullSubtractionResults[1]
    if fullSubtractionResults[2] == 1 and registers.registerFile[3][2] == 0:
        registers.registerFile[3][2] = fullSubtractionResults[2]

    if a.count(1) == 0:
        registers.registerFile[3][0] = True

    registers.registerFile[3][1] = True # Set subtraction flag to true

    registers.registerFile[2] = a # Store the result of subtraction in A


# Testing:

print(f"A: {registers.registerFile[2]}")
print(f"B: {registers.registerFile[4]}")
print(f"Flags: {registers.registerFile[3]}")

print("Adding with flag...")
addToAFromRegisterAndCarryFlag(4)

print(f"A: {registers.registerFile[2]}")
print(f"B: {registers.registerFile[4]}")
print(f"Flags: {registers.registerFile[3]}")

print("Subtracting with flag...")
subRegisterAndCarryFlagFromA(4)

print(f"A: {registers.registerFile[2]}")
print(f"B: {registers.registerFile[4]}")
print(f"Flags: {registers.registerFile[3]}")