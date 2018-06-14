import pygame
import random

def main():
    pygame.init()
    pygame.display.set_caption('Flappy Bird')
    x,y=800,600
    score=0
    screen = pygame.display.set_mode((x,y))
    run = True
    xpos,ypos = 200,200
    bird = pygame.image.load("bird.png")
    bird = pygame.transform.scale(bird,(50,50))
    upipe = pygame.image.load("upipe.png")
    dpipe = pygame.image.load("dpipe.png")
    pygame.font.init()
    myfont=pygame.font.SysFont('Comic Sans MS',30)
    clock=pygame.time.Clock()
    pygame.key.set_repeat(1,10)
    wup=[100,100]
    wdp=[100,100]
    x=[400,800]
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ypos -= 30
        
        screen.fill((255, 255, 255))
        screen.blit(bird,(xpos,ypos))
        for i in range(2):
            upipe = pygame.transform.scale(upipe, (50, wup[i]))
            dpipe = pygame.transform.scale(dpipe, (50, wdp[i]))
            screen.blit(upipe,(x[i],0))
            screen.blit(dpipe,(x[i],600-wdp[i]))
        
        #screen.blit(text, (0, 0))
        
            if (xpos > x[i] and xpos < (x[i]+50)) and (ypos < wup[i] or ypos > (600-wdp[i])):
                ypos=200
                if i:
                    x[i] = x[0]+400
                else:
                    x[i] = x[1]+400
                score = 0
                screen.fill((255, 0, 0))
                pygame.display.update()
                pygame.time.delay(100)
                screen.fill((255, 255, 255))
            if xpos==x[i]:
                score+=1
            if not ypos > 570:
                ypos += 5
            if ypos < 0 or ypos > 570:
                ypos = 200
                score=0
                screen.fill((255, 0, 0))
                pygame.display.update()
                pygame.time.delay(100)
                screen.fill((255, 255, 255))
                if i:
                    if x[0]<800:
                        x[i] = x[0]+400
                else:
                    if x[1]<800:
                        x[i] = x[1]+400
            if x[i] < 0:
                wup[i] = random.choice([50,75,100,125,150,175,200,225,250,300])
                wdp[i] = 400 - wup[i]
                if i:
                    x[i] = x[0]+400
                else:
                    x[i] = x[1]+400
            x[i]-=5
        scor="Score :"+str(int(score))
        text = myfont.render(scor, False, (0, 0, 0))
        screen.blit(text,(0,0))
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
