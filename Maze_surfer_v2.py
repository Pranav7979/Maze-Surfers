import pygame
import random
import sys

# Constants
CELL_SIZE = 40
COLS, ROWS = 7, 8  # Maze size (columns x rows)
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
win = pygame.display.set_mode((360, 640))
pygame.display.set_caption("Maze Surfers")
clock = pygame.time.Clock()

pygame.font.init()

font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 16)
Start = font.render('START', True, WHITE)

high_score_val = 0
score_val = 0

def score_display(x1,y1,x2,y2):
    global high_score_val, score_val

    if score_val > high_score_val:
        high_score_val = score_val

    Score = font2.render('SCORE : ' + str(score_val), True, WHITE)
    High_Score = font2.render('HIGH SCORE : ' + str(high_score_val), True, WHITE)
    win.blit(Score, (x1, y1))
    win.blit(High_Score, (x2, y2))

pla = pygame.image.load('stop.png')
def player(x,y):
    win.blit(pla,(x,y))


# Cell class
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = [True, True, True, True]  # Top, Right, Bottom, Left
        self.visited = False

    def draw(self, win, i):
        x, y = self.x * CELL_SIZE+40, self.y * CELL_SIZE+i
        if self.walls[0]:  # Top
            pygame.draw.line(win, WHITE, (x, y), (x + CELL_SIZE, y))
        if self.walls[1]:  # Right
            pygame.draw.line(win, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
        if self.walls[2]:  # Bottom
            pygame.draw.line(win, WHITE, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE))
        if self.walls[3]:  # Left
            pygame.draw.line(win, WHITE, (x, y + CELL_SIZE), (x, y))

    def highlight(self, win, color=(0, 255, 0)):
        x, y = self.x * CELL_SIZE+40, self.y * CELL_SIZE
        pygame.draw.rect(win, color, (x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4))

def index(x, y):
    if 0 <= x < COLS and 0 <= y < ROWS:
        return y * COLS + x
    return None

