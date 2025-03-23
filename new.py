import pygame

pygame.init()
screen=pygame.display.set_mode((600,300))
running=True
icon=pygame.image.load('images/icon.png.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('asusu')
square=pygame.Surface((50,50))
square.fill('White')
text = pygame.font.Font('fonts/Roboto_Condensed-Bold.ttf', 30)
text_surface=text.render('ayazhan is whe', False, 'Red')
player=pygame.image.load('images/icon.png.png')
while running:
    screen.blit(square, (275,125))
    pygame.draw.circle(screen,"Red", (50,50),5)
    screen.blit(text_surface, (285,20))
    pygame.display.update()
    screen.blit(player, (5,5))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()