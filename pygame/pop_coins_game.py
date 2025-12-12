import tkinter as tk
from tkinter import messagebox
import random
import time
import threading


class PopCoinsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pop Coins Game")
        self.root.geometry("700x750")
        self.root.resizable(False, False)

        # Game variables
        self.canvas_width = 500
        self.canvas_height = 500
        self.coins = []
        self.score = 0
        self.time_left = 60  # 60 seconds
        self.game_running = False
        self.coin_spawn_rate = 2000  # milliseconds
        self.coin_speed = 2
        self.max_coins = 8

        # UI Elements
        self.setup_ui()
        self.create_canvas()
        self.create_controls()
        self.create_score_display()
        self.create_timer_display()

        # Bind mouse click
        self.canvas.bind('<Button-1>', self.pop_coin)

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

        score_container = tk.Frame(display_frame, relief='solid', bd=1)
        score_container.pack(side=tk.LEFT, padx=10)

        self.score_label = tk.Label(
            score_container,
            text="0",
            font=('Arial', 18, 'bold')
        )
        self.score_label.pack(pady=(0, 8))

    def create_timer_display(self):
        """Create timer display"""
        timer_container = tk.Frame(self.root, relief='solid', bd=1)
        timer_container.pack(pady=10)

        self.timer_label = tk.Label(
            timer_container,
            text="60",
            font=('Arial', 18, 'bold')
        )
        self.timer_label.pack(pady=(0, 8))

    def start_game(self):
        """Start the game"""
        if self.game_running:
            return

        self.game_running = True
        self.time_left = 60
        self.score = 0
        self.coins = []

        self.start_button.config(state='disabled')
        self.update_score()
        self.update_timer()

        # Start timer thread
        threading.Thread(target=self.timer_thread, daemon=True).start()

        # Start coin spawning
        self.spawn_coins()

    def reset_game(self):
        """Reset the game"""
        self.game_running = False
        self.coins = []
        self.score = 0
        self.time_left = 60

        self.start_button.config(state='normal')
        self.update_score()
        self.update_timer()
        self.canvas.delete("all")

    def timer_thread(self):
        """Timer countdown thread"""
        while self.game_running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.root.after(0, self.update_timer)

            if self.time_left <= 10:  # Last 10 seconds warning
                self.root.after(0, lambda: self.timer_label.config(fg='red'))

        if self.game_running:
            self.game_over()

    def update_timer(self):
        """Update timer display"""
        self.timer_label.config(text=str(self.time_left))

    def update_score(self):
        """Update score display"""
        self.score_label.config(text=str(self.score))

    def spawn_coins(self):
        """Spawn coins periodically"""
        if not self.game_running:
            return

        # Remove coins that are off screen
        self.coins = [coin for coin in self.coins if coin['y'] < self.canvas_height + 50]

        # Spawn new coin if under limit
        if len(self.coins) < self.max_coins and random.random() < 0.7:
            coin_type = random.choice(['gold', 'silver', 'bronze'])
            x = random.randint(50, self.canvas_width - 50)
            y = -50

            coin = {
                'id': None,
                'x': x,
                'y': y,
                'type': coin_type,
                'speed': random.uniform(1.5, 3.0)
            }
            self.coins.append(coin)

        # Move coins
        self.move_coins()

        # Schedule next spawn
        if self.game_running:
            self.root.after(self.coin_spawn_rate, self.spawn_coins)

    def move_coins(self):
        """Move all coins down"""
        for coin in self.coins[:]:  # Copy list to avoid modification issues
            coin['y'] += coin['speed']

            # Remove coin if it goes off screen
            if coin['y'] > self.canvas_height + 50:
                self.coins.remove(coin)
                continue

            # Draw coin
            self.draw_coin(coin)

    def draw_coin(self, coin):
        """Draw a coin on canvas"""
        # Remove old coin
        if coin['id']:
            self.canvas.delete(coin['id'])

        # Coin colors and values
        colors = {
            'gold': ('yellow', 'orange', 50),
            'silver': ('gray', 'lightgray', 30),
            'bronze': ('brown', 'sienna', 10)
        }

        color1, color2, value = colors[coin['type']]

        # Draw coin as circle with gradient effect
        x, y = coin['x'], coin['y']
        size = 25

        # Outer circle
        coin['id'] = self.canvas.create_oval(
            x - size, y - size, x + size, y + size,
            fill=color1, outline=color2, width=2
        )

        # Inner highlight
        self.canvas.create_oval(
            x - size + 5, y - size + 5, x - 5, y - 5,
            fill=color2, outline=''
        )

        # Coin symbol
        symbol = '🪙' if coin['type'] == 'gold' else ('💰' if coin['type'] == 'silver' else '🪙')
        self.canvas.create_text(
            x, y, text=symbol, font=('Arial', 16), fill='white'
        )

    def pop_coin(self, event):
        """Handle coin clicking"""
        if not self.game_running:
            return

        x, y = event.x, event.y

        # Check if click is on any coin
        for coin in self.coins[:]:
            coin_x, coin_y = coin['x'], coin['y']
            distance = ((x - coin_x) ** 2 + (y - coin_y) ** 2) ** 0.5

            if distance <= 25:  # Coin radius
                # Pop the coin
                self.pop_effect(coin)
                self.coins.remove(coin)

                # Add score
                colors = {'gold': 50, 'silver': 30, 'bronze': 10}
                self.score += colors[coin['type']]
                self.update_score()
                break

    def pop_effect(self, coin):
        """Create pop effect animation"""
        x, y = coin['x'], coin['y']

        # Create explosion particles
        particles = []
        for _ in range(8):
            angle = random.uniform(0, 2 * 3.14159)
            speed = random.uniform(2, 5)
            particle = {
                'x': x,
                'y': y,
                'vx': speed * random.uniform(0.5, 1.5) * random.choice([-1, 1]),
                'vy': speed * random.uniform(0.5, 1.5) * random.choice([-1, 1]),
                'life': 20
            }
            particles.append(particle)

        def animate_particles():
            for particle in particles[:]:
                particle['x'] += particle['vx']
                particle['y'] += particle['vy']
                particle['life'] -= 1

                if particle['life'] <= 0:
                    particles.remove(particle)
                    continue

                # Draw particle
                size = max(1, particle['life'] // 2)
                self.canvas.create_oval(
                    particle['x'] - size, particle['y'] - size,
                    particle['x'] + size, particle['y'] + size,
                    fill='yellow', outline=''
                )

            if particles:
                self.root.after(30, animate_particles)
            else:
                # Clean up
                self.canvas.delete("all")
                # Redraw remaining coins
                for coin in self.coins:
                    self.draw_coin(coin)

        animate_particles()

    def game_over(self):
        """Handle game over"""
        self.game_running = False
        self.start_button.config(state='normal')

        messagebox.showinfo(
            "Time's Up!",
            f"Time's Up!\n\nFinal Score: {self.score}\n\nGreat job! Try again to beat your score!"
        )


def main():
    root = tk.Tk()
    game = PopCoinsGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()