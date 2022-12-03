#!/bin/env python3

f = open('input','r')
strat = f.read().split('\n')
strat.pop(-1)

win = 0
loss = 0
draw = 0
points = 0

for x in strat:
    if x[2] == 'X': # Rock
        points += 1
        if x[0] == 'A': # Rock; Draw
            points += 3
            draw += 1
        elif x[0] == 'B': # Paper; Loss
            points += 0
            loss += 1
        elif x[0] == 'C': # Scissors; Win
            points += 6
            win += 1
    elif x[2] == 'Y': # Paper
        points += 2
        if x[0] == 'A': # Rock; Win
            points += 6
            win += 1
        elif x[0] == 'B': # Paper; Draw
            points += 3
            draw += 1
        elif x[0] == 'C': # Scissors; Loss
            points += 0
            loss += 1
    elif x[2] == 'Z': # Scissors 
        points += 3
        if x[0] == 'A': # Rock; Loss
            points += 0
            loss += 1
        elif x[0] == 'B': # Paper; Win
            points += 6
            win += 1
        elif x[0] == 'C': # Scissors; Draw
            points += 3
            draw += 1

print("Score: " + str(points))
print("Wins: " + str(win))
print("Losses: " + str(loss))
print("Draws: " + str(draw))
