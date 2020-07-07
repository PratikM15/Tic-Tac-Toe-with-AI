import random
all_moves = []

def conditions(string):
    count = 0
    winner = None
    if (string[0] == string[1] == string[2]):
        count += 1
        winner = string[0]
    elif (string[3] == string[4] == string[5]):
        count += 1
        winner = string[3]
    elif (string[6] == string[7] == string[8]):
        count += 1
        winner = string[6]
    elif (string[0] == string[4] == string[8]):
        count += 1
        winner = string[0]
    elif (string[0] == string[3] == string[6]):
        count += 1
        winner = string[0]
    elif (string[1] == string[4] == string[7]):
        count += 1
        winner = string[1]
    elif (string[2] == string[5] == string[8]):
        count += 1
        winner = string[2]
    elif (string[2] == string[4] == string[6]):
        count += 1
        winner = string[2]
    if winner == 'X' or winner == 'O':
        return winner
    return None
        
def show(string):
    row1 = "| "+string[0]+" "+string[1]+" "+string[2]+" |"
    row2 = "| "+string[3]+" "+string[4]+" "+string[5]+" |"
    row3 = "| "+string[6]+" "+string[7]+" "+string[8]+" |"
    print("---------")
    print(row1)
    print(row2)
    print(row3)
    print("---------")

def result(string):
    winner = conditions(string)
    if winner != None:
        print("\n"+winner, "wins\n")
        return True
    elif "_" not in string:
        print("\nDraw\n")
        return True
    return False

def menu():
    while True:
        option = input("Input command: ")
        options = option.split()
        if option == 'exit':
            return 'exit', 'exit'
        elif len(options) == 3:
            player1 = options[1]
            player2 = options[2]
            return player1, player2
        else:
            print("Bad parameters!")
            
def ai_move():
    global all_moves
    while True:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        x = int(x) -1
        y = int(y) -1
        if [x, y] in all_moves:
            continue
        else:
            all_moves.append([x, y])
            return x, y
    

def user_move():
    global all_moves
    while True:
        x, y = input("Enter the coordinates : ").split()
        x = int(x) -1
        y = int(y) -1
        if [x, y] in all_moves:
            print("This cell is occupied! Choose another one!")
        elif 0 <= x < 3 and 0 <= y < 3:
            all_moves.append([x, y])
            return x, y 
        elif not (0 <= x < 3 and 0 <= y < 3):
            print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

def medium_move(string, move):
    if move == 'X':
        oppose = 'O'
    else:
        oppose = 'X'
    global all_moves
    
    for x in range(1, 4):
        for y in range(1, 4):
            x = int(x) -1
            y = int(y) -1
            if [x, y] in all_moves:
                continue
            else:
                row1 = [string[0], string[1], string[2]]
                row2 = [string[3], string[4], string[5]]
                row3 = [string[6], string[7], string[8]]
                moves = [row1, row2, row3]
                new_string = ""
                moves[x][y] = move
                for row in moves:
                    new_string += "".join(row)
                check = conditions(new_string)
                if check == move:
                    all_moves.append([x, y])
                    return x, y
                else:
                    moves[x][y] = oppose
                    for row in moves:
                        new_string += "".join(row)
                    check = conditions(new_string)
                    if check == move:
                        all_moves.append([x, y])
                        return x, y
    return ai_move()   
                    
    
            
                

def start_game(player1, player2):
    global all_moves
    string = "_________"
    show(string)
    all_moves = []
    for k in range(0, 9):
        if k % 2 == 0:
            if player1 == 'user':
                x, y = user_move()
            elif player1 == 'medium':
                print('Making move level "medium"')
                x, y = medium_move(string, 'X')
            elif player1 == 'hard':
                print('Making move level "hard"')
                x, y = medium_move(string, 'X')
            else:
                print('Making move level "easy"')
                x, y = ai_move()
            move = "X"
        else:
            if player2 == 'user':
                x, y = user_move()
            elif player2 == 'medium':
                print('Making move level "medium"')
                x, y = medium_move(string, 'O')
            elif player2 == 'hard':
                print('Making move level "hard"')
                x, y = medium_move(string, 'O')
            else:
                print('Making move level "easy"')
                x, y = ai_move()
            move = 'O'
        
        row1 = [string[0], string[1], string[2]]
        row2 = [string[3], string[4], string[5]]
        row3 = [string[6], string[7], string[8]]
        moves = [row1, row2, row3]
        new_string = ""
        moves[x][y] = move
        for row in moves:
            new_string += "".join(row)
        string = new_string
        show(string)
        check = result(string)
        if check == True:
            break

def main():
    while True:
        player1, player2 = menu()
        if player1 == player2 == 'exit':
            break
            return
        else:
            start_game(player1, player2)
            
main()
