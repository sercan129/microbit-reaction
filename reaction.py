# Add your Python code here. E.g.
from microbit import *
from random import randrange

delay=1500 #ms
factor=.85

def choose_player():
    east_player = randrange(0,1)
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

    delay = delay * factor
    for i in range(3):
        display.show(Image.SQUARE)
        sleep(100)
        display.clear()
