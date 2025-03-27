import pygame
import math
import datetime
import os

class AnalogClock:
    def __init__(self, center, radius, clock_color=(255, 255, 255), number_color=(255, 255, 255)):
        self.center = center  # Tuple (x, y)
        self.radius = radius
        self.clock_color = clock_color
        self.number_color = number_color
        self.font = self.load_font()

    def load_font(self):
        # Load system font from the fonts folder (Inter-Regular.ttf)
        path = os.path.join("fonts", "Inter-Regular.ttf")
        return pygame.font.Font(path, int(self.radius * 0.15))  # Font size proportional to clock radius

    def draw(self, surface):
        # Draw clock circle
        pygame.draw.circle(surface, self.clock_color, self.center, self.radius, 2)
        
        # Draw clock numbers (1 to 12)
        for num in range(1, 13):
            angle = math.radians(num * 30 - 90)
            # Place numbers at 80% of radius
            number_radius = self.radius * 0.8
            x = self.center[0] + number_radius * math.cos(angle)
            y = self.center[1] + number_radius * math.sin(angle)
            number_text = self.font.render(str(num), True, self.number_color)
            text_rect = number_text.get_rect(center=(x, y))
            surface.blit(number_text, text_rect)
        
        now = datetime.datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        # Calculate angles for the hands
        second_angle = math.radians(second * 6 - 90)
        minute_angle = math.radians(minute * 6 - 90)
        hour_angle = math.radians((hour + minute / 60) * 30 - 90)

        # Hand lengths
        sec_length = self.radius * 0.9
        min_length = self.radius * 0.75
        hour_length = self.radius * 0.5

        # Endpoints for each hand
        sec_end = (int(self.center[0] + sec_length * math.cos(second_angle)),
                   int(self.center[1] + sec_length * math.sin(second_angle)))
        min_end = (int(self.center[0] + min_length * math.cos(minute_angle)),
                   int(self.center[1] + min_length * math.sin(minute_angle)))
        hour_end = (int(self.center[0] + hour_length * math.cos(hour_angle)),
                    int(self.center[1] + hour_length * math.sin(hour_angle)))

        # Draw hands
        pygame.draw.line(surface, (255, 0, 0), self.center, sec_end, 2)
        pygame.draw.line(surface, (0, 255, 0), self.center, min_end, 4)
        pygame.draw.line(surface, (0, 0, 255), self.center, hour_end, 6)
