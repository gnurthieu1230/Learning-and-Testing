### Các hàm và biến của ngôn ngữ Assembly ###
# 1. Các kích thước ô nhớ cơ bản (Data Sizes / Directives)
DB / BYTE = Define Byte
DW / WORD = Define Word
DD / DWORD = Define Double Word
DQ / QWORD = Define Quad Word
DT / TWORD = Define Ten Bytes

# 2. Các loại Thanh ghi (Registers - "Biến" siêu tốc nằm ngay trong CPU)
RAX = Accumulator
RBX = Base
RCX = Counter
RDX = Data
RSI = Source Index
RDI = Destination Index
RBP = Base Pointer
RSP = Stack Pointer
R8 --> R15

# 3. Các lệnh thao tác dữ liệu cơ bản (Basic Instructions - Thay thế cho Hàm)
MOV = Move
ADD / SUB = Add / Subtract
MUL / DIV = Multiply / Divide
INC / DEC = Increment / Decrement
PUSH / POP = Push / POP
CMP = Compare
JMP / JE / JNE = Jump / Jump Equal...
CALL / RET = Call / Return
INT / SYSCALL = Interrupt / System Call
