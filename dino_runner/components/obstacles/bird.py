from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):

    def __init__(self):
        self.image = BIRD[0]        
        super().__init__(self.image)
        self.rect.y = 220
        self.step_counter = 0

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.image = BIRD[0] if self.step_counter < 5 else BIRD[1]
        self.step_counter += 1
        if self.step_counter > 10:
            self.step_counter = 0

    
        