# main.py
# game tir
import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загружаем иконку
icon = pygame.image.load("image/images.png")
pygame.display.set_icon(icon)

# Загружаем изображение мишени
original_img = pygame.image.load("image/images.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_img = pygame.transform.scale(original_img, (target_width, target_height))

# Загружаем звук
pygame.mixer.init()
hit_sound = pygame.mixer.Sound("sound/sound_tir.wav")

# Цвет фона
color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

running = True
while running:
        screen.fill(color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()
               if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                   hit_sound.play()  # при попадании
                   target_x = random.randint(0, SCREEN_WIDTH - target_width)
                   target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                   print(f"Попадание! Новые координаты: ({target_x}, {target_y})")
                   score += 1

        screen.blit(target_img, (target_x, target_y))
        score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)


pygame.quit()

