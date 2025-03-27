import pygame

class ProgressBar:
    def __init__(self, rect, max_value=100, current_value=0, bg_color=(50, 50, 50), fg_color=(0, 200, 0)):
        self.rect = pygame.Rect(rect)
        self.max_value = max_value
        self.current_value = current_value
        self.bg_color = bg_color
        self.fg_color = fg_color

    def update(self, value):
        """Update the current value (clamped between 0 and max_value)."""
        self.current_value = max(0, min(value, self.max_value))

    def draw(self, surface):
        """Draw the progress bar on the given surface."""
        # Draw background
        pygame.draw.rect(surface, self.bg_color, self.rect)
        # Calculate filled width
        fill_width = int((self.current_value / self.max_value) * self.rect.width)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill_width, self.rect.height)
        # Draw foreground
        pygame.draw.rect(surface, self.fg_color, fill_rect)
