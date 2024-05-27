import pygame
import sys
from pygame.locals import *



pygame.init()

WIDTH = 1400
HEIGHT = 600
CELL_SIZE = 30
WHITE = "white"
BLACK = "black"
RED = "red"
TIMER_COUNTDOWN = 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

interface = pygame.Surface((230, 600))
interface.fill("white")


game_name_font= pygame.font.Font(None, 100 )
game_name = game_name_font.render('MAZE RUNNER', False, 'black')
clock = pygame.time.Clock()

enemy_move_delay = 300  # enemy speed
last_enemy_move_time = pygame.time.get_ticks()
player_movement_count = 0


    

# (0 for path, 1 for wall)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2, 1], 
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

 
player_x = 1
player_y = 2




enemies = [(1, 4)]

 
def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, "green", (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_enemies():
    for enemy in enemies:
        pygame.draw.circle(screen, RED, (enemy[0] * CELL_SIZE + CELL_SIZE // 2, enemy[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

def draw_timer(seconds_left):
    timer_font = pygame.font.Font(None, 60)
    timer_label = timer_font.render('Timer', False, "black" )
    minutes = str(seconds_left // 60).zfill(2)  # zfills Ensures the  minutes and seconds are displayed with two digits
    seconds = str(seconds_left % 60).zfill(2)   
    time_remaining = timer_font.render(f'{minutes}:{seconds}', True, BLACK)
    screen.blit(timer_label, (1227, 20))
    screen.blit(time_remaining, (1227, 65))

def heuristic(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def astar(maze, start, end):
    open_list = [start]
    closed_list = []
    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_list:
        current = min(open_list, key=lambda x: f_score.get(x, float('inf')))
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        open_list.remove(current)
        closed_list.append(current)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + dx, current[1] + dy
            if neighbor in closed_list or maze[neighbor[1]][neighbor[0]] == 1:
                continue

            tentative_g_score = g_score[current] + 1
            if neighbor not in open_list or tentative_g_score < g_score.get(neighbor, 0):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None

enemies_started_chasing = False
def move_enemies():
    global last_enemy_move_time, player_movement_count, enemies_started_chasing

    if not enemies_started_chasing and abs(player_x - 1) + abs(player_y - 1) >= 5:
        enemies_started_chasing = True

    # Check if enough time has passed since the last enemy move
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_move_time < enemy_move_delay:
        return

    last_enemy_move_time = current_time  


    # Move enemies if they have started chasing
    if enemies_started_chasing:
        for i, enemy in enumerate(enemies):
            path = astar(maze, enemy, (player_x, player_y))
            if path:
                next_step = path[1] if len(path) > 1 else path[0]
                enemies[i] = next_step




def move_player(event):
    global player_x, player_y, player_movement_count
    if event.key == pygame.K_LEFT and maze[player_y][player_x - 1] != 1:
        player_x -= 1
        player_movement_count += 1
    elif event.key == pygame.K_RIGHT and maze[player_y][player_x + 1] != 1:
        player_x += 1
        player_movement_count += 1
    elif event.key == pygame.K_UP and maze[player_y - 1][player_x] != 1:
        player_y -= 1
        player_movement_count += 1
    elif event.key == pygame.K_DOWN and maze[player_y + 1][player_x] != 1:
        player_movement_count += 1
        player_y += 1
    print("Player Position:", player_x, player_y)


try_again_font = pygame.font.Font(None, 40)
try_again_label = try_again_font.render('Try Again', True, "black")
def display_win_message():
    win_font = pygame.font.Font(None, 65)
    win_label = win_font.render('You Win!', True, BLACK)
    interface.blit(win_label, (15, 230))
    try_again_rect = try_again_label.get_rect(center=(115, 300))
    pygame.draw.rect(interface, BLACK, try_again_rect, 2)
    interface.blit(try_again_label, try_again_rect.topleft)

    pygame.display.flip()

def display_lose_message():
    lose_font = pygame.font.Font(None, 65)
    lose_label = lose_font.render('You Lose!', True, BLACK)
    interface.blit(lose_label, (15, 230))
    try_again_rect = try_again_label.get_rect(center=(115, 300))
    pygame.draw.rect(interface, BLACK, try_again_rect, 2)
    interface.blit(try_again_label, try_again_rect.topleft)

    pygame.display.flip()






running = True
player_won = False
player_lost = False
start_ticks = pygame.time.get_ticks()

while running:
    # Calculate time passed
    if not player_won and not player_lost:
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        seconds_left = max(0, TIMER_COUNTDOWN - seconds_passed)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif not player_won and not player_lost:
            if event.type == pygame.KEYDOWN:
                move_player(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and (player_won or player_lost):
            print("mouse_clicked")
            mouse_pos = pygame.mouse.get_pos()
            try_again_rect = try_again_label.get_rect(center=(115, 300))
            button_rect_on_screen = try_again_rect.move(1170, 0)
            if button_rect_on_screen.collidepoint(mouse_pos):
                interface.fill(WHITE)
                player_x, player_y = 1, 2
                player_movement_count = 0
                enemies = [(1, 4)]
                enemies_started_chasing = False
                start_ticks = pygame.time.get_ticks()   
                player_won = False
                player_lost = False
                

    # Move enemies
    if not player_won and not player_lost:
        move_enemies()

    # Check if player won
    if (player_x, player_y) == (36, 13):
        player_won = True

    if seconds_left == 0 and not player_won:
        player_lost = True

    # Check if player lost
    if (player_x, player_y) in enemies:
        player_lost = True

    # Drawing everything on the screen
    screen.fill(WHITE)
    draw_maze()
    draw_enemies()
    draw_player()

    
    screen.blit(game_name,(340, 515))
    screen.blit(interface, (WIDTH - interface.get_width(), 0))
    draw_timer(seconds_left)

   

    if player_won:
        display_win_message()
    elif player_lost:
        display_lose_message()

    
    

    pygame.display.flip()

    # FPS control
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
