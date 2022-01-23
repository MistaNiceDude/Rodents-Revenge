import pygame
import os
import time
import random
from pygame import key
pygame.font.init()
pygame.init()

run = True
pygame.display.set_caption("Rodents Rebooted")

window = WIDTH, HEIGHT = 750, 750
screen = pygame.display.set_mode(window)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rodents Rebooted")

RAT = pygame.transform.scale(pygame.image.load
                             (os.path.join("/Users/rodneythompson/PycharmProjects/Rodents_revenge/Sprites/rat/rat_1.png")),(WIDTH/14, HEIGHT/12))
BG = pygame.transform.scale(pygame.image.load
                            (os.path.join("/Users/rodneythompson/PycharmProjects/Rodents_revenge/Sprites/tiles/grass_1.png")), (WIDTH, HEIGHT))
CAT = pygame.image.load(os.path.join("/Users/rodneythompson/PycharmProjects/Rodents_revenge/Sprites/cat/cat_1.png"))
WOOD_1 = pygame.transform.scale(pygame.image.load
                            (os.path.join("/Users/rodneythompson/PycharmProjects/Rodents_revenge/Sprites/tiles/wood_1.png")), (WIDTH/14, HEIGHT/12))
WOOD_2 = pygame.image.load(os.path.join("/Users/rodneythompson/PycharmProjects/Rodents_revenge/Sprites/tiles/wood_2.png"))
WOOD_3 = pygame.image.load(os.path.join("/Users/rodneythompson/PycharmProjects/Rodents_revenge/Sprites/tiles/wood_3.png"))
WOOD_4 = pygame.image.load(os.path.join("/Users/rodneythompson/PycharmProjects/Rodents_revenge/Sprites/tiles/wood_4.png"))


wood = [WOOD_1, WOOD_2, WOOD_3, WOOD_4]
#wood = WOOD_1


class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.block_img = WOOD_1
        self.mask = pygame.mask.from_surface(self.block_img)
        block_box = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())

    def get_width(self):
        return self.block_img.get_width()

    def get_height(self):
        return self.block_img.get_height()

    def draw(self,window):
        window.blit(self.block_img, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.get_width(), self.get_height())
        #pygame.draw.rect(WIN, (255, 0, 0), self.hitbox, 2)  # temp hitbox

    def collision(self, obj):
        return collide(self, obj)



class Rat:
    def __init__(self, x, y, hits = 1):
        self.x = x
        self.y = y
        self.hits = hits
        self.rat_img = RAT
        self.mask = pygame.mask.from_surface(self.rat_img)
        self.angle = 0
        rat_box = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        #self.hitbox = (self.x, self.y, self.get_width(),self.get_height())


    def get_width(self):
        return self.rat_img.get_width()

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            pygame.transform.rotate(self.rat_img, 90)
        #elif keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:
            #player.x += player_vel
        #elif keys[pygame.K_w] and player.y - player_vel > 0:
            #player.y -= player_vel
        #elif keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:
            #player.y += player_vel

    #def rotate(self, angle):
        #return pygame.transform.rotate(self.rat_img, angle)

    def get_height(self):
        return self.rat_img.get_height()

    def draw(self,window):
        window.blit(self.rat_img, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.get_width(), self.get_height())
        #pygame.draw.rect(WIN,(255,0,0),self.hitbox, 2) #temp hitbox

    def collision(self, obj):
        return collide(self, obj)




def collide(obj1,obj2):
    offset_x = (obj2.x + 2) - obj1.x
    offset_y = (obj2.y + 2) - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    run = True
    FPS = 50
    hits = 3
    level = 0
    hits_font = pygame.font.SysFont("comicsans", 30)
    level_font = pygame.font.SysFont("comicsans", 30)
    player_vel = 7
    clock = pygame.time.Clock()
    player = Rat(WIDTH/2, HEIGHT/2)
    wood = Block(WIDTH/4,HEIGHT/4)
    clock_font= pygame.font.SysFont("impact", 20)

    def redraw_window():
        WIN.blit(BG, (0,0))
        player.draw(WIN)
        wood.draw(WIN)
        hits_label = hits_font.render(f"Hits: {hits}", 1, (149,11,9))
        level_label = level_font.render(f"Level: {level}", 1, (149,11,9))
        clock_label = clock_font.render(f"FPS: {clock}", 1, (149,11, 9))

        WIN.blit(hits_label, (20,20))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 20))
        WIN.blit(clock_label, ( 20,HEIGHT - clock_label.get_height() - 20,))
        #screen.blit(RAT, (WIDTH/2, HEIGHT/2))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        collision = collide(player, wood)
        if collision == True:
            if player.y > wood.y + wood.get_height()/2 - 10:
                wood.y -= player_vel
            elif player.y < wood.y - wood.get_height()/2 + 10:
                wood.y += player_vel
            elif player.x > wood.x + wood.get_width()/2 + 10:
                wood.x -= player_vel
            elif player.x < wood.x - wood.get_width()/2 - 10:
                wood.x += player_vel



#changing if to elif constrains to one direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        elif keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        elif keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        elif keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel


main()



pygame.quit()
