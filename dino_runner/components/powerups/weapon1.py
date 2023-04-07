from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import (
    WEAPON,
    WEAPON_TYPE,
)

class Weapon1(PowerUp):
    def __init__(self):
        self.image = WEAPON
        self.type = WEAPON_TYPE
        super().__init__(self.image,self.type)
