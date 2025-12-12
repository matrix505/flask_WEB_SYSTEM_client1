import tkinter as tk
from tkinter import messagebox
import random


class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Game variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        """Setup the main UI layout"""
        # Title
        title_label = tk.Label(self.root, text="Guess the Number!", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Instructions
        instructions = tk.Label(self.root, text="I'm thinking of a number between 1 and 100.\nYou have 10 attempts to guess it!", font=("Arial", 10))
        instructions.pack(pady=5)

        # Attempts counter
        self.attempts_label = tk.Label(self.root, text=f"Attempts: {self.attempts}/{self.max_attempts}", font=("Arial", 10))
        self.attempts_label.pack(pady=5)

        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        guess_label = tk.Label(input_frame, text="Enter your guess:", font=("Arial", 10))
        guess_label.pack(side=tk.LEFT, padx=5)

        self.guess_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.focus()

        # Guess button
        guess_button = tk.Button(self.root, text="Guess!", command=self.make_guess, font=("Arial", 12), bg="#4CAF50", fg="white")
        guess_button.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 10), fg="blue")
        self.feedback_label.pack(pady=5)

        # New game button
        new_game_button = tk.Button(self.root, text="New Game", command=self.new_game, font=("Arial", 10))
        new_game_button.pack(pady=5)

        # Bind Enter key to guess
        self.root.bind('<Return>', lambda event: self.make_guess())

    def make_guess(self):
        """Process the user's guess"""
        try:
            guess = int(self.guess_entry.get())
            self.guess_entry.delete(0, tk.END)

            if guess < 1 or guess > 100:
                self.feedback_label.config(text="Please enter a number between 1 and 100!", fg="red")
                return

            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!\nThe number was {self.secret_number}")
                self.new_game()
            elif guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try a higher number.", fg="orange")
            else:
                self.feedback_label.config(text="Too high! Try a lower number.", fg="orange")

            if self.attempts >= self.max_attempts and guess != self.secret_number:
                messagebox.showinfo("Game Over", f"Sorry, you've used all {self.max_attempts} attempts.\nThe number was {self.secret_number}")
                self.new_game()

        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="red")

    def new_game(self):
        """Start a new game"""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.feedback_label.config(text="", fg="blue")
        self.guess_entry.focus()


def main():
    root = tk.Tk()
    game = GuessGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()