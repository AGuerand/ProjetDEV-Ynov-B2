import pygame, sys
from Model.player import Player
from func import bullet_Hit_Player
from Model.playerBullet import PlayerBullet
import sqlite3


#Constants
WIDTH, HEIGHT = 800, 500
TITLE = "Super game"

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


#pygame initialization
pygame.init()
Best_User = ('1')
windw = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHOOTHIM")
clock = pygame.time.Clock()
icon = pygame.image.load('Img\military.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Img/fond-de-bitume-une-bande-contrôle-101097202.jpg')

all_sprites = pygame.sprite.Group() # tous les sprites
bullets_p1=pygame.sprite.Group() # la sprite des bulletes du joueur 1 
bullets_p2=pygame.sprite.Group() # la sprite des bulletes du joueur 2
#Player Initialization (/2 => center screen)
player = Player(WIDTH/2, HEIGHT/2)
player2 = Player(WIDTH/3, HEIGHT/3)
all_sprites.add(player) # ajout du joueur 1 dans le groupe des sprites
all_sprites.add(player2) # ajout du joueur 2 dans le groupe des sprites

player_bullets = []

player_bullets = []

#initialize controller
pygame.joystick.init()

joystick1 = pygame.joystick.Joystick(0)
joystick1.init()

joystick2 = pygame.joystick.Joystick(1)
joystick2.init()

pygame.font.init() # you have to call this at the start, 

#Main Loop
while True:
    windw.fill((0, 0, 0))
    windw.blit(background, (0, 0))
    # windw.blit(player.currentLife, (1, (255,255,0)))
    # windw.blit(player2.currentLife, (2, (255,255,0)))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # for event in pygame.event.get():
    #     if event.type == pygame.JOYAXISMOTION:
    #          print(event)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if player.currentLife == 0:
            #ICI AJOUTER LA FUNC DATA
            Best_User = ('2')
            cursor.execute('INSERT INTO score VALUES (?)', Best_User)

            connection.commit()
            # print the first
            cursor.execute("SELECT * FROM score")
            connection.close()
            pygame.quit()
        if player2.currentLife == 0:
            #ICI AJOUTER LA FUNC DATA
            Best_User = ('1')
            cursor.execute('INSERT INTO score VALUES (?)', Best_User)

            connection.commit()
            # print the first
            cursor.execute("SELECT * FROM score")
            connection.close()
            pygame.quit()

        #player 1 movement
        if event.type == pygame.JOYAXISMOTION:
            if event.value < 0.2 and event.value > -0.2 and event.joy == 1:
                player.leftright = event.value
                player.updown = event.value

            if event.joy == 1 and event.axis == 1 and event.value == 1:
                player.leftright = event.value
                player.orientation = "left"

            if event.joy == 1 and event.axis == 1 and event.value < 0:
                player.leftright = event.value
                player.orientation = "right"

            if event.joy == 1 and event.axis == 0 and event.value == 1:
                player.updown = event.value
                player.orientation = "down"

            if event.joy == 1 and event.axis == 0 and event.value < 0:
                player.updown = event.value
                player.orientation = "up"

        #player 1 shoot bullets
        if event.type == pygame.JOYBUTTONDOWN:
            if joystick2.get_button(5):
                bullets_p1.add(PlayerBullet(player.x, player.y, player.orientation))

        #player 2 movement
        if event.type == pygame.JOYAXISMOTION:
            if event.value < 0.2 and event.value > -0.2 and event.joy == 0:
                player2.leftright = event.value
                player.updown = event.value

            if event.joy == 0 and event.axis == 1 and event.value == 1:
                player2.leftright = event.value
                player2.orientation = "left"

            if event.joy == 0 and event.axis == 1 and event.value < 0:
                player2.leftright = event.value
                player2.orientation = "right"

            if event.joy == 0 and event.axis == 0 and event.value == 1:
                player2.updown = event.value
                player2.orientation = "down"

            if event.joy == 0 and event.axis == 0 and event.value < 0:
                player2.updown = event.value
                player2.orientation = "up"

        #Player 2 shots bullets
        if event.type == pygame.JOYBUTTONDOWN:
            if joystick1.get_button(5):
                bullets_p2.add(PlayerBullet(player2.x, player2.y,player2.orientation))
        
    #Draw 
    # player.draw(windw)
    # player2.draw(windw)

    # for bullet in player_bullets:
    #     bullet.main(windw)

    #update

    all_sprites.draw(windw) #affichage des sprites
    bullets_p1.update()
    bullets_p2.update()
    all_sprites.update()
    bullet_Hit_Player(player, player2, bullets_p1)
    bullet_Hit_Player(player2, player, bullets_p2)
    bullets_p1.draw(windw) #affichage des sprites bullets du joueur 1
    bullets_p2.draw(windw) #affichage des sprites bullets du joueur 2
    player.showLife(windw, 10, 10)
    player2.showLife(windw, 490, 10)
    # player.update()
    # player2.update()
    pygame.display.flip()

    clock.tick(60)




# label = myfont.render("Some text!", 1, (255,255,0))
#     windowSurface.blit(label, (100, 100))


#backGroundColor=pygame.Color("LIGHTBLUE")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
#carryOn = True
 
# The clock will be used to control how fast the screen updates
#clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
#while carryOn:
    # --- Main event loop
    #for event in pygame.event.get(): # User did something
     #   if event.type == pygame.QUIT: # If user clicked close
         #     carryOn = False # Flag that we are done so we can exit the while loop
 
     # --- Game logic should go here
 
     # --- Drawing code should go here
     # First, clear the screen to white. 
   # screenSize.fill(backGroundColor)
     #The you can draw different shapes and lines or add text to your background stage.
 #   pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
  #""  pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
   # pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
    #over here you color the screen

 
 
     # --- Go ahead and update the screen with what we've drawn.
 #   pygame.display.flip()
     
     # --- Limit to 60 frames per second
   # clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
#pygame.quit()