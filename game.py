# Menu created by Miguel Castro

import sys,pygame
import main as m
# Configuration
pygame.init()
fps = 60
fpsclock = pygame.time.Clock()
width, height = 1200, 800
scr = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Arial', 40)


buttons = []

#yeah dude trust me i totally know how to do oop and totally didnt yank this from the internet  - miguelillo
# It's gonna be fine - Django
class Button():
    def __init__(self, x, y, width, height, function, buttonText='Button', items=0, onePress=False, eqspace=False):
        self.x = x
        self.y = y
        self.width = width
        print('1')
        self.height = height
        self.onePress = onePress
        self.alreadyPressed = False
        self.function = function
        self.items = items
        self.eqspace = eqspace
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        buttons.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.function(self.items, self.eqspace)
                elif not self.alreadyPressed:
                    self.function(self.items, self.eqspace)
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        scr.blit(self.buttonSurface, self.buttonRect)


def startGame(Nsats, eqspace):
    m.main(Nsats, eqspace)


def main():
    Button(x=30, y=550, width=300, height=100, buttonText='Level 1',function=startGame, items=5)
    Button(x=width - 30 - 300, y=550, width=300, height=100, buttonText='Level 2', function=startGame, items=15, eqspace=True)
    Button(x=30, y=700, width=300, height=100, buttonText='Level 3',function=startGame, items=50)
    Button(x=width - 30 - 300, y=700, width=300, height=100, buttonText='PC go brrrr', function=startGame, items=1000)
    while True:
        scr.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for object in buttons:
            object.process()
        pygame.display.flip()
        fpsclock.tick(fps)

if __name__ == '__main__':
    main()

