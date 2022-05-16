import random
ask = input('Choose any one from Rock/Paper/Scissors - r/p/s: ')
rps = ['rock', 'paper', 'scissors']
computer = random.choice(rps)
if ask.lower() == 'rock' or ask.lower() == 'r':
    if computer == 'rock':
        print('You choose rock and i choose rock so its a tie!')
    if computer == 'paper':
        print('You choose rock and i choose paper so i won!')
    if computer== 'scissors':
        print('You choose rock and i choose scissors so you won!')
elif ask.lower() == 'paper' or ask.lower() == 'p':
    if computer == 'rock':
        print('You choose paper and i choose rock so you won!')
    if computer == 'paper':
        print('You choose paper and i choose paper so its a tie!')
    if computer== 'scissors':
        print('You choose paper and i choose scissors so i won!')
elif ask.lower() == 'scissors' or ask.lower() == 's':
    if computer == 'rock':
        print('You choose scissors and i choose rock so i won!')
    if computer == 'paper':
        print('You choose scissors and i choose paper so you won!')
    if computer== 'scissors':
        print('You choose scissors and i choose scissors so its a tie!')
else:
    print('Invalid Argument')