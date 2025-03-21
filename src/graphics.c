#include "../include/graphics.h"
#include "../include/SDL2/SDL.h"
#include <ctype.h>
#include <string.h>

static SDL_Window* window;
static SDL_Renderer* renderer;

void init_graphics(int width, int height) {
    SDL_Init(SDL_INIT_VIDEO);
    window = SDL_CreateWindow("Graphics Library", SDL_WINDOWPOS_CENTERED, 
                              SDL_WINDOWPOS_CENTERED, width, height, 0);
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
}

void set_color(int r, int g, int b) {
    SDL_SetRenderDrawColor(renderer, r, g, b, 255);
}

void draw_pixel(int x, int y) {
    SDL_RenderDrawPoint(renderer, x, y);
}

void draw_line(int x1, int y1, int x2, int y2) {
    SDL_RenderDrawLine(renderer, x1, y1, x2, y2);
}

void draw_rect(int x, int y, int w, int h) {
    SDL_Rect rect = { x, y, w, h };
    SDL_RenderDrawRect(renderer, &rect);
}

void present() {
    SDL_RenderPresent(renderer);
}

void cleanup_graphics() {
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}
