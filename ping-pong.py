from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (size_x, size_y))
        self.speed = speed
        self.rect  = (self.image.get_rect())
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
window.fill(back)

mixer.init()
mixer.music.load('back_music.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)

clock = time.Clock()
FPS = 60

game = True
finish = False

player1 = Player('racket.png', 30, 200, 4, 50, 150)
player2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)

        player1.update_1()
        player2.update_2()
    
        player1.reset()
        player2.reset()
        ball.reset()

    display.update()

    clock.tick(FPS)
