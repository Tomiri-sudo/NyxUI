import pygame

class ScrollFrame:
    def __init__(self, rect, content_size, bg_color=(30, 30, 30)):
        self.rect = pygame.Rect(rect)
        self.content_size = content_size  # (width, height) of the inner content
        self.bg_color = bg_color
        self.offset = [0, 0]  # Current scroll offset [x, y]
        self.scroll_speed = 10

    def handle_event(self, event):
        """Simple event handling for scrolling with arrow keys."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.offset[0] = max(self.offset[0] - self.scroll_speed, 0)
            elif event.key == pygame.K_RIGHT:
                max_x = max(0, self.content_size[0] - self.rect.width)
                self.offset[0] = min(self.offset[0] + self.scroll_speed, max_x)
            elif event.key == pygame.K_UP:
                self.offset[1] = max(self.offset[1] - self.scroll_speed, 0)
            elif event.key == pygame.K_DOWN:
                max_y = max(0, self.content_size[1] - self.rect.height)
                self.offset[1] = min(self.offset[1] + self.scroll_speed, max_y)

    def draw(self, surface, content_draw_func):
        """
        Draw the scrollable frame.
        - content_draw_func(surface, offset): a callback to draw the inner content.
        """
        # Create a temporary surface for the content.
        content_surf = pygame.Surface(self.content_size)
        content_surf.fill(self.bg_color)
        # Draw the inner content using the provided callback.
        content_draw_func(content_surf, self.offset)
        # Blit the part of the content_surf that should be visible onto the main surface.
        surface.blit(content_surf, self.rect, area=pygame.Rect(self.offset, self.rect.size))
