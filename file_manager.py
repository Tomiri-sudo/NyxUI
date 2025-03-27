import os
import pygame

# Constants for colors and sizes
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (70, 70, 70)
SCREEN_SIZE = (800, 600)
FONT_SIZE = 24

class FileManager:
    def __init__(self, start_path):
        self.current_path = os.path.abspath(start_path)
        self.items = []  # List of (name, full_path, is_dir)
        self.selected_index = 0
        self.font = pygame.font.Font(os.path.join("fonts", "Inter-Regular.ttf"), FONT_SIZE)
        self.prompt_active = False
        self.prompt_message = ""
        self.prompt_callback = None
        self.update_items()

    def update_items(self):
        """Load files and directories in the current directory."""
        self.items = []
        # Add an item to go to the parent directory.
        parent_path = os.path.dirname(self.current_path)
        if parent_path != self.current_path:  # Prevent infinite loop at root.
            self.items.append(("..", parent_path, True))
        for entry in os.listdir(self.current_path):
            full_path = os.path.join(self.current_path, entry)
            is_dir = os.path.isdir(full_path)
            self.items.append((entry, full_path, is_dir))
        self.selected_index = 0

    def draw(self, surface):
        surface.fill(BG_COLOR)
        # Draw current path at the top.
        path_text = self.font.render(f"Path: {self.current_path}", True, TEXT_COLOR)
        surface.blit(path_text, (20, 10))
        # List the items
        start_y = 50
        for i, (name, full_path, is_dir) in enumerate(self.items):
            y = start_y + i * (FONT_SIZE + 10)
            bg_rect = pygame.Rect(10, y, SCREEN_SIZE[0]-20, FONT_SIZE+5)
            if i == self.selected_index:
                pygame.draw.rect(surface, HIGHLIGHT_COLOR, bg_rect)
            text = f"[DIR] {name}" if is_dir else name
            item_text = self.font.render(text, True, TEXT_COLOR)
            surface.blit(item_text, (20, y))
        # If a prompt is active, draw it on top
        if self.prompt_active:
            self.draw_prompt(surface)

    def draw_prompt(self, surface):
        prompt_rect = pygame.Rect(100, 200, 600, 150)
        pygame.draw.rect(surface, (50, 50, 50), prompt_rect)
        pygame.draw.rect(surface, (200, 200, 200), prompt_rect, 2)
        prompt_text = self.font.render(self.prompt_message, True, TEXT_COLOR)
        prompt_rect_text = prompt_text.get_rect(center=prompt_rect.center)
        surface.blit(prompt_text, prompt_rect_text)
        # Draw Yes/No buttons
        yes_text = self.font.render("Yes", True, TEXT_COLOR)
        no_text = self.font.render("No", True, TEXT_COLOR)
        yes_rect = yes_text.get_rect(center=(prompt_rect.centerx - 100, prompt_rect.bottom - 40))
        no_rect = no_text.get_rect(center=(prompt_rect.centerx + 100, prompt_rect.bottom - 40))
        pygame.draw.rect(surface, HIGHLIGHT_COLOR, yes_rect.inflate(20,10))
        pygame.draw.rect(surface, HIGHLIGHT_COLOR, no_rect.inflate(20,10))
        surface.blit(yes_text, yes_rect)
        surface.blit(no_text, no_rect)
        self.yes_rect = yes_rect.inflate(20,10)
        self.no_rect = no_rect.inflate(20,10)

    def handle_event(self, event):
        if self.prompt_active:
            self.handle_prompt_event(event)
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected_index = min(self.selected_index + 1, len(self.items)-1)
            elif event.key == pygame.K_UP:
                self.selected_index = max(self.selected_index - 1, 0)
            elif event.key == pygame.K_RETURN:
                self.activate_selected_item()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check if an item was clicked
                mouse_y = event.pos[1]
                index = (mouse_y - 50) // (FONT_SIZE + 10)
                if 0 <= index < len(self.items):
                    self.selected_index = index
                    self.activate_selected_item()

    def handle_prompt_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.yes_rect.collidepoint(event.pos):
                # Call the callback with True, then clear prompt.
                if self.prompt_callback:
                    self.prompt_callback(True)
                self.prompt_active = False
            elif self.no_rect.collidepoint(event.pos):
                # Call the callback with False.
                if self.prompt_callback:
                    self.prompt_callback(False)
                self.prompt_active = False

    def activate_selected_item(self):
        name, full_path, is_dir = self.items[self.selected_index]
        if is_dir:
            self.current_path = os.path.abspath(full_path)
            self.update_items()
        else:
            # If it's a file, open it. If it's a .nap file, prompt to install.
            if full_path.lower().endswith(".nap"):
                self.prompt_install(full_path)
            else:
                # For non-.nap files, simply print that we're opening the file.
                print(f"Opening file: {full_path}")

    def prompt_install(self, file_path):
        self.prompt_active = True
        self.prompt_message = f"Install app from '{os.path.basename(file_path)}'?"
        # Set a callback that will process the user's response.
        self.prompt_callback = lambda choice: self.install_app(file_path) if choice else print("Installation cancelled.")

    def install_app(self, file_path):
        # Here you would add the logic to install the app.
        print(f"Installing app from {file_path}...")
        # For example, you could extract the .nap file, read the manifest, etc.
        # This is just a placeholder.
        # After installation, you might want to remove or mark the file.
        # (This part will be expanded in the app management system.)
        

# Test program for the file manager.
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    file_manager = FileManager(start_path=".")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            file_manager.handle_event(event)

        file_manager.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
