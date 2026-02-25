import pygame
from Maze import Maze
import random

# -------- CONFIG --------
CELL_SIZE = 20
MAZE_WIDTH = 31   # Must be odd
MAZE_HEIGHT = 31  # Must be odd

WHITE = (240, 240, 240)
BLACK = (30, 30, 30)

# -------- MAZE CLASS --------
class Maze:
    def __init__(self, width, height):
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]

    def generate(self):
        stack = []
        start_x, start_y = 1, 1
        self.grid[start_y][start_x] = 0
        stack.append((start_x, start_y))

        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

        while stack:
            x, y = stack[-1]
            neighbors = []

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1:
                    if self.grid[ny][nx] == 1:
                        neighbors.append((nx, ny, dx, dy))

            if neighbors:
                nx, ny, dx, dy = random.choice(neighbors)

                self.grid[y + dy // 2][x + dx // 2] = 0
                self.grid[ny][nx] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

        return self.grid

def main():
    pygame.init()

    maze = Maze(MAZE_WIDTH, MAZE_HEIGHT)
    grid = maze.generate()

    screen_width = MAZE_WIDTH * CELL_SIZE
    screen_height = MAZE_HEIGHT * CELL_SIZE

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Generator")

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                if grid[y][x] == 0:
                    pygame.draw.rect(
                        screen,
                        WHITE,
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    )

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()