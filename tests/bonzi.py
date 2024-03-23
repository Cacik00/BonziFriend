import pygame
import sys

# Pygame'ı başlat
pygame.init()

# Pencere boyutu ve başlık
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basit Pencere")

# Ana oyun döngüsü
running = True
while running:
    # Kullanıcının pencereyi kapatabilmesi için kontrol
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Ekranı temizle ve yeniden çiz
    window.fill((255, 255, 255))  # Beyaz arka plan
    # Buraya çizim veya diğer işlemler eklenebilir
    
    # Pencereyi güncelle
    pygame.display.update()

# Pygame'i kapat
pygame.quit()
sys.exit()
