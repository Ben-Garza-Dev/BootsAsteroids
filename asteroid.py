import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        asteroid_one_speed = pygame.math.Vector2(self.velocity.x, self.velocity.y)
        asteroid_two_speed = pygame.math.Vector2(self.velocity.x, self.velocity.y)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector_one = asteroid_one_speed.rotate(angle)
            vector_two = asteroid_two_speed.rotate(-angle) 
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = vector_one * 1.2
            asteroid_two.velocity = vector_two * 1.2