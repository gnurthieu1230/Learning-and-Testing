### Các hàm và biến của ngôn ngữ Assembly ###
# 1. Các kích thước ô nhớ cơ bản (Data Sizes / Directives)
DB / BYTE = Define Byte
DW / WORD = Define Word
DD / DWORD = Define Double Word
DQ / QWORD = Define Quad Word
DT / TWORD = Define Ten Bytes

# 2. Các loại Thanh ghi (Registers - "Biến" siêu tốc nằm ngay trong CPU)
RAX = Register Accumulator
RBX = Register Base
RCX = Register Counter
RDX = Register Data
RSI = Register Source Index
RDI = Register Destination Index
RBP = Register Base Pointer
RSP = Register Stack Pointer
RIP = Register Instruction Pointer
R8 --> R15

# 3. Các lệnh thao tác dữ liệu cơ bản (Basic Instructions - Thay thế cho Hàm)
MOV = Move
ADD / SUB = Add / Subtract
MUL / IMUL = Multiply / Integer Multiply
LEA = Load Effective Address
DIV / IDIV = Divide / Integer Divide
INC / DEC = Increment / Decrement
PUSH / POP = Push onto Stack / POP off Stack
CMP = Compare
JMP = Jump
JE / JZ = Jump Equal / Jump Zero
JNE / JNZ = Jump Not Equal / Jump Not Zerở
JG / JL = Jump Greater / Jump Less
CALL / RET = Call / Return
INT / SYSCALL = Interrupt / System Call
