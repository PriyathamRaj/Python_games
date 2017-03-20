
# coding: utf-8

# In[1]:

def drawboard(board):
    print('   |   |')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[2]:

def getletters():
    print('Do you want to be X? y or n')
    if input().lower().startswith('y'):
        playerletter, computerletter = ['X', 'O']
    else:
        playerletter, computerletter = ['O', 'X']
    return playerletter, computerletter


# In[3]:

def whogoesfirst():
    print('Do you want to go first? y or n')
    if input().lower().startswith('y'):
        return 'player'
    else:
        return 'computer'


# In[4]:

def getplayermove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not spaceisfree(board, move):
        print('What is your move? Choose from 1-9')
        move = input()
    return move


# In[5]:

def makemove(board, move, letter):
    board[move] = letter


# In[6]:

def iswinner(bo, le):
    return (bo[1] == bo[2] == bo[3] == le or
           bo[4] == bo[5] == bo[6] == le or
           bo[7] == bo[8] == bo[9] == le or
           bo[1] == bo[4] == bo[7] == le or
           bo[2] == bo[5] == bo[8] == le or
           bo[3] == bo[6] == bo[9] == le or
           bo[1] == bo[5] == bo[9] == le or
           bo[3] == bo[5] == bo[7] == le)


# In[7]:

def boardisfull(board):
    for i in range(1,10):
        if spaceisfree(board, i):
            return False
    return True


# In[8]:

import random
def randommove(board, list):
    possiblemoves = []
    for i in list:
        if spaceisfree(board, i):
            possiblemoves.append(i)
    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)


# In[13]:

def getcomputermove(board, computerletter):
    if computerletter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'
    
    k = 0
    for i in range(1,10):
        if spaceisfree(board, i):
            k += 1
    if k == 8:
        for i in [1,3,7,9]:
            if not spaceisfree(board, i):
                if spaceisfree(board, 5):
                    return 5
    
    for i in range(1,10):
        if spaceisfree(board, i):
            copy = board[:]
            makemove(copy, i, computerletter)
            if iswinner(copy, computerletter):
                return i
            
    for i in range(1,10):
        if spaceisfree(board, i):
            copy = board[:]
            makemove(copy, i, playerletter)
            if iswinner(copy, playerletter):
                return i
            
    move = randommove(board, [1,3,7,9])
    if move != None:
        return move
    if spaceisfree(board, 5):
        return 5
    
    return randommove(board, [2,4,6,8])


# In[14]:

def spaceisfree(board, move):
    return board[int(move)] == ' '


# In[15]:

def playagain():
    print('Do you want to play again? y or n')
    if input().lower().startswith('y'):
        return True


# In[16]:

while True:
    board = [' ']*10
    playerletter, computerletter = getletters()
    turn = whogoesfirst()
    playgoeson = True
    
    while playgoeson:
        if turn == 'player':
            drawboard(board)
            move = int(getplayermove(board))
            makemove(board, move, playerletter)
            
            if iswinner(board, playerletter):
                drawboard(board)
                print('You win!')
                playgoeson = False
                
            else:
                if boardisfull(board):
                    drawboard(board)
                    print('Its a draw.')
                    playgoeson = False
                else:
                    turn = 'computer'

        else:
            #turn = computer
            move = int(getcomputermove(board, computerletter))
            makemove(board, move, computerletter)
            
            if iswinner(board, computerletter):
                drawboard(board)
                print('You lose.')
                playgoeson = False
                
            else:
                if boardisfull(board):
                    drawboard(board)
                    print('Its a draw.')
                    playgoeson = False
                else:
                    turn = 'player'
    if not playagain():
        break
            


# In[ ]:



