import tkinter as tk
from tkinter import messagebox
import random
import time


class MemoryCardsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Cards Game")
        self.root.geometry("700x750")
        self.root.resizable(False, False)

        # Game variables
        self.grid_size = 4  # 4x4 grid
        self.cards = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.moves = 0
        self.game_started = False
        self.card_symbols = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐸', '🐵', '🐔', '🐧', '🐦']
        self.card_back = '❓'

        # UI Elements
        self.setup_ui()
        self.create_card_grid()
        self.create_controls()
        self.create_score_display()

    def setup_ui(self):
        """Setup the main UI layout"""
        pass

    def create_card_grid(self):
        """Create the card grid"""
        grid_frame = tk.Frame(self.root)
        grid_frame.pack(pady=20)

        self.card_buttons = []
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                button = tk.Button(
                    grid_frame,
                    text=self.card_back,
                    font=('Arial', 18),
                    width=4,
                    height=2,
                    relief='raised',
                    bd=2,
                    command=lambda r=row, c=col: self.flip_card(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.card_buttons.append(button)

    def create_controls(self):
        """Create game control buttons"""
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        self.start_button = tk.Button(
            control_frame,
            text="New Game",
            command=self.start_game,
            font=('Arial', 10)
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

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

        # Moves counter
        moves_container = tk.Frame(display_frame, relief='solid', bd=1)
        moves_container.pack(side=tk.LEFT, padx=10)

        self.moves_label = tk.Label(
            moves_container,
            text="0",
            font=('Arial', 18, 'bold')
        )
        self.moves_label.pack(pady=(0, 8))

        # Pairs counter
        pairs_container = tk.Frame(display_frame, relief='solid', bd=1)
        pairs_container.pack(side=tk.LEFT, padx=10)

        self.pairs_label = tk.Label(
            pairs_container,
            text="0/8",
            font=('Arial', 18, 'bold')
        )
        self.pairs_label.pack(pady=(0, 8))

    def start_game(self):
        """Start a new game"""
        self.reset_game()
        self.game_started = True
        self.shuffle_cards()

    def reset_game(self):
        """Reset the game"""
        self.game_started = False
        self.flipped_cards = []
        self.matched_pairs = 0
        self.moves = 0

        self.update_display()

        # Reset all cards
        for button in self.card_buttons:
            button.config(
                text=self.card_back,
                state='normal'
            )

    def shuffle_cards(self):
        """Shuffle and assign symbols to cards"""
        # Get pairs of symbols
        symbols = self.card_symbols[:8] * 2  # 8 pairs
        random.shuffle(symbols)

        self.cards = symbols

    def flip_card(self, row, col):
        """Handle card flipping"""
        if not self.game_started:
            return

        index = row * self.grid_size + col
        button = self.card_buttons[index]

        # Don't flip if already flipped or matched
        if button.cget('text') != self.card_back or len(self.flipped_cards) >= 2:
            return

        # Flip the card
        symbol = self.cards[index]
        button.config(text=symbol)
        self.flipped_cards.append((index, button))

        # Check for match when 2 cards are flipped
        if len(self.flipped_cards) == 2:
            self.moves += 1
            self.update_display()
            self.root.after(1000, self.check_match)

    def check_match(self):
        """Check if flipped cards match"""
        if len(self.flipped_cards) != 2:
            return

        card1_idx, card1_button = self.flipped_cards[0]
        card2_idx, card2_button = self.flipped_cards[1]

        symbol1 = self.cards[card1_idx]
        symbol2 = self.cards[card2_idx]

        if symbol1 == symbol2:
            # Match found!
            self.matched_pairs += 1
            card1_button.config(state='disabled')
            card2_button.config(state='disabled')

            # Celebration effect
            self.celebrate_match(card1_button, card2_button)

            if self.matched_pairs == 8:  # All pairs found
                self.game_won()
        else:
            # No match, flip back
            card1_button.config(text=self.card_back)
            card2_button.config(text=self.card_back)

        self.flipped_cards = []

    def celebrate_match(self, button1, button2):
        """Celebration animation for matched pair"""
        def flash():
            for _ in range(3):
                button1.config(text="✓")
                button2.config(text="✓")
                self.root.update()
                time.sleep(0.1)
                button1.config(text="")
                button2.config(text="")
                self.root.update()
                time.sleep(0.1)

        import threading
        threading.Thread(target=flash, daemon=True).start()

    def game_won(self):
        """Handle game completion"""
        self.game_started = False

        # Calculate score based on moves
        if self.moves <= 16:
            rating = "🏆 Perfect!"
        elif self.moves <= 24:
            rating = "⭐ Excellent!"
        elif self.moves <= 32:
            rating = "👍 Good!"
        else:
            rating = "🎯 Well Done!"

        messagebox.showinfo(
            "Congratulations!",
            f"🎉 You Won!\n\nMoves: {self.moves}\nRating: {rating}\n\nTry again for a better score!"
        )

    def update_display(self):
        """Update score display"""
        self.moves_label.config(text=str(self.moves))
        self.pairs_label.config(text=f"{self.matched_pairs}/8")


def main():
    root = tk.Tk()
    game = MemoryCardsGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()