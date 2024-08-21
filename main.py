import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()
    dt = 0
    point = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = updatable, drawable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = updatable, drawable, asteroids

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = updatable, drawable, shots

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                print(f"Final Score: {point}")
                exit()
        
        #check for collisions between shots and asteroids
        #if a collision is detected, destroy both objects
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    point += asteroid.radius * 10
                    break

        #limit framrate to 60 fps
        dt = fps.tick(60) / 1000
        

if __name__ == "__main__":
    main()