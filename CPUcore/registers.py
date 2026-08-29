from bitarray import bitarray

registerFile = [
    bitarray(8), # Instruction Register (8-bit)
    bitarray(8), # Interrupt Enable (8-bit)
    bitarray('11100110'), # Accumulator (8-bit)
    bitarray(8), # Flags Register (8-bit)
    bitarray('11001100'), # B (8-bit, can form a 16-bit whole with C)
    bitarray(8), # C (8-bit, can form a 16-bit whole with B)
    bitarray(8), # D (8-bit, can form a 16-bit whole with E)
    bitarray(8), # E (8-bit, can form a 16-bit whole with D)
    bitarray(8), # H (8-bit, can form a 16-bit whole with L)
    bitarray(8), # L (8-bit, can form a 16-bit whole with H)
    bitarray(16), # Program Counter (16-bit)
    bitarray(16) # Stack Pointer (16-bit)
]
