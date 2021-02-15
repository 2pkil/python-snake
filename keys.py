    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs ['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs ['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs ['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs ['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
