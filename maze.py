from pygame import *

init()
mixer.init()
mixer.music.load('jungles.ogg')
#mixer.music.play()
mixer_music.set_volume(0.2)
#створи вікно гри;
WIDTH,HEIGHT = 700,500
window = display.set_mode((WIDTH,HEIGHT))
FPS = 60
clock = time.Clock()
#задай фон сцени
bg = image.load('background.jpg')
bg = transform.scale(bg,(700,500))
player_img = image.load("hero.png")
player_img2 = image.load("cyborg.png")
all_sprites = sprite.Group()

#створи 2 спрайти та розмісти їх на сцені
class Sprite(sprite.Sprite):
    def __init__(self,sprite_img,width,height,x,y):
        super().__init__()
        self.image = transform.scale(sprite_img, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_sprites.add(self)

class Player(Sprite):
    def __init__(self,sprite_img,width,height,x,y):
        super().__init__(sprite_img,width,height,x,y)
        self.hp = 100
        self.speed = 4
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s]and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_a]and self.rect.left > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d]and self.rect.right < WIDTH:
            self.rect.x += self.speed

        
player = Player(player_img,70,70,300,300)
player2 = Player(player_img2,70,70,300,400)

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