# Maze generating algorithm using backtracking
# Written by Haider Rauf
# Started on 6 / 8 / 2020
import pygame
import random
from constants import *


class Engine:
    def __init__(self):
        # pygame init stuff
        pygame.init()
        pygame.display.set_mode((MAZE_WIDTH, MAZE_HEIGHT))
        pygame.display.set_caption("Maze Generator by HaiderRauf")
        self.window: pygame.Surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.running = True
        self.cells = [[0 for col in range(CELL_COLS)] for row in range(CELL_ROWS)]
        self.stack = []
        # mark (0, 0) as visited and push to stack...
        self.stack.append((0, 0))
        self.cells[0][0] |= CELL_VISITED
        self.visited_cells = 1
        self.paused = False

    def get_neighbours(self, x, y):
        neighbours = []
        if x > 0 and (self.cells[y][x - 1] & CELL_VISITED == 0):
            neighbours.append(DIR_WEST)
        if x < CELL_COLS - 1 and (self.cells[y][x + 1] & CELL_VISITED == 0):
            neighbours.append(DIR_EAST)
        if y > 0 and (self.cells[y - 1][x] & CELL_VISITED == 0):
            neighbours.append(DIR_NORTH)
        if y < CELL_ROWS - 1 and (self.cells[y + 1][x] & CELL_VISITED == 0):
            neighbours.append(DIR_SOUTH)
        return neighbours

    def draw_borders(self):
        self.window.fill(BORDER_CLR, (0, 0, MAZE_WIDTH, WALL_SIZE))
        self.window.fill(BORDER_CLR, (0, MAZE_HEIGHT - WALL_SIZE, MAZE_WIDTH, WALL_SIZE))
        self.window.fill(BORDER_CLR, (0, 0, WALL_SIZE, MAZE_HEIGHT))
        self.window.fill(BORDER_CLR, (MAZE_WIDTH - WALL_SIZE, 0, WALL_SIZE, MAZE_HEIGHT))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused

    def update(self):
        if not self.paused and self.visited_cells < TOTAL_CELLS:
            x, y = self.stack[-1]
            neighbours = self.get_neighbours(x, y)
            if neighbours:
                next_dir = neighbours[random.randint(0, len(neighbours) - 1)]
                if next_dir == DIR_NORTH:
                    self.stack.append((x, y - 1))
                    self.cells[y][x] |= NORTH_WALL
                    self.cells[y - 1][x] |= SOUTH_WALL
                    self.cells[y - 1][x] |= CELL_VISITED
                elif next_dir == DIR_SOUTH:
                    self.stack.append((x, y + 1))
                    self.cells[y][x] |= SOUTH_WALL
                    self.cells[y + 1][x] |= NORTH_WALL
                    self.cells[y + 1][x] |= CELL_VISITED
                elif next_dir == DIR_EAST:
                    self.stack.append((x + 1, y))
                    self.cells[y][x] |= EAST_WALL
                    self.cells[y][x + 1] |= WEST_WALL
                    self.cells[y][x + 1] |= CELL_VISITED
                elif next_dir == DIR_WEST:
                    self.stack.append((x - 1, y))
                    self.cells[y][x] |= WEST_WALL
                    self.cells[y][x - 1] |= EAST_WALL
                    self.cells[y][x - 1] |= CELL_VISITED
                self.visited_cells += 1
            else:
                self.stack.pop()
        self.clock.tick(60) # cap FPS at 60.0

    def render(self):
        self.window.fill(CLR_BLACK)
        # Drawing Begin

        for y in range(CELL_ROWS):
            for x in range(CELL_COLS):
                if self.cells[y][x] & CELL_VISITED:
                    self.window.fill(PATH_CLR, (x * (CELL_SIZE + WALL_SIZE) + WALL_SIZE,
                                                y * (CELL_SIZE + WALL_SIZE) + WALL_SIZE, CELL_SIZE, CELL_SIZE))
                else:
                    self.window.fill(CELL_CLR, (x * (CELL_SIZE + WALL_SIZE) + WALL_SIZE,
                                                y * (CELL_SIZE + WALL_SIZE) + WALL_SIZE, CELL_SIZE, CELL_SIZE))

                if self.cells[y][x] & SOUTH_WALL:
                    self.window.fill(PATH_CLR, (x * (CELL_SIZE + WALL_SIZE) + WALL_SIZE,
                                                y * (CELL_SIZE + WALL_SIZE) + WALL_SIZE, CELL_SIZE,
                                                CELL_SIZE + WALL_SIZE))
                if self.cells[y][x] & EAST_WALL:
                    self.window.fill(PATH_CLR, (x * (CELL_SIZE + WALL_SIZE) + WALL_SIZE,
                                                y * (CELL_SIZE + WALL_SIZE) + WALL_SIZE,
                                                CELL_SIZE + WALL_SIZE, CELL_SIZE))

                if self.visited_cells < TOTAL_CELLS and (x, y) == self.stack[-1]:
                    self.window.fill(CURSOR_CLR, (x * (CELL_SIZE + WALL_SIZE) + WALL_SIZE,
                                                  y * (CELL_SIZE + WALL_SIZE) + WALL_SIZE, CELL_SIZE, CELL_SIZE))

                self.draw_borders()
        # Drawing End
        pygame.display.flip()

    def main_loop(self):
        print(self.window)
        while self.running:
            self.handle_input()
            self.update()
            self.render()
        pygame.quit()


def main():
    engine = Engine()
    engine.main_loop()


if __name__ == '__main__':
    main()
