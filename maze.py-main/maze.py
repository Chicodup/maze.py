from random import choice
from pygame import *
init()
mixer.init()
mixer.music.load('jungles.ogg')
#mixer.music.play()
mixer_music.set_volume(0.2)
#створи вікно гри;
MAP_WIDTH, MAP_HEIGHT = 25,20
TILESIZE = 33
WIDTH,HEIGHT =MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE
window = display.set_mode((WIDTH,HEIGHT))
FPS = 60
clock = time.Clock()
#задай фон сцени
bg = image.load('background.jpg')
bg = transform.scale(bg,(MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE))
cyborg_img = image.load("cyborg.png")
player_img = image.load("hero.png")
wall_img = image.load("wall.png")
gold_img = image.load("treasure.png")
all_sprites = sprite.Group()

#створи 2 спрайти та розмісти їх на сцені
class Sprite(sprite.Sprite):
    def __init__(self,sprite_img,width,height,x,y):
        super().__init__()
        self.image = transform.scale(sprite_img, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = mask.from_surface(self.image)
        all_sprites.add(self)

class Player(Sprite):
    def __init__(self,sprite_img,width,height,x,y):
        super().__init__(sprite_img,width,height,x,y)
        self.hp = 100
        self.speed = 5
    def update(self):
        key_pressed = key.get_pressed()
        old_pos = self.rect.x, self.rect.y
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s]and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_a]and self.rect.left > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d]and self.rect.right < WIDTH:
            self.rect.x += self.speed

        collide_list = sprite.spritecollide(self,walls,False,sprite.collide_mask)
        if len(collide_list) > 0:
            self.rect.x, self.rect.y = old_pos

class Enemy(Sprite):
    def __init__(self,sprite_img,width,height,x,y):
        super().__init__(sprite_img,width,height,x,y)
        self.damage = 100
        self.speed = 5
        self.dir_list = ["right","left","up","down"]
        self.dir = choice(self.dir_list)
    def update(self):
        if self.dir == "right":
            self.rect.x += self.speed
        elif self.dir == "left":
            self.rect.x -= self.speed
        elif self.dir == "up":
            self.rect.y -= self.speed
        elif self.dir == "down":
            self.rect.y += self.speed

player = Player(player_img,TILESIZE-5,TILESIZE-5,300,300)
walls = sprite.Group()
enemys = sprite.Group()




with open("map.txt", "r") as f:
    map = f.readlines()
    x = 0
    y = 0
    for line in map:
        for symwol in line:
            if symwol == "w":
                walls.add(Sprite(wall_img, TILESIZE,TILESIZE,x,y))
            if symwol == "p":
                player.rect.x = x
                player.rect.y = y
            if symwol == "g":
                walls.add(Sprite(gold_img, 70,70,x,y))
            if symwol == "e":
                enemys.add(Enemy(cyborg_img, TILESIZE,TILESIZE,x,y))
            x += TILESIZE
        y+=TILESIZE
        x = 0

#оброби подію «клік за кнопкою "Закрити вікно"»
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(bg, (0,0))
    all_sprites.draw(window)
    all_sprites.update()

    display.update()
    clock.tick(FPS)