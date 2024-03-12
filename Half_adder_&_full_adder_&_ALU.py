
print("\tYou can organize the logic gate implementations into separate Python files and then import them as modules :\n")
def NAND_gate(a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1
# NOT gate implementation
def NOT_gate(a):
    return NAND_gate(a, a)
# AND gate implementation
def AND_gate(a, b):
    return NAND_gate(NAND_gate(a, b), NAND_gate(a, b))
# OR gate implementation
def OR_gate(a, b):
    return NAND_gate(NOT_gate(a), NOT_gate(b))
# XOR gate implementation
def XOR_gate(a, b):
    return AND_gate(OR_gate(a, b), NAND_gate(a, b))
# half-adder and full adder fonctions

def half_adder(a, b):
    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return s, c    

def full_adder(a, b, c):
    s1, c1 = half_adder(a, b)
    s, c_out = half_adder(s1, c)
    c_out = OR_gate(c1, c_out)
    return s, c_out

def ALU(a, b, c, opcode):
    if opcode == 0:
        s, c = half_adder(a, b)
    elif opcode == 1:
        s, c = full_adder(a, b, c)
    else:
        raise ValueError("Invalid opcode. Opcode must be 0 or 1.")
    
    return s, c

#Test the half-adder and the full-adder

print("\tHalf Adder:")
print("0 0 =",half_adder(0, 0))
print("0 1 =",half_adder(0, 1))
print("1 0 =",half_adder(1, 0))
print("1 1 =",half_adder(1, 1))

print("\n\tFull Adder: ")
print("0 0 0 =",full_adder(0, 0, 0)) 
print("0 0 1 =",full_adder(0, 0, 1)) 
print("0 1 0 =",full_adder(0, 1, 0))  
print("0 1 1 =",full_adder(0, 1, 1))  
print("1 0 0 =",full_adder(1, 0, 0)) 
print("1 0 1 =",full_adder(1, 0, 1)) 
print("1 1 0 =",full_adder(1, 1, 0))
print("1 1 1 =",full_adder(1, 1, 1))

print("\n\tTest out my ALU : Arithmetic Logic Unit")

# Test 1: Half-adder (opcode = 0)
a, b, c, opcode = 0, 0, 1, 0
s, c_out = ALU(a, b, c, opcode)
print(f"\nInput: a={a}, b={b}, c={c}, opcode={opcode}")
print(f"Output: s={s}, c_out={c_out}")

# Test 2: Full-adder (opcode = 1)
a, b, c, opcode = 0, 0, 1, 1
s, c_out = ALU(a, b, c, opcode)
print(f"\nInput: a={a}, b={b}, c={c}, opcode={opcode}")
print(f"Output: s={s}, c_out={c_out}")

# Test 3: Half-adder (opcode = 0)
a, b, c, opcode = 1, 1, 1, 0
s, c_out = ALU(a, b, c, opcode)
print(f"\nInput: a={a}, b={b}, c={c}, opcode={opcode}")
print(f"Output: s={s}, c_out={c_out}")

# Test 4: Full-adder (opcode = 1)
a, b, c, opcode = 1, 1, 1, 1
s, c_out = ALU(a, b, c, opcode)
print(f"\nInput: a={a}, b={b}, c={c}, opcode={opcode}")
print(f"Output: s={s}, c_out={c_out}")
