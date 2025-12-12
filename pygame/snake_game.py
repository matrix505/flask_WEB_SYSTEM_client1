import tkinter as tk
from tkinter import messagebox
import random
import time


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("600x650")
        self.root.resizable(False, False)

        # Game variables
        self.canvas_width = 400
        self.canvas_height = 400
        self.cell_size = 20
        self.snake = [(10, 10)]  # Starting position
        self.direction = (0, 1)  # Moving right initially
        self.food = None
        self.score = 0
        self.game_running = False
        self.speed = 150  # milliseconds

        # UI Elements
        self.setup_ui()
        self.create_canvas()
        self.create_controls()
        self.create_score_display()

        # Bind keys
        self.root.bind('<Key>', self.change_direction)
        self.root.focus_set()

    def setup_ui(self):
        """Setup the main UI layout"""
        pass

    def create_canvas(self):
        """Create the game canvas"""
        canvas_frame = tk.Frame(self.root)
        canvas_frame.pack(pady=10)

        self.canvas = tk.Canvas(
            canvas_frame,
            width=self.canvas_width,
            height=self.canvas_height,
            bg='white',
            highlightthickness=1
        )
        self.canvas.pack()

        # Draw grid lines
        for i in range(0, self.canvas_width, self.cell_size):
            self.canvas.create_line(i, 0, i, self.canvas_height, fill='lightgray', width=1)
        for i in range(0, self.canvas_height, self.cell_size):
            self.canvas.create_line(0, i, self.canvas_width, i, fill='lightgray', width=1)

    def create_controls(self):
        """Create game control buttons"""
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        self.start_button = tk.Button(
            control_frame,
            text="Start Game",
            command=self.start_game,
            font=('Arial', 10)
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(
            control_frame,
            text="Pause",
            command=self.pause_game,
            font=('Arial', 10),
            state='disabled'
        )
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            control_frame,
            text="Reset",
            command=self.reset_game,
            font=('Arial', 10)
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def create_score_display(self):
        """Create score display"""
        score_frame = tk.Frame(self.root)
        score_frame.pack(pady=10)

        score_container = tk.Frame(score_frame, relief='solid', bd=1)
        score_container.pack()

        self.score_label = tk.Label(
            score_container,
            text="0",
            font=('Arial', 18, 'bold')
        )
        self.score_label.pack(pady=(0, 8))

    def start_game(self):
        """Start the game"""
        if not self.game_running:
            self.game_running = True
            self.start_button.config(state='disabled')
            self.pause_button.config(state='normal')
            self.spawn_food()
            self.game_loop()

    def pause_game(self):
        """Pause/unpause the game"""
        if self.game_running:
            self.game_running = False
            self.pause_button.config(text="▶️ Resume")
        else:
            self.game_running = True
            self.pause_button.config(text="⏸️ Pause")
            self.game_loop()

    def reset_game(self):
        """Reset the game"""
        self.game_running = False
        self.snake = [(10, 10)]
        self.direction = (0, 1)
        self.food = None
        self.score = 0
        self.speed = 150

        self.start_button.config(state='normal', text="🎮 Start Game")
        self.pause_button.config(state='disabled', text="⏸️ Pause")

        self.update_score()
        self.draw_game()

    def spawn_food(self):
        """Spawn food at random location"""
        while True:
            x = random.randint(0, (self.canvas_width // self.cell_size) - 1)
            y = random.randint(0, (self.canvas_height // self.cell_size) - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, event):
        """Change snake direction based on key press"""
        if not self.game_running:
            return

        key = event.keysym.lower()
        if key == 'left' or key == 'a':
            if self.direction != (1, 0):  # Not going right
                self.direction = (-1, 0)
        elif key == 'right' or key == 'd':
            if self.direction != (-1, 0):  # Not going left
                self.direction = (1, 0)
        elif key == 'up' or key == 'w':
            if self.direction != (0, 1):  # Not going down
                self.direction = (0, -1)
        elif key == 'down' or key == 's':
            if self.direction != (0, -1):  # Not going up
                self.direction = (0, 1)

    def game_loop(self):
        """Main game loop"""
        if not self.game_running:
            return

        # Move snake
        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= self.canvas_width // self.cell_size or
            new_head[1] < 0 or new_head[1] >= self.canvas_height // self.cell_size):
            self.game_over()
            return

        # Check self collision
        if new_head in self.snake:
            self.game_over()
            return

        # Add new head
        self.snake.insert(0, new_head)

        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.update_score()
            self.spawn_food()
            # Speed up as snake grows
            if self.speed > 80:
                self.speed -= 2
        else:
            # Remove tail if no food eaten
            self.snake.pop()

        self.draw_game()

        # Schedule next move
        self.root.after(self.speed, self.game_loop)

    def draw_game(self):
        """Draw the game state"""
        self.canvas.delete("all")

        # Draw grid
        for i in range(0, self.canvas_width, self.cell_size):
            self.canvas.create_line(i, 0, i, self.canvas_height, fill='lightgray', width=1)
        for i in range(0, self.canvas_height, self.cell_size):
            self.canvas.create_line(0, i, self.canvas_width, i, fill='lightgray', width=1)

        # Draw snake
        for i, segment in enumerate(self.snake):
            x, y = segment
            color = 'green' if i == 0 else 'darkgreen'  # Head is brighter
            self.canvas.create_rectangle(
                x * self.cell_size, y * self.cell_size,
                (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                fill=color, outline='black', width=1
            )

        # Draw food
        if self.food:
            x, y = self.food
            self.canvas.create_oval(
                x * self.cell_size + 2, y * self.cell_size + 2,
                (x + 1) * self.cell_size - 2, (y + 1) * self.cell_size - 2,
                fill='red', outline='black', width=1
            )

    def update_score(self):
        """Update score display"""
        self.score_label.config(text=str(self.score))

    def game_over(self):
        """Handle game over"""
        self.game_running = False
        self.start_button.config(state='normal')
        self.pause_button.config(state='disabled')

        messagebox.showinfo(
            "Game Over",
            f"Game Over!\n\nFinal Score: {self.score}\nSnake Length: {len(self.snake)}\n\nTry again!"
        )


def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()