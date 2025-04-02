import pygame
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((300,300))
playlist = ["music/Dana_Glover_-_It_Is_You_I_Have_Loved_54898325.mp3",
            "music/Smash_Mouth_-_All_Star_48020579.mp3",
            "music/The_Weeknd_Playboi_Carti_-_Timeless_78596950.mp3"]
current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()

pygame.quit()
