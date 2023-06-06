#Rock, Paper, Scissors
import sys
import random



print('Rock, Paper, Scissors')

wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    while True:
        print ('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q')

    if playerMove == 'r':
        print ('Rock versus...')
    if playerMove == 'p':
        print('Paper versus...')
    if playerMove == 's':
        print('Scissors versus...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    if randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    if randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    if playerMove == computerMove:
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose')
        losses = losses + 1