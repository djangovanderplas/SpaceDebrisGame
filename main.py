# Game created by Django van der Plas for AE1205 competition on 31-05-2022
# Game Art created by Miguel Castro

import view, gameobjects    # import other files
import pygame, random

pygame.init()

# Set up window and game options
fps = 60
clock = pygame.time.Clock()
xmax, ymax = 1200, 800
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

def main(Ndebris, eqspace=False):
    running = True
    userquit = False

    ### Declaration and setup of game objects
    # Planet
    earth = gameobjects.Planet(r=6371000, x=xmax/2, y=ymax/2, m=5.9e24)
    # Player sat:
    sat = gameobjects.Satellite(theta=0, size=4, alt=1000000, color=BLUE, thetadot=0.001, m=50, planet=earth, scr=scr) #theta, size, alt, thetadot, m, planet
    sat.InitControl()
    # Debris
    debris_list = []
    nsats = []
    if eqspace:
        for debris in range(0, Ndebris):
            debris_list.append(gameobjects.Debris(theta=debris*(2*3.14/Ndebris), size=3, alt=3500000+random.random()*1000000., color=ORANGE, thetadot=0.00055+random.random()*0.0001, m=50, planet=earth, scr=scr))  # theta, size, alt, thetadot, m, planet
    else:
        for debris in range(0, Ndebris):
            debris_list.append(gameobjects.Debris(theta=0, size=3, alt=3500000+random.random()*1000000., color=ORANGE, thetadot=0.00055+random.random()*0.0001, m=50, planet=earth, scr=scr))  # theta, size, alt, thetadot, m, planet
    for nsat in range(0, round(Ndebris/5)):
        nsats.append(gameobjects.NoTouchSat(theta=nsat*(2*3.14/round(Ndebris/5)), size=5, alt=3000000+random.random()*2000000, color=RED, thetadot=0.00055+random.random()*0.0001, m=50, planet=earth, scr=scr))

    # For equispaced debris:
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
            for nsat in nsats:
                nsat.physics(fps)
                nsat.checkCollision(planet=earth, sat=sat)
                if not nsat.active:
                    nsats.remove(nsat)

        sat.UserInput(0.00001) #This number changes max thrust of the satellite

        # Draw elements

        scr.blit(background,(0,0)) 
        sat.draw(scr)
        earth.draw(scr,earthimg)
        for debris in debris_list:
            debris.draw(scr)
        for nsat in nsats:
            nsat.draw(scr)
        view.flip(fps, clock)


    # Close window on stop condition
    view.closewindow()


