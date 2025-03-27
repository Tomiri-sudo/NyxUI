import pygame
from widgets.progressbar import ProgressBar
from widgets.seekbar import SeekBar
from widgets.analog_clock import AnalogClock
from widgets.scroll_frame import ScrollFrame
from widgets.textwidget import TextWidget

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Instantiate widgets for testing.
progress_bar = ProgressBar(rect=(50, 50, 200, 30))
seek_bar = SeekBar(rect=(50, 100, 200, 30))
clock_widget = AnalogClock(center=(400, 150), radius=80)  # Increased radius to better show numbers
scroll_frame = ScrollFrame(rect=(300, 300, 400, 200), content_size=(800, 400), orientation="vertical")
text_widget = TextWidget("Hello, NyxUI!", pos=(50, 500), size=32, color=(255, 255, 0), font_weight="Regular")

def draw_scroll_content(surface, offset):
    # Dummy content: draw several colored squares.
    for i in range(10):
        pygame.draw.rect(surface, (100, 100, 250), (50 + i * 70, 50, 60, 60))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        seek_bar.handle_event(event)
        scroll_frame.handle_event(event)

    # Update the progress bar value (cyclic update)
    progress_bar.update((pygame.time.get_ticks() // 50) % 101)

    screen.fill((0, 0, 0))
    progress_bar.draw(screen)
    seek_bar.draw(screen)
    clock_widget.draw(screen)
    scroll_frame.draw(screen, draw_scroll_content)
    text_widget.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
