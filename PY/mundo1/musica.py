import pygame
# Usamos essa biblioteca também para imagens e jogos

pygame.init()  # Inicia
pygame.mixer.music.load('tocar.mp3')  # Escolhendo o arquivo
pygame.mixer.music.play()  # Começar a tocar
pygame.event.wait()  # Espera o evento acabar para encerrar o prog



