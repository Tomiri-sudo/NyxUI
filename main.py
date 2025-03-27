import pygame
from widgets.progressbar import ProgressBar
from widgets.seekbar import SeekBar
from widgets.analog_clock import AnalogClock
from widgets.scroll_frame import ScrollFrame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Instantiate widgets
progress_bar = ProgressBar(rect=(50, 50, 200, 30))
seek_bar = SeekBar(rect=(50, 100, 200, 30))
clock_widget = AnalogClock(center=(400, 150), radius=50)
scroll_frame = ScrollFrame(rect=(300, 300, 400, 200), content_size=(800, 400))

def draw_scroll_content(surface, offset):
    # For example: draw multiple rectangles as dummy content
    for i in range(5):
        pygame.draw.rect(surface, (100, 100, 250), (50 + i*150, 50, 100, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        seek_bar.handle_event(event)
        scroll_frame.handle_event(event)

    # Update widget values as needed (for example, simulate progress)
    progress_bar.update((pygame.time.get_ticks() // 50) % 101)

    # Draw background and widgets
    screen.fill((0, 0, 0))
    progress_bar.draw(screen)
    seek_bar.draw(screen)
    clock_widget.draw(screen)
    scroll_frame.draw(screen, draw_scroll_content)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
