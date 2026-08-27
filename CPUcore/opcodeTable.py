from Instructions import eightBitLoadInstructions as eightbit
# import registers

opcodeTable = {
    0x40: eightbit.loadRegisterFromRegister,
    0x41: eightbit.loadRegisterFromRegister
}


'''
Testing:

testopcode = input("Opcode:")
testr1 = int(input("r1: "))
testr2 = int(input("r2: "))

opcodeTable[testopcode](testr1, testr2)

print(registers.registerFile)
'''
