from util import *

# Plant pumpkins in an n*n area starting from (x, y)
def big(x, y, n):
    # Traverse to plant pumpkins
    move_to(x, y)
    for i in range(n):
        for j in range(n):
            move_to(x + j, y + i)
            if get_ground_type() != 'Soil':
                till()
            water()
            plant('Pumpkin')
    # Traverse to check and replant bad pumpkins
    move_to(x, y)
    bad_pumpkins = []
    for i in range(n):
        for j in range(n):
            move_to(x + j, y + i)
            if get_entity_type() == 'Bad Pumpkin':
                bad_pumpkins.append((x + j, y + i))
    while len(bad_pumpkins) > 0:
        pos = bad_pumpkins[0]
        move_to(pos[0], pos[1])
        if get_entity_type() == 'Bad Pumpkin':
            plant('Pumpkin')
        else:
            bad_pumpkins.remove(pos)
    # Final harvest
    move_to(x, y)
    harvest()