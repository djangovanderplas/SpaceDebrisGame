# Menu created by Miguel Castro

import sys,pygame
import main as m
# Configuration
pygame.init()
pygame.font.init()
fps = 60
fpsclock = pygame.time.Clock()
width, height = 1200, 800
scr = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Courier New', 40)
logo = pygame.image.load('assets/Logo.png')
logo = pygame.transform.scale(logo, (600,350))
background = pygame.image.load('assets/background.png')

buttons = []

#yeah dude trust me i totally know how to do oop and totally didnt yank this from the internet  - miguelillo
# It's gonna be fine - Django
class Button():
    def __init__(self, x, y, width, height, function, buttonText='Button', items=0, onePress=False, eqspace=False):
        self.x = x
        self.y = y
        self.width = width
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
    scr.blit(background,(0,0))
    text_list = ['Commander, I have bad news! The Russians just ','shot the ISS and large pieces of debris are ','threatening to come down on earth!','  It\'s up to you to control our Space Garbage','Collector. But make sure not to crash with the','Russian military satellites! That won\'t be good.']
    label = []
    for line in text_list:
        label.append(font.render(line,True,(255,255,255)))
    scr.blit(label[0],pygame.Rect(50,150,600,800))
    pygame.display.flip()
    scr.blit(label[1],pygame.Rect(70,200,600,800))
    pygame.display.flip()
    scr.blit(label[2],pygame.Rect(180,250,600,800))
    pygame.display.flip()
    scr.blit(label[3],pygame.Rect(30,300,600,800))
    pygame.display.flip()
    scr.blit(label[4],pygame.Rect(30,350,600,800))
    pygame.display.flip()
    scr.blit(label[5],pygame.Rect(20,400,600,800))
    pygame.display.flip()
    pygame.time.wait(1000)
    while True:
        scr.fill((20, 20, 20))
        scr.blit(logo, (300,80))
        scr.blit(background,(0,0))
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

