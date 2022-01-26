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
                             (os.path.join("./Sprites/rat/rat_1.png")),(WIDTH/14, HEIGHT/12))
BG = pygame.transform.scale(pygame.image.load
                            (os.path.join("./Sprites/tiles/grass_1.png")), (WIDTH, HEIGHT))
CAT = pygame.image.load(os.path.join("./Sprites/cat/cat_1.png"))
WOOD_1 = pygame.transform.scale(pygame.image.load
                            (os.path.join("./Sprites/tiles/wood_1.png")), (WIDTH/14, HEIGHT/12))
WOOD_2 = pygame.transform.scale(pygame.image.load(os.path.join("./Sprites/tiles/wood_2.png")), (WIDTH/14, HEIGHT/12))
WOOD_3 = pygame.transform.scale(pygame.image.load(os.path.join("./Sprites/tiles/wood_3.png")), (WIDTH/14, HEIGHT/12))
WOOD_4 = pygame.transform.scale(pygame.image.load(os.path.join("./Sprites/tiles/wood_4.png")), (WIDTH/14, HEIGHT/12))

wood = [WOOD_1, WOOD_2, WOOD_3, WOOD_4]
#wood = WOOD_1
LEFT_COLLIDE = 0
RIGHT_COLLIDE = 1
TOP_COLLIDE = 2
BOTTOM_COLLIDE = 3

class Block:
    wood = [WOOD_1, WOOD_2, WOOD_3, WOOD_4]
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.block_img = wood[random.randint(0,3)]
        self.mask = pygame.mask.from_surface(self.block_img)
        block_box = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.can_move = False

    def get_width(self):
        return self.block_img.get_width()

    def get_height(self):
        return self.block_img.get_height()
     
    def get_rect(self):
        return self.block_img.get_rect()

    def draw(self,window):
        GAP = 3
        WIN.blit(self.block_img, (self.x, self.y))
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
        self.rect = pygame.Rect(self.rat_img.get_rect())
        self.vel = 7
        self.angle = 0 

        #self.hitbox = (self.x, self.y, self.get_width(),self.get_height())


    def get_width(self):
        return self.rat_img.get_width()

    def get_height(self):
        return self.rat_img.get_height()

    def get_rect(self):
        return self.rat_img.get_rect()
        

    def draw(self,window):
        window.blit(self.rat_img, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.get_width(), self.get_height())
        #pygame.draw.rect(WIN,(255,0,0),self.hitbox, 2) #temp hitbox



    def collision(self, obj):
        return collide(self, obj)

    def rotate(self, angle):
        if self.angle != angle:
            act_angle = angle - self.angle
            self.angle = angle
            self.rat_img = pygame.transform.rotate(self.rat_img, act_angle)

    def collide_dir(self, surface: pygame.Surface):

        rect = surface.get_rect()
        if self.rat_img.get_rect().collidepoint(rect.midright):
            return LEFT_COLLIDE
        elif self.rat_img.get_rect().collidepoint(rect.midtop):
            return BOTTOM_COLLIDE
        elif self.rat_img.get_rect().collidepoint(rect.midbottom):
            return TOP_COLLIDE
        elif self.rat_img.get_rect().collidepoint(rect.midleft):
            return RIGHT_COLLIDE
        else:
            return 4

        

  # def update(self):
  #      self.image = pygame.transform.rotate(self.rat_img, self.angle)
  #      self.angle += 1 % 360
  #      x, y = self.rect
  #      self.rect = self.rat_img_rect()
  #      self.rect.center = (x.y)



def collide(obj1,obj2):
    offset_x = (obj2.x + 2) - obj1.x
    offset_y = (obj2.y + 2) - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None



def draw_grid(img, size):
    GAP = 3
    for i in range(9):
        WIN.blit(img.block_img, (img.x + img.get_width() + GAP, img.y))

        
    def collision(self, obj):
        return collide(self, obj)







def main():
    run = True
    FPS = 60
    hits = 3
    level = 0
    hits_font = pygame.font.SysFont("comicsans", 30)
    level_font = pygame.font.SysFont("comicsans", 30)
    player_vel = 7
    clock = pygame.time.Clock()
    player = Rat(WIDTH/2, HEIGHT/2)
    wood = Block(WIDTH/4,HEIGHT/4)
    clock_font= pygame.font.SysFont("impact", 20)
    player_pos = (player.x, player. y)

    def redraw_window():
        #Since the window is the thing drawing everything, fill it blank before every redraw to avoid
        #   that pesky issue where colored rects stay drawn in black/background corners.
        WIN.fill(0)
        WIN.blit(BG, (0,0))
        player.rect = player.rect.move(1, 0)
        player.draw(WIN)
        wood.draw(WIN)
        draw_grid(wood)

        
        #pygame.draw.rect(WIN, pygame.color.Color(200, 0, 0), player.rect)
        hits_label = hits_font.render(f"Hits: {hits}", 1, (149,11,9))
        level_label = level_font.render(f"Level: {level}", 1, (149,11,9))
        clock_label = clock_font.render(f"FPS: {clock}", 1, (149,11, 9))

        WIN.blit(hits_label, (20,20))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 20))
        WIN.blit(clock_label, ( 20,HEIGHT - clock_label.get_height() - 20,))
        #WIN.blit(player.rect)
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
            if player.y > wood.y + wood.get_height()/2 - 10 and wood.y > 0:
                wood.y -= player_vel
            elif player.y < wood.y - wood.get_height()/2 + 10 and  wood.y + wood.get_height() < HEIGHT:
                wood.y += player_vel
            elif player.x > wood.x + wood.get_width()/2 + 10 and wood.x > 0:
                wood.x -= player_vel
            elif player.x < wood.x - wood.get_width()/2 - 10 and wood.x + wood.get_width() < WIDTH:
                wood.x += player_vel



#changing if to elif constrains to one direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            Rat.rotate(player, 90)
            current_pos = player.x
            player.x -= player_vel
            #if player.collide_dir(wood) == LEFT_COLLIDE:
                #player.x = current_pos
                
        elif keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:
            Rat.rotate(player, 270)
            current_pos = player.x
            player.x += player_vel
            #if player.collide_dir(wood) == RIGHT_COLLIDE:
                #player.x = current_pos
        elif keys[pygame.K_w] and player.y - player_vel > 0:
            Rat.rotate(player, 0)
            player.y -= player_vel
        elif keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:
            Rat.rotate(player, 180)
            player.y += player_vel

main()

pygame.quit()

