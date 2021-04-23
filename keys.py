# Условия движения
if key[pygame.K_w] and (dx, dy) != traffic_dict["S"]:
    dx, dy = traffic_dict["W"]
if key[pygame.K_s] and (dx, dy) != traffic_dict["W"]:
    dx, dy = traffic_dict["S"]
if key[pygame.K_a] and (dx, dy) != traffic_dict["D"]:
    dx, dy = traffic_dict["A"]
if key[pygame.K_d] and (dx, dy) != traffic_dict["A"]:
    dx, dy = traffic_dict["D"]
