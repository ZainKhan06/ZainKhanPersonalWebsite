# Hack Assembler for nand2tetris

Converts Hack assembly `.asm` files into machine code `.hack` files.

## Run

```bash
python3 HackAssembler.py Add.asm
```

This creates:

```text
Add.hack
```

## Supports

- A-instructions: `@2`, `@i`, `@SCREEN`
- C-instructions: `D=A`, `M=D+1`, `0;JMP`
- Labels: `(LOOP)`
- Variables starting at RAM address 16
- Predefined symbols: `R0`-`R15`, `SP`, `LCL`, `ARG`, `THIS`, `THAT`, `SCREEN`, `KBD`

## Example

```asm
@2
D=A
@3
D=D+A
@0
M=D
```
