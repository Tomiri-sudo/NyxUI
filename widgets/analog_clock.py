import pygame
import math
import datetime

class AnalogClock:
    def __init__(self, center, radius, clock_color=(255, 255, 255)):
        self.center = center  # Tuple (x, y)
        self.radius = radius
        self.clock_color = clock_color

    def draw(self, surface):
        # Draw clock circle
        pygame.draw.circle(surface, self.clock_color, self.center, self.radius, 2)

        now = datetime.datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        # Calculate angles for each hand (in radians)
        second_angle = math.radians(second * 6 - 90)
        minute_angle = math.radians(minute * 6 - 90)
        hour_angle = math.radians((hour + minute / 60) * 30 - 90)

        # Hand lengths
        sec_length = self.radius * 0.9
        min_length = self.radius * 0.75
        hour_length = self.radius * 0.5

        # Endpoints of the hands
        sec_end = (self.center[0] + sec_length * math.cos(second_angle),
                   self.center[1] + sec_length * math.sin(second_angle))
        min_end = (self.center[0] + min_length * math.cos(minute_angle),
                   self.center[1] + min_length * math.sin(minute_angle))
        hour_end = (self.center[0] + hour_length * math.cos(hour_angle),
                    self.center[1] + hour_length * math.sin(hour_angle))

        # Draw hands
        pygame.draw.line(surface, (255, 0, 0), self.center, sec_end, 2)
        pygame.draw.line(surface, (0, 255, 0), self.center, min_end, 4)
        pygame.draw.line(surface, (0, 0, 255), self.center, hour_end, 6)
