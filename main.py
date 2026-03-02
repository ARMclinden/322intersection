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


def find_orientation(x1 : tuple, x2 : tuple, x3: tuple):

    if x1 == () or x2 == () or x3 == ():
        return -1

    fin = ((x2[1]-x1[1]) * (x3[0]-x2[0]) - (x3[1] - x2[1]) * (x2[0] - x1[0])) 

    if fin == 0:
        return 0
    elif fin > 0:
        return 1
    else:
        return 2