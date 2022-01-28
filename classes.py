import pygame
import os
import random

window = WIDTH, HEIGHT = 750, 750

WOOD_1 = pygame.transform.scale(pygame.image.load
                            (os.path.join("./Sprites/tiles/wood_1.png")), (WIDTH/14, HEIGHT/12))
WOOD_2 = pygame.transform.scale(pygame.image.load(os.path.join("./Sprites/tiles/wood_2.png")), (WIDTH/14, HEIGHT/12))
WOOD_3 = pygame.transform.scale(pygame.image.load(os.path.join("./Sprites/tiles/wood_3.png")), (WIDTH/14, HEIGHT/12))
WOOD_4 = pygame.transform.scale(pygame.image.load(os.path.join("./Sprites/tiles/wood_4.png")), (WIDTH/14, HEIGHT/12))
RAT = pygame.transform.scale(pygame.image.load
                             (os.path.join("./Sprites/rat/rat_1.png")),(WIDTH/14, HEIGHT/12))
BG = pygame.transform.scale(pygame.image.load
                            (os.path.join("./Sprites/tiles/grass_1.png")), (WIDTH, HEIGHT))
CAT = pygame.image.load(os.path.join("./Sprites/cat/cat_1.png"))


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
LEFT_COLLIDE = 0
RIGHT_COLLIDE = 1
TOP_COLLIDE = 2
BOTTOM_COLLIDE = 3


def collide(obj1, obj2):
    offset_x = (obj2.x + 2) - obj1.x
    offset_y = (obj2.y + 2) - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def draw_grid(img):
    GAP = 3
    for i in range(9):
        WIN.blit(img.block_img, (img.x + img.get_width() + GAP, img.y))

    def collision(self, obj):
        return collide(self, obj)

class Rat:
    def __init__(self, x, y, hits=1):
        self.x = x
        self.y = y
        self.hits = hits
        self.rat_img = RAT
        self.mask = pygame.mask.from_surface(self.rat_img)
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.vel = 7
        self.angle = 0

    def get_width(self):
        return self.rat_img.get_width()

    def get_height(self):
        return self.rat_img.get_height()

    def get_rect(self):
        return self.rat_img.get_rect()

    def draw(self, window):
        window.blit(self.rat_img, (self.x, self.y))


    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.rect.x = self.x
        self.rect.y = self.y




    def collision(self, obj):
        return collide(self, obj)

    def rotate(self, angle):
        if self.angle != angle:
            act_angle = angle - self.angle
            self.angle = angle
            self.rat_img = pygame.transform.rotate(self.rat_img, act_angle)

    def collide_dir(self, rect: pygame.Rect):
        block_rect = rect
        if block_rect.collidepoint(self.rect.midleft):
            return LEFT_COLLIDE
        elif block_rect.collidepoint(self.rect.midbottom):
            return BOTTOM_COLLIDE
        elif block_rect.collidepoint(self.rect.midtop):
            return TOP_COLLIDE
        elif block_rect.collidepoint(self.rect.midright):
            return RIGHT_COLLIDE
        else:
            return 4


class Block:
    def __init__(self, x, y):
        wood = [WOOD_1, WOOD_2, WOOD_3, WOOD_4]
        self.x = x
        self.y = y
        self.block_img = wood[random.randint(0, 3)]
        self.mask = pygame.mask.from_surface(self.block_img)
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.can_move = False

    def get_width(self):
        return self.block_img.get_width()

    def get_height(self):
        return self.block_img.get_height()

    def get_rect(self):
        return self.block_img.get_rect()

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.rect.x = self.x
        self.rect.y = self.y

    def collide_dir(self, rect: pygame.Rect):
        rat_rect = rect
        if rat_rect.collidepoint(self.rect.midleft):
            return LEFT_COLLIDE
        elif rat_rect.collidepoint(self.rect.midbottom):
            return BOTTOM_COLLIDE
        elif rat_rect.collidepoint(self.rect.midtop):
            return TOP_COLLIDE
        elif rat_rect.collidepoint(self.rect.midright):
            return RIGHT_COLLIDE
        else:
            return 4





    def draw(self, window):
        GAP = 3
        WIN.blit(self.block_img, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.get_width(), self.get_height())
        # pygame.draw.rect(WIN, (255, 0, 0), self.hitbox, 2)  # temp hitbox

    def collision(self, obj):
        return collide(self, obj)