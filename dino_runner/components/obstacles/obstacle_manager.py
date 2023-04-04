import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.koopa_troopa import KoopaTroopa
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):        
        if len(self.obstacles) == 0:
            obstacle_class = random.randint(0,2)
            if obstacle_class == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
                #debug
                #print(type(self.obstacles[0]) )
            elif obstacle_class == 1:
                self.obstacles.append(Bird())
            elif obstacle_class == 2:
                self.obstacles.append(KoopaTroopa())
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)                
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(2000) #poner 2000 ms
                game.playing = False
                break
            

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)