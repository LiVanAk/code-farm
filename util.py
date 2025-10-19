from init import *

def move_to(x, y):
    if abs(x - get_pos_x) < get_world_size() - abs(x - get_pos_x):
        if get_pos_x() < x:
            while get_pos_x() != x:
                move('East')
        elif get_pos_x() > x:
            while get_pos_x() != x:
                move('West')
    else:
        if get_pos_x() < x:
            while get_pos_x() != x:
                move('West')
        elif get_pos_x() > x:
            while get_pos_x() != x:
                move('East')

    if abs(y - get_pos_y) < get_world_size() - abs(y - get_pos_y):
        if get_pos_y() < y:
            while get_pos_y() != y:
                move('North')
        elif get_pos_y() > y:
            while get_pos_y() != y:
                move('South')
    else:
        if get_pos_y() < y:
            while get_pos_y() != y:
                move('South')
        elif get_pos_y() > y:
            while get_pos_y() != y:
                move('North')

def water():
    pass
