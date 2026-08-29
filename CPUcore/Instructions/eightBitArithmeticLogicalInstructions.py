import CPUcore.registers as registers
from bitarray import bitarray

# Helper functions:

def binaryAddition(a, b):
    # Adds two binary numbers, a and b, together, and returns the result and whether there was a carry as a list.
    
    carry = False
    while b.count(1) > 0:
        partial_sum = a ^ b # Sum of a and b, ignoring carries
    
        if (a & b)[0] == 1 and carry == False:
            # If the MSB of a & b == 1, then the carry flag must be set (if not already set),
            # since a 1 is about to be shifted left, off of the byte
            carry = True
    
        # Identifies where a and b are both 1,
        # which indicates where carries will occur.
        # Carries are then added to the partial sum again at the start of the loop
        carry = (a & b) << 1
    
        a = partial_sum
        b = carry

    return [a, carry, halfCarryCheck(a, b)]

def halfCarryCheck(a, b):
    # Uses bitmasks to check if a half-carry will occur during the addition of two binary numbers, a and b,
    # and returns this boolean value

    if (((a & 0x0F) + (b & 0x0F)) & 0x10) == 0x10:
        return True
    else:
        return False

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
    carryFlag = registers.registerFile[3][3]

    # First, add the values of a and the other register, store this value in a,
    # and update the carry/half-carry flags accordingly.
    tempAdditionResults = binaryAddition(a, b)
    a = tempAdditionResults[0]
    registers.registerFile[3][3] = tempAdditionResults[1]
    registers.registerFile[3][2] = tempAdditionResults[2]

    # Then, add the values of a and the carry flag, store this value in a,
    # and update the carry/half-carry flags accordingly.
    fullAdditionResults = binaryAddition(a, carryFlag)
    a = fullAdditionResults[0]
    registers.registerFile[3][3] = fullAdditionResults[1]
    registers.registerFile[3][2] = tempAdditionResults[2]

    if a.count(1) == 0:
        registers.registerFile[3][0] = True

    registers.registerFile[3][1] = False

    registers.registerFile[2] = a

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
