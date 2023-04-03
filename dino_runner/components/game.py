import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, CLOUD, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud1 = 900
        self.y_pos_cloud1 = 80
        self.x_pos_cloud2 = 250
        self.y_pos_cloud2 = 80-34
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        # dibuja el piso
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        #debug
        #print(self.x_pos_bg, end = " ")
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        #debug
        #print(image_width + self.x_pos_bg, end=" ")
        if self.x_pos_bg <= -image_width:
            # esta linea es inutil
            #self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
            self.x_pos_cloud1 = 900
            self.x_pos_cloud2 = 250
        #actual line of code that changes self.x_pos_bg
        self.x_pos_bg -= self.game_speed       
        self.screen.blit(CLOUD, (self.x_pos_cloud1, self.y_pos_cloud1))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud1, self.y_pos_cloud1))
        self.screen.blit(CLOUD, (self.x_pos_cloud2, self.y_pos_cloud2))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud2, self.y_pos_cloud2))
        #debug
        #print(self.x_pos_cloud1, self.x_pos_cloud2)
        self.x_pos_cloud1 -= self.game_speed
        self.x_pos_cloud2 -= self.game_speed
        
    