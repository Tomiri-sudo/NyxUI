import pygame

class ScrollFrame:
    def __init__(self, rect, content_size, orientation="vertical", bg_color=(30, 30, 30)):
        self.rect = pygame.Rect(rect)
        self.content_size = content_size  # (width, height) of inner content
        self.bg_color = bg_color
        self.orientation = orientation  # "vertical" or "horizontal"
        self.offset = [0, 0]
        self.scroll_speed = 20

        # For click-and-drag of the scrollbar thumb
        self.dragging_thumb = False
        self.thumb_rect = self.calculate_thumb_rect()

    def calculate_thumb_rect(self):
        if self.orientation == "vertical":
            visible_ratio = self.rect.height / self.content_size[1]
            thumb_height = max(20, self.rect.height * visible_ratio)
            max_offset = self.content_size[1] - self.rect.height
            if max_offset:
                thumb_y = self.rect.y + (self.offset[1] / max_offset) * (self.rect.height - thumb_height)
            else:
                thumb_y = self.rect.y
            return pygame.Rect(self.rect.right - 15, int(thumb_y), 10, int(thumb_height))
        else:
            visible_ratio = self.rect.width / self.content_size[0]
            thumb_width = max(20, self.rect.width * visible_ratio)
            max_offset = self.content_size[0] - self.rect.width
            if max_offset:
                thumb_x = self.rect.x + (self.offset[0] / max_offset) * (self.rect.width - thumb_width)
            else:
                thumb_x = self.rect.x
            return pygame.Rect(int(thumb_x), self.rect.bottom - 15, int(thumb_width), 10)

    def handle_event(self, event):
        # Mouse wheel scrolling
        if event.type == pygame.MOUSEWHEEL:
            if self.orientation == "vertical":
                self.offset[1] = min(max(self.offset[1] - event.y * self.scroll_speed, 0), max(0, self.content_size[1] - self.rect.height))
            else:
                self.offset[0] = min(max(self.offset[0] - event.y * self.scroll_speed, 0), max(0, self.content_size[0] - self.rect.width))
            self.thumb_rect = self.calculate_thumb_rect()

        # Click and drag the scrollbar thumb
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
                    # Map thumb position back to content offset
                    ratio = (new_y - self.rect.y) / (self.rect.height - self.thumb_rect.height)
                    self.offset[1] = ratio * (self.content_size[1] - self.rect.height)
                else:
                    new_x = event.pos[0] - self.drag_offset[0]
                    new_x = min(max(new_x, self.rect.x), self.rect.right - self.thumb_rect.width)
                    ratio = (new_x - self.rect.x) / (self.rect.width - self.thumb_rect.width)
                    self.offset[0] = ratio * (self.content_size[0] - self.rect.width)
                self.thumb_rect = self.calculate_thumb_rect()

    def draw(self, surface, content_draw_func):
        # Draw the background for the content area
        content_surf = pygame.Surface(self.content_size)
        content_surf.fill(self.bg_color)
        # Draw the inner content using the callback
        content_draw_func(content_surf, self.offset)
        # Blit the visible part
        surface.blit(content_surf, self.rect, area=pygame.Rect(self.offset, self.rect.size))

        # Draw the scrollbar track and thumb
        if self.orientation == "vertical":
            track_rect = pygame.Rect(self.rect.right - 15, self.rect.y, 15, self.rect.height)
        else:
            track_rect = pygame.Rect(self.rect.x, self.rect.bottom - 15, self.rect.width, 15)
        pygame.draw.rect(surface, (60, 60, 60), track_rect)
        pygame.draw.rect(surface, (100, 100, 100), self.thumb_rect)
