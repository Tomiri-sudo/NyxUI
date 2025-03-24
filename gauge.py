import pygame
import math

class Gauge:
    def __init__(self, center, radius,
                 min_val=0, max_val=100, redline=80,
                 base_color=(128, 128, 128),
                 needle_color=(0, 255, 0), needle_size=2,
                 font=None, name=""):
        self.center = center
        self.radius = radius
        self.min_val = min_val
        self.max_val = max_val
        self.redline = redline
        self.base_color = base_color
        self.needle_color = needle_color
        self.needle_size = needle_size
        self.font = font  # path to a TTF font file; can be used for drawing labels.
        self.name = name  # label to be displayed in the center of the gauge.
        self.value = min_val  # start at the minimum value

        # Update the angle range:
        # Map min_val to 0° and max_val to 270°.
        self.start_angle = 0
        self.end_angle = 270

    def set_value(self, value):
        # Clamp the value within [min_val, max_val]
        self.value = max(self.min_val, min(self.max_val, value))

    def render(self, surface):
        # Draw the gauge base (a circle)
        pygame.draw.circle(surface, self.base_color, self.center, self.radius, 2)

        # Compute the angle for the current value.
        angle = self._value_to_angle(self.value)
        end_pos = (
            self.center[0] + self.radius * math.cos(math.radians(angle)),
            self.center[1] - self.radius * math.sin(math.radians(angle))
        )
        # Draw the needle for the current value.
        pygame.draw.line(surface, self.needle_color, self.center, end_pos, self.needle_size)

        # Draw the redline marker.
        red_angle = self._value_to_angle(self.redline)
        red_end = (
            self.center[0] + self.radius * math.cos(math.radians(red_angle)),
            self.center[1] - self.radius * math.sin(math.radians(red_angle))
        )
        pygame.draw.line(surface, (255, 0, 0), self.center, red_end, self.needle_size)

        # Draw the gauge name label in the center with a downward offset.
        if self.name:
            # Use provided font or default system font.
            font_to_use = pygame.font.Font(self.font, int(self.radius / 3)) if self.font else pygame.font.SysFont(None, int(self.radius / 3))
            text_surface = font_to_use.render(self.name, True, self.base_color)
            text_rect = text_surface.get_rect(center=(self.center[0], self.center[1] + 10))
            surface.blit(text_surface, text_rect)

    def _value_to_angle(self, value):
        # Map the given value linearly to the gauge’s angle range (0 to 270 degrees)
        ratio = (value - self.min_val) / (self.max_val - self.min_val)
        angle = self.start_angle + ratio * (self.end_angle - self.start_angle)
        return angle
