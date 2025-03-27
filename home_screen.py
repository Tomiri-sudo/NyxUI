import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load system font from /fonts (Inter-Regular.ttf) for home screen text.
font_path = os.path.join("fonts", "Inter-Regular.ttf")
system_font = pygame.font.Font(font_path, 24)

# Dummy list of apps for the grid.
apps = [
    {"name": "Calculator", "color": (255, 100, 100)},
    {"name": "Calendar", "color": (100, 255, 100)},
    {"name": "Music", "color": (100, 100, 255)},
    {"name": "Photos", "color": (255, 255, 100)},
    {"name": "Settings", "color": (255, 100, 255)},
    {"name": "Browser", "color": (100, 255, 255)},
]

# Layout parameters for the app icon grid.
icon_size = 80
padding = 20
cols = 3
rows = (len(apps) + cols - 1) // cols

def draw_home_screen(surface):
    surface.fill((20, 20, 20))  # Background color
    # Draw title.
    title = system_font.render("Home Screen", True, (255, 255, 255))
    title_rect = title.get_rect(center=(400, 40))
    surface.blit(title, title_rect)
    
    # Center the grid.
    start_x = (800 - (cols * icon_size + (cols - 1) * padding)) // 2
    start_y = 80
    for index, app in enumerate(apps):
        row = index // cols
        col = index % cols
        x = start_x + col * (icon_size + padding)
        y = start_y + row * (icon_size + padding)
        # Draw the app icon (as a filled rectangle).
        icon_rect = pygame.Rect(x, y, icon_size, icon_size)
        pygame.draw.rect(surface, app["color"], icon_rect)
        # Draw the app name below the icon.
        name_text = system_font.render(app["name"], True, (255, 255, 255))
        name_rect = name_text.get_rect(center=(x + icon_size // 2, y + icon_size + 15))
        surface.blit(name_text, name_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_home_screen(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

