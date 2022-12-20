import sys, pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BreakBricks')
clock = pygame.time.Clock()

class rect():
    def __init__(self):
        self.y = height-50
        self.x = width/2
        self.vel = 10   
    def keys_handler(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and self.x>0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]and self.x<width-20:
            self.x += self.vel

class ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = [2,2]
    def update_dir(self):
        if self.x>=width or self.x == 0:
            self.dir[0] = -self.dir[0]
        if self.y>=height-50 or self.y == 0:
            self.dir[1] = -self.dir[1]
    def update_pos(self):
        self.x += self.dir[0]
        self.y += self.dir[1]
        if self.y >= height-50 and not(self.x >= player.x and self.x <= player.x+60):
            print("Game over")
            sys.exit(0)
        else:
            self.update_dir()
    def get_pos(self):
        return self.x, self.y


balls = [ball(width/2,height/2)]
player = rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    player.keys_handler()
    
    screen.fill((0,0,0))
    for ball in balls:
        ball.update_pos()
        pygame.draw.circle(screen, (255,255,255), ball.get_pos(), 3)
    pygame.draw.rect(screen, (255,255,255), (player.x, height-50, 60, 10))
    clock.tick(60)
    pygame.display.update()

