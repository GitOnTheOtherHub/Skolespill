"""A simple 2D side-scrolling platform game built with pygame.

The player starts on the left edge of the screen and must reach the gold flag
on the right edge. Along the way, randomly placed enemies patrol the ground.
The player can attack with the Z key to kill enemies and rack up a score, but
touching a live enemy ends the game.

Gameplay flow:
    1. ``reset()`` creates a fresh :class:`Player`, a list of :class:`Enemy`
       objects, a zeroed score, and sets the game state to ``"playing"``.
    2. The main loop handles input events (attacking with Z, restarting with R),
       updates the player and enemies, and resolves collisions.
    3. The game state transitions to ``"won"`` when the player reaches the goal
       zone, or to ``"dead"`` when the player collides with a live enemy.
    4. While in a terminal state, pressing R calls ``reset()`` to start over.

Controls:
    Left / A:        Move left.
    Right / D:       Move right.
    Space / Up / W:  Jump (only while on the ground).
    Z:               Attack in the facing direction.
    R:               Restart after winning or dying.

States:
    "playing": Normal interactive gameplay.
    "won":     Player reached the goal; shows a victory screen.
    "dead":    Player touched an enemy; shows a game-over screen.
"""

import pygame
import random
import sys

# Initialize all imported pygame modules (display, font, etc.).
pygame.init()

# --- Screen / display configuration -------------------------------------------
WIDTH, HEIGHT = 960, 540                       # Window size in pixels.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Run to the Right!")
clock = pygame.time.Clock()                    # Used to cap the frame rate.
FPS = 60                                        # Target frames per second.

# --- Color palette (R, G, B) --------------------------------------------------
SKY = (135, 206, 235)
GROUND = (96, 64, 32)
GRASS = (60, 160, 60)
PLAYER_C = (40, 90, 200)
ENEMY_C = (200, 50, 50)
ATTACK_C = (255, 230, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOAL_C = (255, 215, 0)

# --- World physics / layout constants -----------------------------------------
GROUND_Y = HEIGHT - 80          # Y coordinate of the top of the ground strip.
GRAVITY = 0.8                   # Downward acceleration applied each frame.
font = pygame.font.SysFont("arial", 24)               # HUD text.
big_font = pygame.font.SysFont("arial", 56, bold=True)  # End-screen text.


class Player:


    def __init__(self):
    
        self.w, self.h = 36, 56
        self.x = 40
        self.y = GROUND_Y - self.h   # Place feet on the ground.
        self.vx = 0
        self.vy = 0
        self.speed = 5
        self.jump = -15              # Negative because up is the -Y direction.
        self.on_ground = True
        self.facing = 1              # Start facing right toward the goal.
        self.attacking = 0           # Counts down to 0 after an attack.

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        """Update position from input, apply gravity, and tick the attack timer."""
        keys = pygame.key.get_pressed()   # Snapshot of held-down keys.

        # --- Horizontal movement ---
        self.vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -self.speed
            self.facing = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = self.speed
            self.facing = 1

        # Apply horizontal movement and clamp within the screen bounds.
        self.x += self.vx
        self.x = max(0, min(WIDTH - self.w, self.x))

        # Count down the attack animation timer.
        if self.attacking > 0:
            self.attacking -= 1

    def draw(self, surf):
        """Draw the player, its eye, and the attack hitbox when active.

        Args:
            surf (pygame.Surface): Surface to draw onto.
        """
        pygame.draw.rect(surf
                         , PLAYER_C
                         , self.rect
                         , border_radius=6)
        # Position the eye on the side the player is facing.
        ex = self.x + (self.w - 12 if self.facing == 1 else 4)
        pygame.draw.circle(surf, WHITE, (ex + 4, self.y + 18), 5)
        pygame.draw.circle(surf, BLACK, (ex + 5, self.y + 18), 2)
        # Show the attack flash while the attack timer is running.
        if self.attacking > 0:
            pygame.draw.rect(surf, ATTACK_C, self.attack_rect(), border_radius=4)


class Enemy:
    """A patrolling ground enemy.

    Each enemy walks back and forth between a randomized left/right boundary at
    a randomized speed until killed.

    Attributes:
        w (int): Enemy width in pixels.
        h (int): Enemy height in pixels.
        x (float): Left position in pixels.
        y (float): Top position in pixels.
        dir (int): Current walk direction; 1 for right, -1 for left.
        speed (float): Patrol speed in pixels per frame.
        left (float): Left boundary of the patrol range.
        right (float): Right boundary of the patrol range.
        alive (bool): Whether the enemy is still active.
    """

    def __init__(self, x):
        """Create an enemy centered around a spawn x-coordinate.

        Args:
            x (int): The approximate horizontal spawn position; the patrol
                range is derived randomly around this value.
        """
        self.w, self.h = 34, 48
        self.x = x
        self.y = GROUND_Y - self.h               # Stand on the ground.
        self.dir = random.choice([-1, 1])        # Random initial direction.
        self.speed = random.uniform(1.2, 2.6)    # Random patrol speed.
        self.left = x - random.randint(40, 120)  # Random left patrol bound.
        self.right = x + random.randint(40, 120) # Random right patrol bound.
        self.alive = True

    @property
    def rect(self):
        """pygame.Rect: The enemy's bounding box for collision checks."""
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        """Move the enemy and reverse direction at its patrol boundaries."""
        self.x += self.dir * self.speed
        # If a boundary is crossed, flip direction and clamp back in range.
        if self.x < self.left or self.x > self.right:
            self.dir *= -1
            self.x = max(self.left, min(self.right, self.x))

    def draw(self, surf):
        """Draw the enemy body and a single eye.

        Args:
            surf (pygame.Surface): Surface to draw onto.
        """
        pygame.draw.rect(surf, ENEMY_C, self.rect, border_radius=6)
        pygame.draw.circle(surf, WHITE, (int(self.x + self.w / 2), self.y + 16), 4)
        pygame.draw.circle(surf, BLACK, (int(self.x + self.w / 2), self.y + 16), 2)


def make_enemies():
    """Create a list of enemies at random positions across the level.

    Returns:
        list[Enemy]: Seven enemies spawned between the start and goal zones.
    """
    enemies = []
    for i in range(7):
        # Keep spawns away from the player start and the goal flag.
        ex = random.randint(220, WIDTH - 160)
        enemies.append(Enemy(ex))
    return enemies


def reset():
    """Build a fresh game state.

    Returns:
        tuple: ``(player, enemies, score, state)`` where ``player`` is a new
        :class:`Player`, ``enemies`` is a list of :class:`Enemy`, ``score`` is
        ``0``, and ``state`` is ``"playing"``.
    """
    return Player(), make_enemies(), 0, "playing"


def draw_world():
    """Draw the static scenery: sky, grass, ground, and the goal flag."""
    screen.fill(SKY)
    pygame.draw.rect(screen, GRASS, (0, GROUND_Y - 10, WIDTH, 10))      # Grass strip.
    pygame.draw.rect(screen, GROUND, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))  # Dirt.
    # Goal zone (gold pillar) on the right edge.
    pygame.draw.rect(screen, GOAL_C, (WIDTH - 50, GROUND_Y - 120, 50, 120))
    # A small triangular flag attached to the goal.
    flag = [(WIDTH - 50, GROUND_Y - 120), (WIDTH - 90, GROUND_Y - 105), (WIDTH - 50, GROUND_Y - 90)]
    pygame.draw.polygon(screen, ENEMY_C, flag)


