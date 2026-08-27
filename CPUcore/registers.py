registerFile = [
    5, # Instruction Register (8-bit)
    10, # Interrupt Enable (8-bit)
    0, # Accumulator (8-bit)
    0, # Flags Register (8-bit (?))
    0, # B (8-bit, can form a 16-bit whole with C)
    0, # C (8-bit, can form a 16-bit whole with B)
    0, # D (8-bit, can form a 16-bit whole with E)
    0, # E (8-bit, can form a 16-bit whole with D)
    0, # H (8-bit, can form a 16-bit whole with L)
    0, # L (8-bit, can form a 16-bit whole with H)
    0, # Program Counter (16-bit)
    0 # Stack Pointer (16-bit)
]
