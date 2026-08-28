from Instructions import eightBitLoadInstructions as eightbit, miscellaneousInstructions as misc
import registers

register_A = 2
register_B = 4
register_C = 5
register_D = 6
register_E = 7
register_H = 8
register_L = 9

opcodeTable = {
    0x00: lambda: misc.nop(),
    0x40: lambda: eightbit.loadIntoRegisterFromRegister(register_B, register_B),
    0x41: lambda: eightbit.loadIntoRegisterFromRegister(register_B, register_C),
    0x42: lambda: eightbit.loadIntoRegisterFromRegister(register_B, register_D),
    0x43: lambda: eightbit.loadIntoRegisterFromRegister(register_B, register_E),
    0x44: lambda: eightbit.loadIntoRegisterFromRegister(register_B, register_H),
    0x45: lambda: eightbit.loadIntoRegisterFromRegister(register_B, register_L),
    0x47: lambda: eightbit.loadIntoRegisterFromRegister(register_B, register_A)
}
