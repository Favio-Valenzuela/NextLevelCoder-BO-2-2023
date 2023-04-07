

from dino_runner.components.bullet import Bullet
from dino_runner.utils.constants import WEAPON_TYPE


class BulletManager():
    def __init__(self):
        self.bullets = []
        self.bullet_speed = 20
        self.bullet_step = 0

    def draw(self,screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def update(self, game):
        bullet_flag = False
        if game.player.type == WEAPON_TYPE:            
            if self.bullet_step%5 == 0:
                self.bullets.append(Bullet(game.player))        
            self.bullet_step += 1
        for bullet in self.bullets[:]:
            bullet.update(self.bullet_speed, self.bullets)
            for obstacle in game.obstacle_manager.obstacles[:]:
                if bullet.rect.colliderect(obstacle.rect):
                    game.obstacle_manager.obstacles.remove(obstacle)
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    bullet_flag = True
                    break
            if bullet_flag:
                break
                    
            
    
