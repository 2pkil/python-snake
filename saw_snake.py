# Отрисовка змейки
for i, j in body_snake:
    pygame.draw.rect(screen, pygame.Color('green'), (i, j, OBJECT_SIZE, OBJECT_SIZE))
