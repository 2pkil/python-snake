# Условия движения
if key[pygame.K_w] and (dx, dy) != traffic_dict["S"]:
    dx, dy = traffic_dict["W"]
