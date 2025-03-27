import pygame

class SeekBar:
    def __init__(self, rect, max_value=100, current_value=0, bg_color=(100, 100, 100), fg_color=(200, 50, 50)):
        self.rect = pygame.Rect(rect)
        self.max_value = max_value
        self.current_value = current_value
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.dragging = False

    def handle_event(self, event):
        """Handle mouse events to update the seekbar value."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                self.set_value_from_pos(event.pos[0])
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.set_value_from_pos(event.pos[0])

    def set_value_from_pos(self, x_pos):
        """Calculate and set the value based on the x position of the mouse."""
        relative_x = x_pos - self.rect.x
        percentage = relative_x / self.rect.width
        self.current_value = max(0, min(int(percentage * self.max_value), self.max_value))

    def draw(self, surface):
        """Draw the seekbar."""
        pygame.draw.rect(surface, self.bg_color, self.rect)
        fill_width = int((self.current_value / self.max_value) * self.rect.width)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill_width, self.rect.height)
        pygame.draw.rect(surface, self.fg_color, fill_rect)
