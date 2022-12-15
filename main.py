import sys, pygame
pygame.init()

size = width, height = 320*2, 240*2
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
vel = 10
x = 200

class rect():
    def __init__(self):
        pass



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
       x-=vel
    if keys[pygame.K_RIGHT]and x<width-20:
        x += vel
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (x,height-50,60,10))
    clock.tick(60)
    pygame.display.update()

