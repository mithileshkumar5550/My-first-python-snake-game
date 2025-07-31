# import pygame
# import random

# # Initialize pygame
# pygame.init()

# pygame.mixer.init()

# # Load and play background music
# pygame.mixer.music.load("song.mp3")  # Replace with your music file name
# pygame.mixer.music.play(-1)  # Loop the music indefinitely
# pygame.mixer.music.set_volume(0.5)  # Set volume (optional)

# # Colours
# white = (255, 255, 255)
# red = (255, 0, 0)
# blue = (0, 0, 255)
# green = (0, 255, 0)
# orange = (255, 165, 0)
# yellow = (255, 255, 0)
# sky_blue=(13, 32, 33, 1)
# black=(0,0,0)
# Gold=(255, 215, 0)



# # Screen dimensions
# screen_width = 1000
# screen_height = 600
# gamescreen = pygame.display.set_mode((screen_width, screen_height))

# # Game title
# pygame.display.set_caption("Hunter Snake")
# pygame.display.update()

# # Initialize font
# font = pygame.font.SysFont(None, 55)

# # Function to display text on screen
# def text_screen(text, color, x, y):
#     screen_text = font.render(text, True, color)
#     gamescreen.blit(screen_text, [x, y])

# # Function to draw the snake
# def plot_snake(gamescreen, snake_list, snake_size, head_color, body_color):
#     for i, segment in enumerate(snake_list):
#         color = head_color if i == 0 else body_color
#         pygame.draw.rect(gamescreen, color, (segment[0], segment[1], snake_size, snake_size))

# # Main game loop
# def gameloop():
#     # Game Variables
#     exit_game = False
#     game_over = False
#     snake_x = 60
#     snake_y = 50
#     snake_size = 20
#     fps = 30
#     velocity_x = 0
#     velocity_y = 0
#     food_x = random.randint(20, screen_width - 20)
#     food_y = random.randint(20, screen_height - 20)
#     score = 0
#     snake_list = []
#     snake_length = 1

#     # Read the high score from the file
#     try:
#         with open("highscore.txt", "r") as f:
#             highscore = int(f.read())
#     except (FileNotFoundError, ValueError):
#         highscore = 0

#     # Game settings
#     init_velocity = 8
#     clock = pygame.time.Clock()

#     # Snake colors
#     head_color = black
#     body_color = Gold

#     while not exit_game:
#         if game_over:
#             # Save the high score when the game is over
#             with open("highscore.txt", "w") as f:
#                 f.write(str(highscore))
            
#             gamescreen.fill(yellow)
#             text_screen("BDSK,RESTART KARO DOBARA", red, 200, 250)
#             text_screen(f"Your Score: {score}", blue, 350, 300)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit_game = True
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RETURN:
#                         gameloop()  # Restart the game
#         else:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit_game = True
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RIGHT and velocity_x == 0:
#                         velocity_x = init_velocity
#                         velocity_y = 0
#                     if event.key == pygame.K_LEFT and velocity_x == 0:
#                         velocity_x = -init_velocity
#                         velocity_y = 0
#                     if event.key == pygame.K_UP and velocity_y == 0:
#                         velocity_y = -init_velocity
#                         velocity_x = 0
#                     if event.key == pygame.K_DOWN and velocity_y == 0:
#                         velocity_y = init_velocity
#                         velocity_x = 0

#             # Update snake position
#             snake_x += velocity_x
#             snake_y += velocity_y

#             # Detect collision with food
#             if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
#                 score += 50
#                 food_x = random.randint(20, screen_width - 20)
#                 food_y = random.randint(20, screen_height - 20)
#                 snake_length += 5
#                 if score > highscore:
#                     highscore = score

#             # Fill background
#             gamescreen.fill(green)
#             text_screen(f"Score: {score}  Highscore: {highscore}", blue, 5, 5)

#             # Snake head and body tracking
#             head = [snake_x, snake_y]
#             snake_list.append(head)

#             if len(snake_list) > snake_length:
#                 del snake_list[0]

#             # Check collision with itself
#             if head in snake_list[:-1]:
#                 game_over = True

#             # Check collision with walls
#             if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
#                 game_over = True

#             # Draw food
#             pygame.draw.rect(gamescreen, red, [food_x, food_y, snake_size, snake_size])

#             # Draw snake
#             plot_snake(gamescreen, snake_list, snake_size, head_color, body_color)

#         pygame.display.update()
#         clock.tick(fps)

#     pygame.quit()
#     quit()

# # Start the game
# gameloop()
