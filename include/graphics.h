#ifndef GRAPHICS_H
#define GRAPHICS_H

void init_graphics(int width, int height);
void set_background_color(int r, int g, int b);
void set_color(int r, int g, int b);
void draw_pixel(int x, int y);
void draw_line(int x1, int y1, int x2, int y2);
void draw_rect(int x, int y, int w, int h);
void present();
void cleanup_graphics();

void draw_text(int x, int y, const char* text);

#endif