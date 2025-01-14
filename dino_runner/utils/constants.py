import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

KOOPA_TROOPA = [
    pygame.image.load(os.path.join(IMG_DIR,"Mario/koopa troopa izquierda.png"))
]

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SKIN1 = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1-aren32.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2-aren32.png"))
]

RUNNING_SKIN2 = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1-MarioHat.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2-MarioHat.png"))
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_WEAPON1 = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Weapon1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Weapon1.png"))
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_WEAPON = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpWeapon1.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_WEAPON1 = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Weapon1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png"))
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
WEAPON = pygame.image.load(os.path.join(IMG_DIR,"Weapon/weapon1.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Other/bullet.png"))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
WEAPON_TYPE = "weapon"
FONT_STYLE = [
    "freesansbold.ttf",
    os.path.join(IMG_DIR, "Fonts/Nice Sugar.ttf")
]

COLORS = {
    "black": (0,0,0),
    "white": (255,255,255)
}

MUSIC = [
    os.path.join(IMG_DIR, "Music/Powerful-Trap-.mp3")
]