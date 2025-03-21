#include "../include/graphics.h"
#include "../include/SDL2/SDL.h"

int main() {
    init_graphics(800, 600);

    // Set white background.
    set_background_color(255, 255, 255);

    // Set drawing color to red for shapes.
    set_color(255, 0, 0);
    draw_line(100, 100, 300, 300);
    draw_rect(400, 200, 100, 50);

    // Set drawing color to blue for text.
    set_color(0, 0, 255);
    draw_text(50, 50, "AB BA");

    present();

    SDL_Event event;
    int running = 1;
    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT)
                running = 0;
        }
        SDL_Delay(16);  // Roughly 60 FPS.
    }

    cleanup_graphics();
    return 0;
}
