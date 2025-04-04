# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2   

    player = Player(x, y)
    astroField = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                sys.exit("Game over!")
            for bullet in shots:
                if bullet.checkCollision(asteroid):
                    bullet.kill()
                    asteroid.split()

        pygame.Surface.fill(screen, color = "black")

        dt = clock.tick(60) / 1000

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip() # Call last in loop

if __name__ == "__main__":
    main()

