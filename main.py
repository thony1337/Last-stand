import pygame
print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))

while True :
  # check for all event
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          quit()