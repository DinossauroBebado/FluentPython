
# 1
board = [["_"]*3 for i in range(3)]
print(board)


# diferente de
# 2
BOARD = [["_"]*3]*3

print(BOARD)

# nesse caso tds as linhas são alias e se referem ao msm objeto

BOARD[1][2] = "X"

board[1][2] = "0"

print(board)
print(BOARD)
print("------------------------------")
# o ex 2 é equivalente a

row = ["_"] * 3
BOARD = []

for i in range(3):
    BOARD.append(row)

# o ex1

board = []
for i in range(3):
    row = ["_"] * 3
    board.append(row)

board[1][2] = "X"
BOARD[1][2] = "X"

print(board)
print(BOARD)
