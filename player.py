from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game): 
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angel = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angel)
        cos_a = math.cos(self.angel)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx = dx + speed_cos
            dy = dy + speed_sin
        if keys[pg.K_s]:
            dx = dx - speed_cos
            dy = dy - speed_sin
        if keys[pg.K_a]:
            dx = dx + speed_sin
            dy = dy - speed_cos
        if keys[pg.K_d]:
            dx = dx - speed_sin
            dy = dy + speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angel -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angel += PLAYER_ROT_SPEED * self.game.delta_time
        self.angel %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y + dy)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.line(self.game.screen, "yellow", (self.x * 100, self.y * 100),
                    (self.x * 100 + WIDTH * math.cos(self.angel), 
                    self.y * 100 + WIDTH * math.sin(self.angel)), 2)
        pg.draw.circle(self.game.screen, "green", (self.x *100, self.y * 100), 15)                
    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    