# Handles all gameobjects of the game
import pygame, math

BLUE = (53, 189, 150)
GREEN = (116, 235, 52)
RED = (235, 73, 52)

scale = 50000
speed_scale=10
G = 6.674e-11

class Planet:
    def __init__(self, r, x, y, m):
        self.x = x
        self.y = y
        self.r = r
        self.m = m
        self.color = BLUE

    def draw(self, scr,earthimg):
        image_x = earthimg.get_width()
        image_y = earthimg.get_width()

        try:
            scr.blit(earthimg,((self.x-(image_x/2)),(self.y-(image_y)/2)))
        except:
            print('Failed to load earth image.')
            pygame.draw.circle(scr, self.color, (self.x, self.y), self.r/scale)

class Sat:
    def __init__(self, theta, size, color, alt, thetadot, m, planet, scr):
        ### Static Properties
        self.size = size
        self.m = m
        self.planet = planet
        self.color = color
        self.colorhistory = color
        self.control = False
        self.active = True

        ### Dynamic properties
        # Position
        self.r = alt + self.planet.r
        self.theta = theta
        # Velocity
        self.rdot = 0
        self.thetadot = thetadot
        # Accerleration
        self.rdotdot = 0
        self.thetadotdot = 0
        self.pgthrust = 0
        self.draw(scr)

    def draw(self, scr,satimg):
        # Determine screen coordinates
        if self.active:
            self.x = self.r/scale*math.cos(self.theta) + self.planet.x
            self.y = -self.r/scale*math.sin(self.theta) + self.planet.y

        # Draw sat
            pygame.draw.circle(scr, self.color, (self.x, self.y), self.size)

    def physics(self, fps):
        dt = 1/fps*speed_scale
        ### Dynamics
        # Accelerations
        self.rdotdot = - self.planet.m * G/(self.r**2)+self.r*self.thetadot**2
        self.thetadotdot = - 2 * self.rdot * self.thetadot / self.r + self.pgthrust/self.m
        # Velocity
        self.rdot += self.rdotdot * dt
        self.thetadot += self.thetadotdot * dt
        # Position
        self.r += self.rdot * dt
        self.theta += self.thetadot * dt

    def InitControl(self):
        self.control = True

    def UserInput(self, thrust):
        if self.control:
            keys = pygame.key.get_pressed()
            prograde = 0
            if keys[pygame.K_RIGHT]:
                prograde = 1
                self.color = GREEN
            elif keys[pygame.K_LEFT]:
                prograde = -1
                self.color = RED
            else:
                self.color = self.colorhistory
            self.pgthrust = thrust*prograde

    def checkCollision(self, planet, sat):
        distance = math.sqrt((self.x-sat.x)**2+(self.y-sat.y)**2)
        if not self.control:
            if distance < 10:
                self.active = False
        if self.r < planet.r:
            self.active = False
