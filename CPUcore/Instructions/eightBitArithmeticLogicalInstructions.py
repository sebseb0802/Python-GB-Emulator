import CPUcore.registers as registers

def addToRegisterFromRegister(r1, r2):
    a = registers.registerFile[r1]
    b = registers.registerFile[r2]

    while b.count(1) > 0:
        partial_sum = a ^ b # Sum of a and b, ignoring carries

        if (a & b)[0] == 1:
            # If the MSB of a & b == 1, then the carry flag must be set
            # (Since a 1 is about to be shifted left, off of the byte)
            registers.registerFile[3][3] = True

        if (a & b)[4] == 1:
            # If bit 3 of a & b == 1, then the half carry flag must be set
            # (Since a 1 is about to be shifted from the lower nibble to the upper nibble)
            registers.registerFile[3][2] = True

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
