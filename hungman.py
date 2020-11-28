import random
word = ["veren", "keigo", "banana", "orange", "aho", "bodoh"]

def hangman(word):
    wrong = 0
    stages = ["",
              "_________        ",
              "|                ",
              "|        |       ",
              "|        O       ",
              "|      / | \     ",
              "        / \      ",
              "                 "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to HUNGMAN!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
            print("".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print("Answer is " + "".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! Answer is {}.".format(word))

hangman(word[random.randint(0, len(word))])