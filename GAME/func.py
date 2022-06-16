import pygame
from Model.player import Player 
from Model.playerBullet import PlayerBullet

def bullet_Hit_Player(predator,victim,bullets):

        #collision des bullets avec la victime
        hit_On_P1= pygame.sprite.spritecollide(victim,bullets,True)
        if hit_On_P1:
            # predator.updateScore(200)
            # print(predator.name+" : ",predator.score)
            print("predator damage: ",predator.damage)
            victim.get_damage(predator.damage)
            print("victime life: ", victim.currentLife)
            # print(victim.name+ " touché par un bullet")
            # victim.decreaseHP(predator.Dmg)
            # print(victim.HP)
            # victim.respawn(predator)