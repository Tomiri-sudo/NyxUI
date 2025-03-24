import pygame

class TextLabel:
    def __init__(self, text, position=(0, 0), size=30, font=None,
                 color=(255, 255, 255), bold=False, skew=0, italic=False,
                 width=None, height=None):
        self.text = text
        self.position = position
        self.size = size
        # For now, font is expected to be a path to a TTF file.
        # You can later override this with your custom vector-based font implementation.
        self.font = font or pygame.font.get_default_font()  
        self.color = color
        self.bold = bold
        self.skew = skew  # skew in degrees; you might replace this with a custom transform.
        self.italic = italic
        self.width = width
        self.height = height
        self._calculate_dimensions()

    def _calculate_dimensions(self):
        # Calculate width/height using pygame's font metrics if not explicitly provided.
        pygame_font = pygame.font.Font(self.font, self.size)
        pygame_font.set_bold(self.bold)
        pygame_font.set_italic(self.italic)
        text_surface = pygame_font.render(self.text, True, self.color)
        if self.width is None:
            self.width = text_surface.get_width()
        if self.height is None:
            self.height = text_surface.get_height()

    def render(self, surface):
        pygame_font = pygame.font.Font(self.font, self.size)
        pygame_font.set_bold(self.bold)
        pygame_font.set_italic(self.italic)
        text_surface = pygame_font.render(self.text, True, self.color)
        
        # Apply skew transformation if needed.
        if self.skew:
            # Pygame doesn’t have a direct shear transformation;
            # as a simple substitute, rotate the text by the skew value.
            text_surface = pygame.transform.rotate(text_surface, self.skew)
        
        # If explicit width/height are provided, scale the text surface.
        if self.width and self.height:
            text_surface = pygame.transform.smoothscale(text_surface, (self.width, self.height))
            
        surface.blit(text_surface, self.position)
