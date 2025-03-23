import pygame
import sys
import random
pygame.init()
screen=pygame.display.set_mode((722,409))
pygame.display.set_caption('ayapus')
running=True
icon=pygame.image.load('images/icon.png.png')
pygame.display.set_icon(icon)
bg=pygame.image.load('images/bg.png')
bgx=0
sound=pygame.mixer.Sound('audios/Smash_Mouth_-_All_Star_48020579.mp3')
sound.play()
a=pygame.time.Clock()
a.tick(60)
while running:
    screen.blit(bg,(bgx,0))
    screen.blit(bg, (bgx+722, 0))
    bgx-=2
    if bgx==-722:
        bgx=0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()