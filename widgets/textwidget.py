import pygame
import os

class TextWidget:
    def __init__(self, text, pos, size, color=(255, 255, 255), font_weight="Regular"):
        """
        text: the text string to display
        pos: tuple (x, y)
        size: font size
        color: text color
        font_weight: "Regular", "Bold", etc.
        """
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.font_weight = font_weight
        self.font = self.load_font()

    def load_font(self):
        # Map font weight to a file in the /fonts folder.
        font_files = {
            "Regular": "fonts/Inter-Regular.ttf",
            "Bold": "fonts/Inter-Bold.ttf"
        }
        path = font_files.get(self.font_weight, "fonts/Inter-Regular.ttf")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Font file not found: {path}")
        return pygame.font.Font(path, self.size)

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, self.pos)
