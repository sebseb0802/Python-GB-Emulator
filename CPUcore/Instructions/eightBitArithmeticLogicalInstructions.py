import CPUcore.registers as registers

def addToRegisterFromRegister(r1, r2):
    a = registers.registerFile[r1]
    b = registers.registerFile[r2]

    if (((a & 0x0F) + (b & 0x0F)) & 0x10) == 0x10:
        # Uses bitmasks to check if the half-carry flag needs to be set
        registers.registerFile[3][2] = True

    while b.count(1) > 0:
        partial_sum = a ^ b # Sum of a and b, ignoring carries

        if (a & b)[0] == 1 and registers.registerFile[3][3] == False:
            # If the MSB of a & b == 1, then the carry flag must be set (if not already set),
            # since a 1 is about to be shifted left, off of the byte
            registers.registerFile[3][3] = True

        # Identifies where a and b are both 1,
        # which indicates where carries will occur.
        # Carries are then added to the partial sum again at the start of the loop
        carry = (a & b) << 1

        a = partial_sum
        b = carry

    if a.count(1) == 0:
        # If a is zero as a result of the addition/shifting, then the zero flag must be set
        registers.registerFile[3][0] = True

    registers.registerFile[3][1] = False # Subtraction has not occurred, so the subtraction flag must be cleared

    registers.registerFile[r1] = a # Store the result of addition in the first register

'''
Testing:

print(f"A: {registers.registerFile[2]}")
print(f"B: {registers.registerFile[4]}")
print(f"Flags: {registers.registerFile[3]}")

print("Operation...")
addToRegisterFromRegister(2, 4)

print(f"A: {registers.registerFile[2]}")
print(f"B: {registers.registerFile[4]}")
print(f"Flags: {registers.registerFile[3]}")
'''
