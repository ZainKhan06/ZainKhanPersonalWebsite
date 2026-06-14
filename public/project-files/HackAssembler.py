#!/usr/bin/env python3
import sys
import os

PREDEFINED = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
}

for i in range(16):
    PREDEFINED[f"R{i}"] = i

DEST = {
    None: "000",
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

JUMP = {
    None: "000",
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

COMP = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "A+D": "0000010",
    "D+M": "1000010",
    "M+D": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "A&D": "0000000",
    "D&M": "1000000",
    "M&D": "1000000",
    "D|A": "0010101",
    "A|D": "0010101",
    "D|M": "1010101",
    "M|D": "1010101",
}


def clean_line(line: str) -> str:
    line = line.split("//", 1)[0]
    return line.strip().replace(" ", "")


def load_instructions(path: str) -> list[str]:
    instructions = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            cleaned = clean_line(line)
            if cleaned:
                instructions.append(cleaned)
    return instructions


def first_pass(instructions: list[str]) -> tuple[list[str], dict[str, int]]:
    symbols = dict(PREDEFINED)
    rom_address = 0
    real_instructions = []

    for instruction in instructions:
        if instruction.startswith("(") and instruction.endswith(")"):
            label = instruction[1:-1]
            symbols[label] = rom_address
        else:
            real_instructions.append(instruction)
            rom_address += 1

    return real_instructions, symbols


def translate_a_instruction(instruction: str, symbols: dict[str, int], next_var: list[int]) -> str:
    value = instruction[1:]

    if value.isdigit():
        address = int(value)
    else:
        if value not in symbols:
            symbols[value] = next_var[0]
            next_var[0] += 1
        address = symbols[value]

    if address < 0 or address > 32767:
        raise ValueError(f"A-instruction address out of range: {instruction}")

    return format(address, "016b")


def translate_c_instruction(instruction: str) -> str:
    if "=" in instruction:
        dest_part, rest = instruction.split("=", 1)
    else:
        dest_part, rest = None, instruction

    if ";" in rest:
        comp_part, jump_part = rest.split(";", 1)
    else:
        comp_part, jump_part = rest, None

    if comp_part not in COMP:
        raise ValueError(f"Unknown comp field '{comp_part}' in instruction: {instruction}")
    if dest_part not in DEST:
        raise ValueError(f"Unknown dest field '{dest_part}' in instruction: {instruction}")
    if jump_part not in JUMP:
        raise ValueError(f"Unknown jump field '{jump_part}' in instruction: {instruction}")

    return "111" + COMP[comp_part] + DEST[dest_part] + JUMP[jump_part]


def assemble_file(input_path: str) -> str:
    if not input_path.endswith(".asm"):
        raise ValueError("Input file must end with .asm")

    output_path = input_path[:-4] + ".hack"
    raw_instructions = load_instructions(input_path)
    instructions, symbols = first_pass(raw_instructions)
    next_var = [16]

    machine_code = []
    for instruction in instructions:
        if instruction.startswith("@"):
            machine_code.append(translate_a_instruction(instruction, symbols, next_var))
        else:
            machine_code.append(translate_c_instruction(instruction))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(machine_code))
        f.write("\n")

    return output_path


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 HackAssembler.py Prog.asm")
        sys.exit(1)

    input_path = sys.argv[1]
    try:
        output_path = assemble_file(input_path)
        print(f"Wrote {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
