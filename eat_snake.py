    if snake[-1] == apple:
        apple = randrange(0, WIN, SIZE), randrange(0, WIN, SIZE)
        length = length + 1
        fps = fps + 1