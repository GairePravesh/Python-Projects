import os
import pygame
import random
class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.width, self.height = 800, 600
        self.x=self.width
        self.y=self.height
        self.throw = True
        self.cut = False
        self.n=0
        self.score=0
        self.life=6
        self.fell = False
        pygame.font.init()
        #self.start_ticks = pygame.time.get_ticks()

    def on_init(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size,pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.image.load('Background.jpg')
        self.background = pygame.transform.scale(self.background, self.size)
        self.screen.blit(self.background, (0, 0))
        pygame.mixer.music.load('bg_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.load_images()
        self.load_sounds()
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        #pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
        self.Images = {
            0: [self.apple, self.apple_1, self.apple_2],
            1: [self.banana, self.banana_1, self.banana_2],
            2: [self.basaha, self.basaha_1, self.basaha_2],
            3: [self.peach, self.peach_1, self.peach_2],
            4: [self.sandia, self.sandia_1, self.sandia_2]
        }
        self.on_execute()
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    def on_loop(self):
        self.screen.blit(self.background, (0, 0))
        x,y=pygame.mouse.get_pos()
        rect=self.Images[self.n][0].get_rect()
        self.screen.blit(self.sword, (x-20, y-20))
        if not self.cut:
            self.screen.blit(self.Images[self.n][0], (self.x, self.y))
            self.life_score()
            pygame.display.update()

        if not self.cut and (x > self.x and x < (self.x + rect[2])) and (y > self.y and y < (self.y + rect[3])):
            pygame.mixer.Sound.play(self.splatter)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Images[self.n][1],(x-25,y-25))
            self.screen.blit(self.Images[self.n][2],(x+25,y+25))
            #self.screen.blit(self.flash, (x - 150, y+25))
            self.life_score()
            self.screen.blit(self.splash, (x, y))
           # pygame.display.update()
            #pygame.time.wait(0)
            #self.screen.blit(self.background, (0, 0))
            pygame.display.update()
            self.cut = True
            self.score += 1
            pygame.time.delay(500)



    def load_images(self):
        self.apple = pygame.image.load('apple.png')
        self.apple_1 = pygame.image.load('apple-1.png')
        self.apple_2 = pygame.image.load('apple-2.png')
        self.banana = pygame.image.load('banana.png')
        self.banana_1 = pygame.image.load('banana-1.png')
        self.banana_2 = pygame.image.load('banana-2.png')
        self.basaha = pygame.image.load('basaha.png')
        self.basaha_1 = pygame.image.load('basaha-1.png')
        self.basaha_2 = pygame.image.load('basaha-2.png')
        self.peach = pygame.image.load('peach.png')
        self.peach_1 = pygame.image.load('peach-1.png')
        self.peach_2 = pygame.image.load('peach-2.png')
        self.sandia = pygame.image.load('sandia.png')
        self.sandia_1 = pygame.image.load('sandia-1.png')
        self.sandia_2 = pygame.image.load('sandia-2.png')
        self.boom = pygame.image.load('boom.png')
        self.flash = pygame.image.load('flash.png')
        self.lose = pygame.image.load('lose.png')
        self.splash = pygame.image.load('Splash.png')
        self.game_over = pygame.image.load('game_over.png')
        self.sword = pygame.image.load('sword.png')
    def load_sounds(self):
        self.boomm = pygame.mixer.Sound('boom.ogg')
        self.splatter = pygame.mixer.Sound('splatter.ogg')
        self.throws = pygame.mixer.Sound('throw.ogg')
    def throw_objects(self):
        pygame.mixer.Sound.play(self.throws)
        self.n = random.randint(0, 4)
        self.x = random.randint(210,500)
        self.y = random.randint(50,600)
        if not self.cut:
            self.life -= 1
            #pygame.mixer.Sound.play(self.boomm)
        self.cut = False
        #print("Thrown")
    def life_score(self):
        x,y=30,30
        for i in range(self.life+1):
            self.screen.blit(self.lose,(x,y))
            y+=100
        if self.life < 0:
            #print("game over")
            self.score=0
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.game_over,(265,300))
            pygame.display.update()
            pygame.mixer.Sound.play(self.boomm)
            pygame.time.delay(3000)
            self.life = 5
        myFont=pygame.font.SysFont('Comic Sans MS',50)
        text=myFont.render('Score : '+str(self.score),False,(255,255,255))
        self.screen.blit(text,(270,10))

    def on_execute(self):
        xamount=10
        yamount=5
        while( self.running ):
            #print(xamount,yamount)
            for event in pygame.event.get():
                self.on_event(event)
            if self.throw:
                #xamount = random.choice([-10,10])
                self.throw_objects()
                self.throw = False
                #print("throwing")
                #self.x = random.randint(0,self.height)
            if self.y < 50:
                yamount = -yamount

            if (self.y > self.height) or self.cut:
                self.throw_objects()
                xamount = 10
                yamount = 5

            if self.x < 200:
                xamount = -xamount
            if self.x > 520:
                xamount = -xamount
            self.on_loop()
            self.y -= yamount
            self.x -= xamount
            #print(self.score)
            # time = ( pygame.time.get_ticks() - self.start_ticks ) / 1000
            # # if time % 2 == 0:
            # #     xamount += 1
            # #     yamount += 1
            self.clock.tick(60)
            #print(xamount,yamount)

if __name__ == '__main__':
    game = App()
    game.on_init()
