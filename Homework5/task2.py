# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# 1 | 2 | X
# 4 | X | O
# X | 8 | O

victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]
        ]

def showBoard(board):
    for i in range(3):
        print(board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], end='\n')
    print()

def is_win(board):
    for v  in victory:
        if board[v[0]] == board[v[1]] == board[v[2]]:
            return board[v[0]]
    return False

def playerStep(player, sign):
    correct = False
    while not correct:
        player_step = int(input('Ход игрока ' + player+ ': '))
        if player_step >= 1 and player_step <= 9:
            if str(board[player_step-1]) not in 'XO':
                board[player_step-1] = sign
                correct = True
            else:
                print('Эта клетка уже занята')
        else:
            print('Некорректный ввод. Ввежите число от 1 до 9.')


board = list(range(1,10))

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
print()
showBoard(board)

counter = 0
win = False
while not win:
    if counter % 2 == 0:
        playerStep(player1, "X")
    else:
        playerStep(player2, "O")
    counter += 1
    end = is_win(board)
    if end=='X' or end=='O':
        if end == 'X':
            print('Игрок', player1, 'выиграл!')
        else:
            print('Игрок', player2, 'выиграл!')
        win = True
        break
    if counter == 9:
        print("Ничья!")
        break
    showBoard(board)
    