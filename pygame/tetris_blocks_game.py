import tkinter as tk
from tkinter import messagebox
import random
import time


class TetrisBlocksGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris Blocks Game")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        # Game variables
        self.board_width = 10
        self.board_height = 20
        self.cell_size = 25
        self.board = [[0 for _ in range(self.board_width)] for _ in range(self.board_height)]
        self.current_piece = None
        self.current_position = [0, self.board_width // 2 - 1]
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.game_running = False
        self.drop_speed = 1000  # milliseconds

        # Tetris pieces (shapes)
        self.pieces = [
            [[1, 1, 1, 1]],  # I-piece
            [[1, 1], [1, 1]],  # O-piece
            [[1, 0, 0], [1, 1, 1]],  # J-piece
            [[0, 0, 1], [1, 1, 1]],  # L-piece
            [[0, 1, 1], [1, 1, 0]],  # S-piece
            [[1, 1, 0], [0, 1, 1]],  # Z-piece
            [[0, 1, 0], [1, 1, 1]]   # T-piece
        ]
        self.piece_colors = ['cyan', 'yellow', 'blue', 'orange', 'green', 'red', 'purple']

        # UI Elements
        self.setup_ui()
        self.create_canvas()
        self.create_controls()
        self.create_score_display()

        # Bind keys
        self.root.bind('<Key>', self.handle_keypress)
        self.root.focus_set()

    def setup_ui(self):
        """Setup the main UI layout"""
        pass

    def create_canvas(self):
        """Create the game canvas"""
        canvas_frame = tk.Frame(self.root)
        canvas_frame.pack(pady=10)

        canvas_width = self.board_width * self.cell_size + 2
        canvas_height = self.board_height * self.cell_size + 2

        self.canvas = tk.Canvas(
            canvas_frame,
            width=canvas_width,
            height=canvas_height,
            bg='white',
            highlightthickness=1
        )
        self.canvas.pack()

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
        display_frame = tk.Frame(self.root)
        display_frame.pack(pady=10)

        # Score
        score_container = tk.Frame(display_frame, relief='solid', bd=1)
        score_container.pack(side=tk.LEFT, padx=10)

        self.score_label = tk.Label(
            score_container,
            text="0",
            font=('Arial', 16, 'bold')
        )
        self.score_label.pack(pady=(0, 5))

        # Lines
        lines_container = tk.Frame(display_frame, relief='solid', bd=1)
        lines_container.pack(side=tk.LEFT, padx=10)

        self.lines_label = tk.Label(
            lines_container,
            text="0",
            font=('Arial', 16, 'bold')
        )
        self.lines_label.pack(pady=(0, 5))

        # Level
        level_container = tk.Frame(display_frame, relief='solid', bd=1)
        level_container.pack(side=tk.LEFT, padx=10)

        self.level_label = tk.Label(
            level_container,
            text="1",
            font=('Arial', 16, 'bold')
        )
        self.level_label.pack(pady=(0, 5))

    def start_game(self):
        """Start the game"""
        if not self.game_running:
            self.game_running = True
            self.start_button.config(state='disabled')
            self.pause_button.config(state='normal')
            self.spawn_piece()
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
        self.board = [[0 for _ in range(self.board_width)] for _ in range(self.board_height)]
        self.current_piece = None
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.drop_speed = 1000

        self.start_button.config(state='normal', text="🎮 Start Game")
        self.pause_button.config(state='disabled', text="⏸️ Pause")

        self.update_display()
        self.draw_board()

    def spawn_piece(self):
        """Spawn a new random piece"""
        piece_index = random.randint(0, len(self.pieces) - 1)
        self.current_piece = {
            'shape': [row[:] for row in self.pieces[piece_index]],  # Deep copy
            'color': self.piece_colors[piece_index],
            'x': self.board_width // 2 - len(self.pieces[piece_index][0]) // 2,
            'y': 0
        }

    def handle_keypress(self, event):
        """Handle keyboard input"""
        if not self.game_running or not self.current_piece:
            return

        key = event.keysym.lower()

        if key == 'left':
            self.move_piece(-1, 0)
        elif key == 'right':
            self.move_piece(1, 0)
        elif key == 'down':
            self.move_piece(0, 1)
        elif key == 'up' or key == 'space':
            self.rotate_piece()
        elif key == 'space':
            self.drop_piece()

    def move_piece(self, dx, dy):
        """Move the current piece"""
        if not self.current_piece:
            return

        new_x = self.current_piece['x'] + dx
        new_y = self.current_piece['y'] + dy

        if self.valid_position(self.current_piece['shape'], new_x, new_y):
            self.current_piece['x'] = new_x
            self.current_piece['y'] = new_y
            self.draw_board()

    def rotate_piece(self):
        """Rotate the current piece"""
        if not self.current_piece:
            return

        # Rotate 90 degrees clockwise
        shape = self.current_piece['shape']
        rotated = list(zip(*shape[::-1]))

        if self.valid_position(rotated, self.current_piece['x'], self.current_piece['y']):
            self.current_piece['shape'] = [list(row) for row in rotated]
            self.draw_board()

    def drop_piece(self):
        """Drop piece to bottom instantly"""
        if not self.current_piece:
            return

        while self.valid_position(self.current_piece['shape'],
                                self.current_piece['x'],
                                self.current_piece['y'] + 1):
            self.current_piece['y'] += 1

        self.place_piece()

    def valid_position(self, shape, x, y):
        """Check if piece position is valid"""
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    board_x = x + col_idx
                    board_y = y + row_idx

                    # Check boundaries
                    if (board_x < 0 or board_x >= self.board_width or
                        board_y >= self.board_height):
                        return False

                    # Check collision with existing pieces (but allow negative y for spawning)
                    if board_y >= 0 and self.board[board_y][board_x]:
                        return False

        return True

    def place_piece(self):
        """Place the current piece on the board"""
        if not self.current_piece:
            return

        shape = self.current_piece['shape']
        color = self.current_piece['color']
        x, y = self.current_piece['x'], self.current_piece['y']

        # Place on board
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    board_y = y + row_idx
                    board_x = x + col_idx
                    if board_y >= 0:
                        self.board[board_y][board_x] = color

        # Check for completed lines
        lines_cleared = self.clear_lines()
        if lines_cleared > 0:
            self.lines_cleared += lines_cleared
            self.score += lines_cleared * 100 * self.level
            self.level = self.lines_cleared // 10 + 1
            self.drop_speed = max(100, 1000 - (self.level - 1) * 100)

        self.update_display()

        # Spawn new piece
        self.spawn_piece()

        # Check game over
        if not self.valid_position(self.current_piece['shape'],
                                self.current_piece['x'],
                                self.current_piece['y']):
            self.game_over()

    def clear_lines(self):
        """Clear completed lines"""
        lines_to_clear = []

        for y in range(self.board_height):
            if all(self.board[y]):
                lines_to_clear.append(y)

        # Remove completed lines
        for y in reversed(lines_to_clear):
            del self.board[y]
            self.board.insert(0, [0] * self.board_width)

        return len(lines_to_clear)

    def game_loop(self):
        """Main game loop"""
        if not self.game_running:
            return

        if self.current_piece:
            # Try to move piece down
            if self.valid_position(self.current_piece['shape'],
                                 self.current_piece['x'],
                                 self.current_piece['y'] + 1):
                self.current_piece['y'] += 1
            else:
                # Piece can't move down, place it
                self.place_piece()

        self.draw_board()

        # Schedule next iteration
        self.root.after(self.drop_speed, self.game_loop)

    def draw_board(self):
        """Draw the game board"""
        self.canvas.delete("all")

        # Draw board cells
        for y in range(self.board_height):
            for x in range(self.board_width):
                color = self.board[y][x]
                if color:
                    self.draw_cell(x, y, color)

        # Draw current piece
        if self.current_piece:
            shape = self.current_piece['shape']
            color = self.current_piece['color']
            piece_x, piece_y = self.current_piece['x'], self.current_piece['y']

            for row_idx, row in enumerate(shape):
                for col_idx, cell in enumerate(row):
                    if cell:
                        board_x = piece_x + col_idx
                        board_y = piece_y + row_idx
                        if 0 <= board_x < self.board_width and 0 <= board_y < self.board_height:
                            self.draw_cell(board_x, board_y, color)

        # Draw grid lines
        for x in range(self.board_width + 1):
            self.canvas.create_line(
                x * self.cell_size, 0,
                x * self.cell_size, self.board_height * self.cell_size,
                fill='black', width=1
            )

        for y in range(self.board_height + 1):
            self.canvas.create_line(
                0, y * self.cell_size,
                self.board_width * self.cell_size, y * self.cell_size,
                fill='black', width=1
            )

    def draw_cell(self, x, y, color):
        """Draw a single cell"""
        x1 = x * self.cell_size
        y1 = y * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size

        # Simple cell without fancy effects
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black', width=1)

    def update_display(self):
        """Update score display"""
        self.score_label.config(text=str(self.score))
        self.lines_label.config(text=str(self.lines_cleared))
        self.level_label.config(text=str(self.level))

    def game_over(self):
        """Handle game over"""
        self.game_running = False
        self.start_button.config(state='normal')
        self.pause_button.config(state='disabled')

        messagebox.showinfo(
            "Game Over",
            f"Game Over!\n\nFinal Score: {self.score}\nLines Cleared: {self.lines_cleared}\nLevel Reached: {self.level}\n\nTry again!"
        )


def main():
    root = tk.Tk()
    game = TetrisBlocksGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()