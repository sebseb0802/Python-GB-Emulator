import registers

def loadIntoRegisterFromRegister(r1, r2):
    registers.registerFile[r1] = registers.registerFile[r2]
