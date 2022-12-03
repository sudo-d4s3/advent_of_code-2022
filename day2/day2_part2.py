#!/bin/env python3

f = open('input','r')
strat = f.read().split('\n')
strat.pop(-1)

win = 0
loss = 0
draw = 0
points = 0

def funcLoss(ans):
    global loss, points
    loss += 1
    if ans == 'A': # Rock
        points += 0 + 3 # Loss + Scissors
    elif ans == 'B': # Paper
        points += 0 + 1 # Loss + Rock
    elif ans == 'C': # Scissors
        points += 0 + 2 # Loss + Paper

def funcDraw(ans):
    global draw, points
    draw += 1
    if ans == 'A': # Rock
        points += 3 + 1 # Draw + Rock
    elif ans == 'B': # Paper
        points += 3 + 2 # Draw + Paper
    elif ans == 'C': # Scissors
        points += 3 + 3 # Draw + Scissors

def funcWin(ans):
    global win, points
    win += 1
    if ans == 'A': # Rock
        points += 6 + 2 # Win + Paper
    elif ans == 'B': # Paper
        points += 6 + 3 # Win + Scissors
    elif ans == 'C': # Scissors
        points += 6 + 1 # Win + Rock

for x in strat:
    if x[2] == 'X': # Loss
        funcLoss(x[0])
    elif x[2] == 'Y': # Draw
        funcDraw(x[0])
    elif x[2] == 'Z': # Win
        funcWin(x[0])

print("Score: " + str(points))
print("Wins: " + str(win))
print("Losses: " + str(loss))
print("Draws: " + str(draw))
