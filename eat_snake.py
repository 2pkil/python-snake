# Поедание яблока
if body_snake[-1] == apple:
    apple = randrange(0, WINDOW_WIDTH, OBJECT_SIZE), randrange(0, WINDOW_HEIGHT, OBJECT_SIZE)
    length_snake += 1
    fps += 1
