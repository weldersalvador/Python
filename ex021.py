import pygame

pygame.init()
pygame.mixer.music.load('image.mp3')
pygame.mixer.music.play()
pygame.event.wait()
