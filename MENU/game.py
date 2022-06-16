"""
pygame-menu
https://github.com/ppizarror/pygame-menu
EXAMPLE - SIMPLE
Super simple example of pygame-menu usage, featuring a selector and a button.
"""
import pygame
import sqlite3
import pygame_menu
from pygame.locals import *

from pygame_menu.examples import create_example_window

from typing import Tuple, Any
# create database
connection = sqlite3.connect('score.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS score
  (
     Name    TEXT
  ) 
	''')

# send to database multiple query
# Best_User = [('Tesla', 2020),
#              ('Kia', 2022),
#              ('Porsche', 2021)]
# cursor.executemany('INSERT INTO score VALUES (?,?)', Best_User)

# send to database one query
Best_User = ('1')
cursor.execute('INSERT INTO score VALUES (?)', Best_User)

connection.commit()
# print the first
cursor.execute("SELECT * FROM score")
# record = cursor.fetchone()
# print all
#record = cursor.fetchall()
# print a specific number of entry
record = cursor.fetchmany(2)

# loop to print line by line
# for records in record:
    #
    # print(record)

print(record)

connection.close()

# /create database

surface = create_example_window('Example - Simple', (600, 400))


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')

def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    GREEN = ( 0, 255, 0)
    RED = ( 255, 0, 0)

    size = (1024, 768)
    # screen = pygame.display.set_mode( (size), pygame.FULLSCREEN )
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My First Game")
    backGroundColor=pygame.Color("LIGHTBLUE")

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we can exit the while loop
    
        # --- Game logic should go here
    
        # --- Drawing code should go here
        # First, clear the screen to white. 
        screen.fill(backGroundColor)
        #The you can draw different shapes and lines or add text to your background stage.
        #  pygame.draw.rect(SURFACE, RGB_COLOR, (X, Y, WIDTH, HEIGHT))
        # pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
        #  pygame.draw.line(surface, color, start_pos, end_pos, width)
        # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        # pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
        pygame.draw.rect(screen, BLACK, [0, 0, 1024, 768],0)
        pygame.draw.line(screen, GREEN, [0, 0], [0, 1000], 5)
        pygame.draw.line(screen, GREEN, [340, 0], [340, 1000], 5)
        pygame.draw.line(screen, GREEN, [700, 0], [700, 1000], 5)
        pygame.draw.line(screen, GREEN, [1024, 0], [1024, 1000], 5)

        #over here you color the screen

    
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

    global user_name
    print(f'{user_name.get_value()}, Do the job here!')


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)
menu_score = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Database',
    width=400
)
for i in record:   
    menu_score.add.button("player"+str(i)+" WIn")
# user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
# menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('score', menu_score)
menu.add.button('Quit', pygame_menu.events.EXIT)
# database test

if __name__ == '__main__':
    menu.mainloop(surface)