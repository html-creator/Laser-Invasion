#import evrything
import pygame
import pygame.mixer
import time
from random import randrange
from tkinter import *
import os
os.system('cls')
print("Laser Invasion by carrot studio")

# among us
def create_window():
    window = Tk()
    img = PhotoImage(file='among_us.png')
    Label(
    window,
    image=img
    ).pack()
    window.configure(bg="olive")
    window.title("among us")
    window.image_types
    window.geometry("1000x1000+100+100")
    window.mainloop()
szansa_na_amonga = randrange(900000, 1000000)
# Initialize Pygame
pygame.init()
pygame.mixer.init()

#font
font = pygame.font.Font(None, 36)

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Laser Invasion")
pygame_icon = pygame.image.load('player.png')
pygame.display.set_icon(pygame_icon)

#set up the sounds
laser_sound = pygame.mixer.Sound('laser_shot.wav')
win_sound = pygame.mixer.Sound('win.wav')
hit_sound = pygame.mixer.Sound('hit.wav')
dead = pygame.mixer.Sound('lose.wav')
pygame.mixer.music.load('muzyka.mp3')
pygame.mixer.music.set_volume(1)
hit_sound.set_volume(2)
win_sound.set_volume(2)
laser_sound.set_volume(0.5)
pygame.mixer.music.play(-1)

#bg
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))

# Set up the player
player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 2
player_y = 506
player_speed = 5
image = pygame.image.load("player.png")
pr = image.get_rect()

#set up ground
ground_x = 0
ground_y = screen_height - 50
ground = pygame.image.load("ground.png")

# Set up the laser
laser_width = 5
laser_height = 20
laser_speed = 10
laser_color = (255, 0, 0)
lasers = []

#set up kamień
rand1 = randrange(0, screen_width - randrange(70, 90))
rand2 = randrange(100, screen_height - 300)
kamień = pygame.image.load("kamień.png") 
wh = randrange(30, 45)
kamień = pygame.transform.scale(kamień, (wh, wh))
hitbox_kamieńa = kamień.get_rect()
hitbox_kamieńa.x = rand1
hitbox_kamieńa.y = rand2
def narysuj_kamień(x, y):
    screen.blit(kamień, (x, y))

# Set up the enemy laser
enemy_lasers = []

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = (screen_width - enemy_width) / 2
enemy_y = 35
enemy_speed = 5
eimg = pygame.image.load("enemy.png")
rect = eimg.get_rect()
hp_set = 1#randrange(10, 30)
enemy_hp = hp_set
def napisz(napis, x, y, color):
    text = font.render(napis, True, color)
    screen.blit(text, (x, y))

# Set up the game loop
running = True
while running:
    # Handle events
    rect.x = enemy_x
    rect.y = enemy_y
    pr.x = player_x
    pr.y = player_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if randrange(1, 10) != 1:
                    laser_x = player_x + player_width / 2 - laser_width / 2
                    laser_y = player_y - laser_height
                    laser = pygame.Rect(laser_x, laser_y, laser_width, laser_height)
                    lasers.append(laser)
                    laser_sound.play()
    if randrange(1, 25) == 1:
        laser_x = enemy_x + enemy_width / 2 - laser_width / 2
        laser_y = enemy_y - laser_height
        laser = pygame.Rect(laser_x, laser_y, laser_width, laser_height)
        enemy_lasers.append(laser)
        laser_sound.play()
    elif  enemy_x == player_y:
        laser_x = enemy_x + enemy_width / 2 - laser_width / 2
        laser_y = enemy_y - laser_height
        laser = pygame.Rect(laser_x, laser_y, laser_width, laser_height)
        enemy_lasers.append(laser)
        laser_sound.play()
    if randrange(1, szansa_na_amonga) == 1:
        print("among us")
        running = False        
        create_window()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the lasers and chek for colisions
    for laser in lasers:
        laser.y -= laser_speed
        if rect.colliderect(laser):
            enemy_hp -= 1
            enemy_speed *= 1.000002341
            lasers.remove(laser)
            if enemy_hp == 0:
                win_sound.play()
                screen.fill((0,0,0))
                napisz("BRAWO! wygrałeś", 300, 300, (255,255,255))
                pygame.display.flip()
                time.sleep(3.5)
                running = False
            else:
                hit_sound.play()
        if laser.y < 0:
            lasers.remove(laser)
        if hitbox_kamieńa.colliderect(laser):
            lasers.remove(laser)
    for laser in enemy_lasers:
        laser.y += laser_speed
        if pr.colliderect(laser):
            dead.play()
            screen.fill((0,0,0))
            napisz("o nie! przegrałeś", 300, 300, (255,255,255))
            pygame.display.flip()
            enemy_lasers.remove(laser)
            time.sleep(3.5)
            enemy_hp = hp_set
        if laser.y > 600:
            enemy_lasers.remove(laser)
        if hitbox_kamieńa.colliderect(laser):
            enemy_lasers.remove(laser)


    # Move the enemy
    enemy_x += enemy_speed
    if enemy_x < 0 or enemy_x > screen_width - enemy_width:
        enemy_speed *= -1


    # Draw the screen
    screen.blit(background, (0, 0))
    screen.blit(image, (player_x, player_y))#player
    for laser in enemy_lasers:
        pygame.draw.rect(screen, laser_color, laser)#lasers
    for laser in lasers:
        pygame.draw.rect(screen, laser_color, laser)#lasers
    screen.blit(eimg, rect)#enemy
    screen.blit(ground, (ground_x , ground_y))#ground
    enemy_speed += 0.0000000000000001
    napisz("enemy has " + str(enemy_hp) + "hp", 0, 0, (0,0,0))
    narysuj_kamień(rand1, rand2)#kamie
    pygame.display.flip()

pygame.quit()
 
