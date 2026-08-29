from Instructions import eightBitLoadInstructions as eightbitload 
from Instructions import miscellaneousInstructions as misc
from Instructions import eightBitArithmeticLogicalInstructions as eightbitarith

register_A = 2
register_B = 4
register_C = 5
register_D = 6
register_E = 7
register_H = 8
register_L = 9

opcodeTable = {
    0x00: lambda: misc.nop(),
    0x40: lambda: eightbitload.loadIntoRegisterFromRegister(register_B, register_B),
    0x41: lambda: eightbitload.loadIntoRegisterFromRegister(register_B, register_C),
    0x42: lambda: eightbitload.loadIntoRegisterFromRegister(register_B, register_D),
    0x43: lambda: eightbitload.loadIntoRegisterFromRegister(register_B, register_E),
    0x44: lambda: eightbitload.loadIntoRegisterFromRegister(register_B, register_H),
    0x45: lambda: eightbitload.loadIntoRegisterFromRegister(register_B, register_L),
    0x47: lambda: eightbitload.loadIntoRegisterFromRegister(register_B, register_A),
    0x80: lambda: eightbitarith.addToAFromRegister(register_B),
    0x81: lambda: eightbitarith.addToAFromRegister(register_C),
    0x82: lambda: eightbitarith.addToAFromRegister(register_D),
    0x83: lambda: eightbitarith.addToAFromRegister(register_E),
    0x84: lambda: eightbitarith.addToAFromRegister(register_H),
    0x85: lambda: eightbitarith.addToAFromRegister(register_L),
    0x87: lambda: eightbitarith.addToAFromRegister(register_A),
    0x90: lambda: eightbitarith.subRegisterFromA(register_B),
    0x91: lambda: eightbitarith.subRegisterFromA(register_C),
    0x92: lambda: eightbitarith.subRegisterFromA(register_D),
    0x93: lambda: eightbitarith.subRegisterFromA(register_E),
    0x94: lambda: eightbitarith.subRegisterFromA(register_H),
    0x95: lambda: eightbitarith.subRegisterFromA(register_L),
    0x96: lambda: eightbitarith.subRegisterFromA(register_A)
}
