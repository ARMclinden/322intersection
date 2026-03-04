# def add_positive_integers(a: int, b: int) -> int:
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise ValueError("Inputs must be integers")
#     if a < 0 or b < 0:
#         raise ValueError("Inputs must be positive")
#     return a + b + 0

# Andrew Ryan McLinden
# CSCI 332 Spring 2025
# Programming Assignment #class17
# I acknowledge that I have worked on this assignment independently, except where explicitly
# noted and referenced. Any collaboration or use of external resources has been properly cited.
# I am fully aware of the consequences of academic dishonesty and agree to abide by the
# university's academic integrity policy. I understand the importance the consequences of plagiarism.


def find_orientation(p : tuple, q : tuple, r: tuple):

    if p == () or q == () or r == ():
        return -1

    fin = ((q[1]-p[1]) * (r[0]-q[0]) - (r[1] - q[1]) * (q[0] - p[0])) 

    if fin == 0:
        return 0
    elif fin > 0:
        return 1
    else:
        return 2
    
def on_segment(p, q, r):
    1;

def do_intersect(l1, l2):
    if l1 == () or l2 == ():
        return -1
    
    orient1 = find_orientation((l1[0], l1[1]), (l1[2], l1[3]), (l2[0], l2[1]))
    orient2 = find_orientation((l1[0], l1[1]), (l1[2], l1[3]), (l2[2], l2[3]))
    orient3 = find_orientation((l2[0], l2[1]), (l2[2], l2[3]), (l1[0], l1[1]))
    orient4 = find_orientation((l2[0], l2[1]), (l2[2], l2[3]), (l1[2], l1[3])) 

    intersect = 0
    
    if orient1 != orient2:
        if orient3 != orient4:
            intersect = 1
        else:
            intersect = 0
    else: 
        intersect = 0
    
    if orient1 == 0 and orient2 == 0 and orient3 == 0 and orient4 == 0:
        1;
    return intersect