import tkinter as tk
from tkinter import messagebox
import random
import time


class SpaceShooterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Shooter Game")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        # Game variables
        self.canvas_width = 500
        self.canvas_height = 500
        self.player_x = self.canvas_width // 2
        self.player_y = self.canvas_height - 50
        self.player_speed = 8
        self.bullets = []
        self.enemies = []
        self.explosions = []
        self.score = 0
        self.lives = 3
        self.game_running = False
        self.level = 1
        self.enemy_speed = 2
        self.bullet_speed = 10

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

        self.canvas = tk.Canvas(
            canvas_frame,
            width=self.canvas_width,
            height=self.canvas_height,
            bg='black',
            highlightthickness=1
        )
        self.canvas.pack()

        # Draw stars background
        self.draw_stars()

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

        # Lives
        lives_container = tk.Frame(display_frame, relief='solid', bd=1)
        lives_container.pack(side=tk.LEFT, padx=10)

        self.lives_label = tk.Label(
            lives_container,
            text="3",
            font=('Arial', 16, 'bold')
        )
        self.lives_label.pack(pady=(0, 5))

        # Level
        level_container = tk.Frame(display_frame, relief='solid', bd=1)
        level_container.pack(side=tk.LEFT, padx=10)

        self.level_label = tk.Label(
            level_container,
            text="1",
            font=('Arial', 16, 'bold')
        )
        self.level_label.pack(pady=(0, 5))

    def draw_stars(self):
        """Draw background stars"""
        for _ in range(50):
            x = random.randint(0, self.canvas_width)
            y = random.randint(0, self.canvas_height)
            size = random.randint(1, 3)
            brightness = random.randint(150, 255)
            color = f'#{brightness:02x}{brightness:02x}{brightness:02x}'
            self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline='')

    def start_game(self):
        """Start the game"""
        if not self.game_running:
            self.game_running = True
            self.start_button.config(state='disabled')
            self.pause_button.config(state='normal')
            self.spawn_enemies()
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
        self.player_x = self.canvas_width // 2
        self.bullets = []
        self.enemies = []
        self.explosions = []
        self.score = 0
        self.lives = 3
        self.level = 1
        self.enemy_speed = 2

        self.start_button.config(state='normal', text="🎮 Start Game")
        self.pause_button.config(state='disabled', text="⏸️ Pause")

        self.update_display()
        self.draw_game()

    def handle_keypress(self, event):
        """Handle keyboard input"""
        if not self.game_running:
            return

        key = event.keysym.lower()

        if key in ['a', 'left'] and self.player_x > 20:
            self.player_x -= self.player_speed
        elif key in ['d', 'right'] and self.player_x < self.canvas_width - 20:
            self.player_x += self.player_speed
        elif key == 'space':
            self.shoot_bullet()

        self.draw_game()

    def shoot_bullet(self):
        """Shoot a bullet"""
        # Prevent too many bullets
        if len([b for b in self.bullets if b['active']]) < 5:
            bullet = {
                'x': self.player_x,
                'y': self.player_y - 20,
                'active': True
            }
            self.bullets.append(bullet)

    def spawn_enemies(self):
        """Spawn enemies for current level"""
        num_enemies = min(5 + self.level, 12)  # Max 12 enemies

        for i in range(num_enemies):
            enemy = {
                'x': random.randint(30, self.canvas_width - 30),
                'y': random.randint(-100, -20),
                'active': True,
                'type': random.choice(['alien1', 'alien2', 'alien3'])
            }
            self.enemies.append(enemy)

    def game_loop(self):
        """Main game loop"""
        if not self.game_running:
            return

        self.update_game()
        self.draw_game()
        self.check_collisions()

        # Check level completion
        if not any(e['active'] for e in self.enemies):
            self.level_complete()

        # Schedule next frame
        self.root.after(50, self.game_loop)

    def update_game(self):
        """Update game state"""
        # Update bullets
        for bullet in self.bullets:
            if bullet['active']:
                bullet['y'] -= self.bullet_speed
                if bullet['y'] < -10:
                    bullet['active'] = False

        # Update enemies
        for enemy in self.enemies:
            if enemy['active']:
                enemy['y'] += self.enemy_speed

                # Check if enemy reached bottom
                if enemy['y'] > self.canvas_height:
                    enemy['active'] = False
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_over()
                    else:
                        self.update_display()

        # Update explosions
        for explosion in self.explosions[:]:
            explosion['life'] -= 1
            if explosion['life'] <= 0:
                self.explosions.remove(explosion)

    def check_collisions(self):
        """Check for collisions between bullets and enemies"""
        for bullet in self.bullets:
            if not bullet['active']:
                continue

            for enemy in self.enemies:
                if not enemy['active']:
                    continue

                # Simple collision detection
                if (abs(bullet['x'] - enemy['x']) < 20 and
                    abs(bullet['y'] - enemy['y']) < 20):
                    # Hit!
                    bullet['active'] = False
                    enemy['active'] = False
                    self.score += 10 * self.level

                    # Create explosion
                    explosion = {
                        'x': enemy['x'],
                        'y': enemy['y'],
                        'life': 10
                    }
                    self.explosions.append(explosion)

                    self.update_display()
                    break

    def level_complete(self):
        """Handle level completion"""
        self.level += 1
        self.enemy_speed += 0.5
        self.score += 100 * self.level  # Level bonus

        self.update_display()

        # Brief pause before next level
        self.game_running = False
        self.root.after(2000, lambda: self.start_next_level())

    def start_next_level(self):
        """Start the next level"""
        self.enemies = []
        self.bullets = []
        self.explosions = []
        self.spawn_enemies()
        self.game_running = True
        self.game_loop()

    def draw_game(self):
        """Draw the game state"""
        self.canvas.delete("all")

        # Redraw stars
        self.draw_stars()

        # Draw player ship
        self.draw_player()

        # Draw bullets
        for bullet in self.bullets:
            if bullet['active']:
                self.canvas.create_oval(
                    bullet['x'] - 2, bullet['y'] - 2,
                    bullet['x'] + 2, bullet['y'] + 2,
                    fill='cyan', outline='cyan'
                )

        # Draw enemies
        for enemy in self.enemies:
            if enemy['active']:
                self.draw_enemy(enemy)

        # Draw explosions
        for explosion in self.explosions:
            size = (11 - explosion['life']) * 3
            self.canvas.create_oval(
                explosion['x'] - size, explosion['y'] - size,
                explosion['x'] + size, explosion['y'] + size,
                fill='red', outline='red'
            )

    def draw_player(self):
        """Draw the player ship"""
        # Ship body
        self.canvas.create_polygon(
            self.player_x, self.player_y + 20,
            self.player_x - 15, self.player_y,
            self.player_x + 15, self.player_y,
            fill='blue', outline='blue', width=2
        )

        # Ship cockpit
        self.canvas.create_oval(
            self.player_x - 5, self.player_y - 5,
            self.player_x + 5, self.player_y + 5,
            fill='yellow', outline='yellow'
        )

    def draw_enemy(self, enemy):
        """Draw an enemy ship"""
        x, y = enemy['x'], enemy['y']

        if enemy['type'] == 'alien1':
            # Simple alien ship
            self.canvas.create_oval(
                x - 12, y - 8, x + 12, y + 8,
                fill='red', outline='red'
            )
            # Eyes
            self.canvas.create_oval(x - 6, y - 3, x - 3, y, fill='#000000')
            self.canvas.create_oval(x + 3, y - 3, x + 6, y, fill='#000000')

        elif enemy['type'] == 'alien2':
            # Different alien
            self.canvas.create_polygon(
                x, y - 10, x - 10, y + 5, x + 10, y + 5,
                fill='purple', outline='purple'
            )

        else:  # alien3
            # Another alien type
            self.canvas.create_rectangle(
                x - 8, y - 6, x + 8, y + 6,
                fill='green', outline='green'
            )

    def update_display(self):
        """Update score display"""
        self.score_label.config(text=str(self.score))
        self.lives_label.config(text='♥' * self.lives)
        self.level_label.config(text=str(self.level))

    def game_over(self):
        """Handle game over"""
        self.game_running = False
        self.start_button.config(state='normal')
        self.pause_button.config(state='disabled')

        messagebox.showinfo(
            "Game Over",
            f"Game Over!\n\nFinal Score: {self.score}\nLevel Reached: {self.level}\n\nEarth has been invaded! Try again!"
        )


def main():
    root = tk.Tk()
    game = SpaceShooterGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()