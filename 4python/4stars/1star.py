def draw_triangle(lines):
    for i in range(lines): 
        print(i)

def draw_ltriangle(lines):
    n=lines
    for i in range(1,lines+1):
        print('*'*i)

def draw_rtriangle(lines):
    n=lines
    for i in range(1,lines+1):
        print(' '*(n-i) ,end='')
        print('*'*i)
        # print(' '*(n-i) +'*'*i)

draw_ltriangle(5)
draw_rtriangle(5)