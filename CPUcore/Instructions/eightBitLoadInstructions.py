import registers

def loadRegisterFromRegister(register1, register2):
    registers.registerFile[register1] = registers.registerFile[register2]
