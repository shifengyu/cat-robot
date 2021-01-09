import pygame
pygame.mixer.init()
def play(a,b):
    if b == 'play':
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
    if b == 'stop':
        pygame.mixer.music.stop()
