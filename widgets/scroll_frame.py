import pygame

class ScrollFrame:
    def __init__(self, rect, content_size, orientation="vertical", bg_color=(30, 30, 30)):
        self.rect = pygame.Rect(rect)
        self.content_size = content_size  # (width, height) of inner content
        self.bg_color = bg_color
        self.orientation = orientation  # "vertical" or "horizontal"
        self.offset = [0, 0]
        self.scroll_speed = 20

        # Settings for scrollbar track and thumb
        self.track_thickness = 15
        self.thumb_margin = 2
        self.dragging_thumb = False
        self.thumb_rect = self.calculate_thumb_rect()

    def calculate_thumb_rect(self):
        if self.orientation == "vertical":
            visible_ratio = self.rect.height / self.content_size[1] if self.content_size[1] > self.rect.height else 1
            thumb_height = max(20, self.rect.height * visible_ratio)
            max_offset = max(1, self.content_size[1] - self.rect.height)
            thumb_y = self.rect.y + (self.offset[1] / max_offset) * (self.rect.height - thumb_height)
            thumb_x = self.rect.right - self.track_thickness + self.thumb_margin
            return pygame.Rect(thumb_x, int(thumb_y), self.track_thickness - 2 * self.thumb_margin, int(thumb_height))
        else:
            visible_ratio = self.rect.width / self.content_size[0] if self.content_size[0] > self.rect.width else 1
            thumb_width = max(20, self.rect.width * visible_ratio)
            max_offset = max(1, self.content_size[0] - self.rect.width)
            thumb_x = self.rect.x + (self.offset[0] / max_offset) * (self.rect.width - thumb_width)
            thumb_y = self.rect.bottom - self.track_thickness + self.thumb_margin
            return pygame.Rect(int(thumb_x), thumb_y, int(thumb_width), self.track_thickness - 2 * self.thumb_margin)

    def handle_event(self, event):
        # Handle mouse wheel scrolling
        if event.type == pygame.MOUSEWHEEL:
            if self.orientation == "vertical":
                self.offset[1] = min(max(self.offset[1] - event.y * self.scroll_speed, 0),
                                     max(0, self.content_size[1] - self.rect.height))
            else:
                self.offset[0] = min(max(self.offset[0] - event.y * self.scroll_speed, 0),
                                     max(0, self.content_size[0] - self.rect.width))
            self.thumb_rect = self.calculate_thumb_rect()

        # Handle thumb dragging with mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.thumb_rect.collidepoint(event.pos):
                self.dragging_thumb = True
                self.drag_offset = (event.pos[0] - self.thumb_rect.x, event.pos[1] - self.thumb_rect.y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging_thumb = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_thumb:
                if self.orientation == "vertical":
                    new_y = event.pos[1] - self.drag_offset[1]
                    new_y = min(max(new_y, self.rect.y), self.rect.bottom - self.thumb_rect.height)
                    ratio = (new_y - self.rect.y) / (self.rect.height - self.thumb_rect.height)
                    self.offset[1] = ratio * (self.content_size[1] - self.rect.height)
                else:
                    new_x = event.pos[0] - self.drag_offset[0]
                    new_x = min(max(new_x, self.rect.x), self.rect.right - self.thumb_rect.width)
                    ratio = (new_x - self.rect.x) / (self.rect.width - self.thumb_rect.width)
                    self.offset[0] = ratio * (self.content_size[0] - self.rect.width)
                self.thumb_rect = self.calculate_thumb_rect()

    def draw(self, surface, content_draw_func):
        # Create a temporary surface for the inner content.
        content_surf = pygame.Surface(self.content_size)
        content_surf.fill(self.bg_color)
        # Draw inner content via the callback
        content_draw_func(content_surf, self.offset)
        # Blit the visible portion to the main surface.
        surface.blit(content_surf, self.rect, area=pygame.Rect(self.offset, self.rect.size))

        # Draw scrollbar track and thumb.
        if self.orientation == "vertical":
            track_rect = pygame.Rect(self.rect.right - self.track_thickness, self.rect.y,
                                     self.track_thickness, self.rect.height)
        else:
            track_rect = pygame.Rect(self.rect.x, self.rect.bottom - self.track_thickness,
                                     self.rect.width, self.track_thickness)
        pygame.draw.rect(surface, (60, 60, 60), track_rect)
        pygame.draw.rect(surface, (100, 100, 100), self.thumb_rect)
