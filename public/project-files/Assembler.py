import os
def decbin(num):
    return format(num, '016b')

symbol_table = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576,
    "R0": 0, "R1": 1, "R2": 2, "R3": 3,
    "R4": 4, "R5": 5, "R6": 6, "R7": 7,
    "R8": 8, "R9": 9, "R10": 10, "R11": 11,
    "R12": 12, "R13": 13, "R14": 14, "R15": 15,
}

comp_table = {
    "0":   "0101010", "1":   "0111111", "-1":  "0111010",
    "D":   "0001100", "A":   "0110000", "!D":  "0001101",
    "!A":  "0110001", "-D":  "0001111", "-A":  "0110011",
    "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
    "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
    "M":   "1110000", "!M":  "1110001", "-M":  "1110011",
    "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
    "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
    "D|M": "1010101"
}

dest_table = {
    "null": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111"
}

jump_table = {
    "null": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
}

percentage = 0
lines_add = 0
with open("Sum.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    cleaned = line.strip()
    if '//' in cleaned:
        cleaned = cleaned.split('//')[0].strip()
    if not cleaned:
        continue
    if not cleaned or (cleaned.startswith('(') and cleaned.endswith(')')):
        cleaned = cleaned.split()[0].strip()
        label = cleaned[1:-1]
        symbol_table[label] = lines_add
        continue
    lines_add += 1

output_lines = []
next_variable_address = 16

for line in lines:
    original_line = line.rstrip('\n')
    cleaned = original_line.strip()
    
    if '//' in line:
        line = line.split('//')[0].strip()
    if not line:
        continue
    if '//' in original_line:
        code_part = original_line.split('//')[0]
    else:
        code_part = original_line

    cleaned = code_part.strip()
    

    if not cleaned or (cleaned.startswith('(') and cleaned.endswith(')')):
        continue
    percentage+=1
    print(f"Processing: {percentage/(lines_add)*100:.50f}%")
    if cleaned.startswith('@'):
        symbol = cleaned[1:]
        if symbol.isdigit():
            address = int(symbol)
        else:
            if symbol not in symbol_table:
                symbol_table[symbol] = next_variable_address
                next_variable_address += 1
            address = symbol_table[symbol]
        binary = decbin(address)
        output_lines.append(binary)
        continue
    dest = None
    comp = None
    jump = None
    if '=' in cleaned:
        dest, rest = cleaned.split('=', 1)
    else:
        dest = None
        rest = cleaned
    if ';' in rest:
        comp, jump = rest.split(';', 1)
    else:
        comp = rest
        jump = None
    comp = comp.strip()
    dest = dest.strip() if dest else "null"
    jump = jump.strip() if jump else "null"
    compb_code = comp_table.get(comp)
    dest_code = dest_table.get(dest, "000")
    jump_code = jump_table.get(jump, "000")
    if compb_code:
        binary = "111" + compb_code + dest_code + jump_code
        output_lines.append(binary)
    else:
        output_lines.append(original_line) 
with open("Sum.hack", "w") as file:
    for line in output_lines:
        file.write(line + '\n')
print("Saving to:", os.path.abspath("Sum.hack"))
print("Saving to:", os.path.abspath("Sum.txt"))