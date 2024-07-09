#Python function that prints out the first n rows of the pascal's triangle.


def pascal_triangle(n):
    trow=[1]
    y=[0]
    for x in range(max(n,0)):
        print(trow)
        trow = [1 + r for l,r in zip(trow+y,y+trow)]
    return n >= 1
pascal_triangle(6)