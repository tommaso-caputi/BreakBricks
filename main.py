import sys, pygame
pygame.init()

size = width, height = 320*2, 240*2
screen = pygame.display.set_mode(size)
rect = pygame.Rect(50, 60, 20, 8)
vel = 1
x = 200
y = 200

i=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
       x-=vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    rect.move_ip(x,y)

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (x,y,20,8))
    pygame.display.flip()