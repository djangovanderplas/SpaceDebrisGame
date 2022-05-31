# Game created by Django van der Plas for AE1205 competition on 31-05-2022
# Game Art created by Miguel Castro

import view, gameobjects    # import other files
import pygame, random

pygame.init()

# Set up window and game options
fps = 60
clock = pygame.time.Clock()
xmax, ymax = 800, 800
scr = view.openwindow(xmax, ymax)
font = pygame.font.SysFont('Arial', 20)
SpeedScale = 100

#Load images
earthimg = pygame.image.load('assets/earth.png')
earthimg = pygame.transform.scale(earthimg, (270,270)) #Scaling eyeballed. But it works. So...
background = pygame.image.load('assets/background.png')

#Colors
RED = (245, 96, 66)
ORANGE = (217, 127, 30)
BLUE = (52, 140, 235)

def main(Ndebris):
    running = True
    userquit = False

    ### Declaration and setup of game objects
    # Planet
    earth = gameobjects.Planet(r=6371000, x=xmax/2, y=ymax/2, m=5.9e24)
    # Player sat:
    sat = gameobjects.Sat(theta=0, size=5, alt=1000000, color=BLUE, thetadot=0.001, m=50, planet=earth, scr=scr) #theta, size, alt, thetadot, m, planet
    sat.InitControl()
    # Debris
    debris_list = []
    for debris in range(0, Ndebris):
        debris_list.append(gameobjects.Sat(theta=0, size=3, alt=3500000+random.random()*1000000., color=ORANGE, thetadot=0.0006+random.random()*0.0001, m=50, planet=earth, scr=scr))  # theta, size, alt, thetadot, m, planet
    # For equispaced debris: theta=debris*(2*3.14/Ndebris)
    ### Main Loop
    while running:
        # Check running conditions:
        if userquit:
            running = False
        view.checkEvents()
        view.clr(scr)
        if not sat.active:
            userquit = True

        # Handle physics
        for i in range(0, SpeedScale): #runs the simulation SpeedScale times per frame
            sat.physics(fps)
            sat.checkCollision(planet=earth, sat=sat)
            for debris in debris_list:
                debris.physics(fps)
                debris.checkCollision(planet=earth, sat=sat)
                if not debris.active:
                    debris_list.remove(debris)
        sat.UserInput(0.00001) #This number changes max thrust of the satellite

        # Draw elements

        scr.blit(background,(0,0)) 
        sat.draw(scr)
        earth.draw(scr,earthimg)
        for debris in debris_list:
            debris.draw(scr)
        view.flip(fps, clock)


    # Close window on stop condition
    view.closewindow()

if __name__ == '__main__':
    main(20)

