import random

word_size = random.randint(1, 16)  # Simulate world size between 1 and 16
pos_x, pos_y = random.randint(0, word_size - 1), random.randint(0, word_size - 1)

def get_world_size():
    return word_size

def get_pos_x():
    return pos_x

def get_pos_y():
    return pos_y

def move(direction):
    global pos_x, pos_y
    if direction == 'North' and pos_y > 0:
        pos_y -= 1
    elif direction == 'South' and pos_y < word_size - 1:
        pos_y += 1
    elif direction == 'West' and pos_x > 0:
        pos_x -= 1
    elif direction == 'East' and pos_x < word_size - 1:
        pos_x += 1

def plant(EntityType):
    pass

def get_ground_type():
    return random.choice(['Soil', 'Grass'])

def get_entity_type():
    return random.choice(['Healthy Pumpkin', 'Bad Pumpkin'])

def till():
    pass

def harvest():
    pass