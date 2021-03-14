# from enemy import *
#
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode(size=(480, 700))
#
# background = pygame.image.load("./images/background.png")
# plane = pygame.image.load("./images/me1.png")
# plane2 = pygame.image.load("./images/me2.png")
# plane_coordinate = pygame.Rect(189, 500, 102, 126)
#
# screen.blit(background, (0, 0))
# screen.blit(plane, plane_coordinate)
#
# enemy_image = pygame.image.load("./images/enemy1.png")
# enemy = Enemy(enemy_image)
# enemy_Group = pygame.sprite.Group(enemy)
#
#
# while True:
#     clock.tick(60)
#     plane_coordinate.y -= 1
#
#     screen.blit(background, (0, 0))
#     enemy_Group.update()
#     enemy_Group.draw(screen)
#
#     if plane_coordinate.y <= 0:
#         plane_coordinate.y = 0
#     elif plane_coordinate.y >= 574:
#         plane_coordinate.y = 574
#
#     screen.blit(plane, plane_coordinate)
#     pygame.display.update()
#
#     event = pygame.event.poll()
#
#     if event.type == pygame.QUIT:
#         pygame.quit()
#         exit()
#
