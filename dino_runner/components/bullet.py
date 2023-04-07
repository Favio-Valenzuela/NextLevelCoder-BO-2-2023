from pygame.sprite import Sprite

from dino_runner.utils.constants import (
    BULLET,
    SCREEN_WIDTH,
)

class Bullet(Sprite):
    def __init__(self,player):
        self.image = BULLET
        self.rect = self.image.get_rect()
        self.rect.center = (player.rect.right, player.rect.top+(player.rect.bottom-player.rect.top)/2 )

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, bullet_speed, bullets):
        self.rect.x += bullet_speed
        if self.rect.x > SCREEN_WIDTH:            
            bullets.remove(self)
