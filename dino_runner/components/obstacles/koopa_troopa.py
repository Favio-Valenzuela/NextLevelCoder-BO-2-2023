

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import KOOPA_TROOPA


class KoopaTroopa(Obstacle):
    def __init__(self):
        self.image = KOOPA_TROOPA[0]
        super().__init__(self.image)
        self.rect.y = 300