def remove_walls(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    if dx == 1:
        a.walls[3] = b.walls[1] = False  # Remove left-right wall
    elif dx == -1:
        a.walls[1] = b.walls[3] = False
    elif dy == 1:
        a.walls[0] = b.walls[2] = False  # Remove top-bottom wall
    elif dy == -1:
        a.walls[2] = b.walls[0] = False

# Create grid of cells
# grid = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
grid1 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
grid2 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
grid3 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
rand = []

def rand_gen():
    a, b = 0, 0
    while (a-b==-1) or (a-b==0) or (a-b==1):
        a=random.randint(0,6)
        b=random.randint(0,6)
    return [a,b]

# Maze generation using recursive backtracking
def generate_maze(grid, cont=0):
    stack = []
    current = grid[0]
    current.visited = True
    global rand

    while True:
        next_cell = get_unvisited_neighbor(current,grid)
        if next_cell:
            next_cell.visited = True
            stack.append(current)
            remove_walls(current, next_cell)
            current = next_cell
        elif stack:
            current = stack.pop()
        else:
            break

    if rand:
        grid[49+rand[0]].walls[2]=False
        grid[49+rand[1]].walls[2]=False
    rand.clear()
    rand = rand_gen()
    grid[rand[0]].walls[0]=False
    grid[rand[1]].walls[0]=False

        # i=0
        # Visualization
        # win.fill(BLACK)
        # for cell in grid:
        #     cell.draw(win,i)
        # current.highlight(win)
        # pygame.display.flip()
        # clock.tick(FPS)

def get_unvisited_neighbor(cell,grid):
    neighbors = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for i, (dx, dy) in enumerate(directions):
        neighbor_index = index(cell.x + dx, cell.y + dy)
        if neighbor_index is not None:
            neighbor = grid[neighbor_index]
            if not neighbor.visited:
                neighbors.append(neighbor)
    return random.choice(neighbors) if neighbors else None

def recreate(grid):
    # global grid1
    grid.clear()
    grid = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
    generate_maze(grid)

# Main loop
def main():
    global grid1, grid2, grid3
    # generate_maze(grid1)
    # generate_maze(grid2)
    # generate_maze(grid3)
    # i1=320
    # i2=0
    # i3=-320
    # px=164
    # py=444

    release = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        win.blit(Start, (130, 300))
        if event.type == pygame.KEYDOWN:
            release =False
            break

        pygame.display.flip()
        clock.tick(FPS)


    while True:
        grid1.clear()
        grid2.clear()
        grid3.clear()
        grid1 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
        grid2 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
        grid3 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
        generate_maze(grid1)
        generate_maze(grid2)
        generate_maze(grid3)
        i1=320
        i2=0
        i3=-320
        px=164
        py=324
        global score_val
        global high_score_val
        score_val = 0

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        status = True

        while status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if i1 == 640:
                i1=-320
                # recreate(grid1)
                grid1.clear()
                grid1 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
                generate_maze(grid1)
            if i2 == 640:
                i2=-320
                # recreate(grid1)
                grid2.clear()
                grid2 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
                generate_maze(grid2)
            if i3 == 640:
                i3=-320
                # recreate(grid1)
                grid3.clear()
                grid3 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
                generate_maze(grid3)

            win.fill(BLACK)
            for cell in grid1:
                cell.draw(win,i1)
            for cell in grid2:
                cell.draw(win,i2)
            for cell in grid3:
                cell.draw(win,i3)

            pygame.draw.line(win, RED, (0,580), (360, 580))
            pygame.draw.rect(win, BLACK, pygame.Rect(0, 0, 360, 40))

            score = font.render('SCORE : ' + str(score_val), True, WHITE)
            win.blit(score, (20, 4))

            player(px,py)

            if event.type == pygame.KEYUP:
                release = True

            if event.type == pygame.KEYDOWN and release == True:
                release = False
                if event.key == pygame.K_UP:
                    while BLACK == win.get_at((px,py-4)):
                        if (BLACK == win.get_at((px-4,py-4)) or BLACK == win.get_at((px+36,py-4))) and BLACK == win.get_at((px,py-4)):
                            py-=39
                            break
                        py-=1
                        pygame.display.flip()
                        # clock.tick(FPS)
                elif event.key == pygame.K_DOWN:
                    while BLACK == win.get_at((px,py+36)):
                        if (BLACK == win.get_at((px-4,py+36)) or BLACK == win.get_at((px+36,py+36))) and BLACK == win.get_at((px,py+36)):
                            py+=39
                            break
                        py+=1
                        pygame.display.flip()
                        # clock.tick(FPS)
                elif event.key == pygame.K_RIGHT:
                    while BLACK == win.get_at((px+36,py)):
                        if (BLACK == win.get_at((px+36,py-4)) or BLACK == win.get_at((px+36,py+36))) and BLACK == win.get_at((px+36,py)):
                            px+=39
                            break
                        px+=1
                        pygame.display.flip()
                        # clock.tick(FPS)
                elif event.key == pygame.K_LEFT:
                    while BLACK == win.get_at((px-4,py)):
                        if (BLACK == win.get_at((px-4,py-4)) or BLACK == win.get_at((px-4,py+36))) and BLACK == win.get_at((px-4,py)):
                            px-=39
                            break
                        px-=1
                        pygame.display.flip()
                        # clock.tick(FPS)

            if py >= 548:
                status = False
            if py <= 44:
                py=44 + (i1+400)%40

            speed = int(score_val/500)

            pygame.display.flip()
            clock.tick(FPS + speed)
            i1+=2
            i2+=2
            i3+=2
            py+=2
            score_val+=1
            # if i==20:
            #     grid1.clear()
            #     grid1 = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
            #     generate_maze(grid1)
        
        pygame.time.delay(2000)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYUP:
                release = True

            win.fill(BLACK)
            win.blit(Start, (130, 300))
            score_display(20, 46, 20, 20)
            if event.type == pygame.KEYDOWN and release == True:
                break

            pygame.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    main()
