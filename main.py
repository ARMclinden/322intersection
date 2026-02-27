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

class Point():
    x = 0
    y = 0

    def __init__(self, n, m):
        self.x = n
        self.y = m

def find_orientation(x1 : Point, x2 : Point, x3 : Point):
    fin = ((x2.y-x1.y) * (x3.x-x2.x) - (x3.y - x2.y) * (x2.x - x1.x)) 

    if fin == 0:
        return 0
    elif fin > 0:
        return 1
    else:
        return 2