# Create the initial game state before entering the main loop.
player, enemies, score, state = reset()

# --- Main game loop -----------------------------------------------------------
running = True
while running:
    # --- Event handling: discrete key presses and window close ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Z triggers an attack only during active gameplay.
            if event.key == pygame.K_z and state == "playing":
                player.attacking = 10            # Start the attack animation.
                hit = player.attack_rect()       # Compute the attack hitbox.
                # Kill any live enemy overlapping the hitbox.
                for e in enemies:
                    if e.alive and hit.colliderect(e.rect):
                        e.alive = False
                        score += 1
            # R restarts the game from a won/dead state.
            if event.key == pygame.K_r and state != "playing":
                player, enemies, score, state = reset()

    # --- Update phase (only while playing) ---
    if state == "playing":
        player.update()
        for e in enemies:
            if e.alive:
                e.update()
                # Dying: touching a live enemy while not mid-attack is fatal.
                if player.attacking == 0 and player.rect.colliderect(e.rect):
                    state = "dead"
        # Winning: reaching the goal zone on the right edge.
        if player.x + player.w >= WIDTH - 50:
            state = "won"

    # --- Draw phase ---
    draw_world()
    for e in enemies:
        if e.alive:
            e.draw(screen)
    player.draw(screen)

    # HUD: number of enemies killed and remaining.
    alive = sum(1 for e in enemies if e.alive)
    screen.blit(font.render(f"Killed: {score}", True, BLACK), (12, 12))
    screen.blit(font.render(f"Enemies left: {alive}", True, BLACK), (12, 40))

    # End-of-game overlays.
    if state == "won":
        msg = big_font.render("YOU MADE IT!", True, (20, 120, 20))
        screen.blit(msg, msg.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30)))
        sub = font.render(f"Enemies killed: {score}   Press R to play again", True, BLACK)
        screen.blit(sub, sub.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20)))
    elif state == "dead":
        msg = big_font.render("YOU DIED", True, (160, 20, 20))
        screen.blit(msg, msg.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30)))
        sub = font.render(f"Enemies killed: {score}   Press R to retry", True, BLACK)
        screen.blit(sub, sub.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20)))

    # Present the frame and wait to maintain the target frame rate.
    pygame.display.flip()
    clock.tick(FPS)

# Clean up pygame and exit the process.
pygame.quit()
sys.exit()