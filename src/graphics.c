#include "../include/graphics.h"
#include "../include/SDL2/SDL.h"
#include "../include/ctype.h"
#include <string.h>

// Global SDL variables.
static SDL_Window* window;
static SDL_Renderer* renderer;

// Basic dictionary for vector-style letters.
typedef struct {
    char letter;
    int num_segments;
    int segments[10][4];  // Each segment: x1, y1, x2, y2.
} Letter;

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

// Only a couple of letters for demonstration purposes.
static Letter letters[] = {
    // Letter A: two diagonal lines and a crossbar.
    { 'A', 3, { {0,20, 10,0}, {10,0, 20,20}, {5,10, 15,10} } },
    // Letter B: a vertical line and three horizontal segments.
    { 'B', 4, { {0,0, 0,20}, {0,0, 10,0}, {0,10, 10,10}, {0,20, 10,20} } }
};

void init_graphics(int width, int height) {
    SDL_Init(SDL_INIT_VIDEO);
    window = SDL_CreateWindow("Graphics Library", 
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, 0);
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
}

void set_background_color(int r, int g, int b) {
    // Set draw color and clear the renderer.
    SDL_SetRenderDrawColor(renderer, r, g, b, 255);
    SDL_RenderClear(renderer);
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

// New: Basic text rendering function.
void draw_text(int x, int y, const char* text) {
    const int letter_width = 22;  // Fixed width for each letter (including spacing)
    
    // Loop through each character in the string.
    for (int i = 0; text[i] != '\0'; i++) {
        char ch = toupper(text[i]);
        
        // Handle space.
        if (ch == ' ') {
            x += letter_width;
            continue;
        }
        
        // Search for the letter in our dictionary.
        int found = 0;
        int numLetters = sizeof(letters) / sizeof(Letter);
        for (int j = 0; j < numLetters; j++) {
            if (letters[j].letter == ch) {
                // Draw each segment for the letter.
                for (int k = 0; k < letters[j].num_segments; k++) {
                    int x1 = x + letters[j].segments[k][0];
                    int y1 = y + letters[j].segments[k][1];
                    int x2 = x + letters[j].segments[k][2];
                    int y2 = y + letters[j].segments[k][3];
                    draw_line(x1, y1, x2, y2);
                }
                found = 1;
                break;
            }
        }
        // If the letter is not found in the dictionary, you could skip or add a placeholder.
        if (!found) {
            // For now, we'll simply leave a blank space.
        }
        // Move the x coordinate for the next letter.
        x += letter_width;
    }
}
