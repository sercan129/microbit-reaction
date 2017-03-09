from microbit import *
from random import randrange
score=0
delay=1500 #ms
factor=.85

def choose_player():
    east_player = randrange(0,2)
    if east_player:
        display.show(Image.ARROW_E)
    else:
        display.show(Image.ARROW_W)
    return east_player

def correct_button_pressed(echosen):
    if echosen and button_b.was_pressed():
        return True
    elif echosen == 0 and button_a.was_pressed():
        return True
    else:
        return False

while delay > 1:
    echosen = choose_player()
    sleep(delay)
    if correct_button_pressed(echosen) == False:
        display.scroll("your score is "+str(score))
        break
    else:
        score=score+1
