'''
Faça um programa em Python que abra e
reproduza o Áudio de um arquivo MP3.
'''
import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('piano.mp3')
pygame.mixer.music.play(loops=0, start=0.0) # 15.0 inicia aos 15 segundos
input()

pygame.event.wait() # espera toda a música e depois encerra o programa
