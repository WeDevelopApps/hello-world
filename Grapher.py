from tkinter import *
import math
sin = math.sin
cos = math.cos
tan = math.tan






x = None



def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


def graph(raw_expression, xmin, xmax, ymin, ymax):
    raw_expression = raw_expression.replace('^', '**')
    raw_expression = raw_expression.replace('(', '*')
    raw_expression = raw_expression.replace(')', '')
    originx = abs(xmin * 100)
    originy = abs(ymax * 100)

    tk = Tk()
    tk.title("Grapher")

    canvas = Canvas(tk, width=(originx + (xmax * 100)), height=(originy + abs(ymin * 100)))
    canvas.pack()

    canvas.create_line(originx, 0, originx, (originy + abs(ymin * 100)), width=2)

    canvas.create_line(0, originy, (originx + (xmax * 100)), originy, width=2)

    for i in frange(100, (originx + (xmax * 100)), 100):
        canvas.create_line(i, 0, i, (originx + (xmax * 100)), fill='gray')

    for j in frange(100, (originy + abs(ymin * 100)), 100):
        canvas.create_line(0, j, (originy + abs(ymin * 100)), j, fill='gray')

    for k in frange((xmin * 100), (xmax * 100), .01):
        x = (k / 100)
        y = eval(raw_expression)

        canvas.create_rectangle(((k) + originx), (originy - (100 * y)), ((k) + originx), (originy - (100 * y)))
    tk.update_idletasks()
    tk.update()
    tk.mainloop()

def solve(f, d, i):
    import math
    import operator
    import functools
    f = f.replace('x', 'L[n]')
    f = f.replace('^', '**')
    f = f.replace('(', '*')
    f = f.replace(')', '')
    L = list(range(d))
    M = list(range(d))
    N = list(range(d))
    n = 0
    while (n < (d)):
        L[n] = (0.4+.0909*((-1)**.5))**n
        M[n] = "L[n] - (0.4 + .9*((-1)**.5))" + "**" + str(n)
        n = n + 1
    p = 0
    while (p < i):
        n = 0
        while(n < (d)):
            M[n] = 1
            o = 0
            while(o < d):
                M[o] = eval(str(M[o]))
                o = o + 1
            N = functools.reduce(lambda x, y: x*y, M)
            L[n] = L[n] - (eval(f)/N)
            M[n] = "L[n] - " + str(L[n])
            n = n + 1
        p = p + 1
    n = 0
    while (n < d):
        print("x" + str(n+1) + " = " + str(L[n]))
        n = n + 1
        


##raw_expression = input('''Type in the function to be graphed. If there are exponents in the equation, use ** in place of the exponent.
##For example: y = ....
##>>> ''')
##
##xmin = float(input('''Type in the minimum x value.
##>>> '''))
##
##xmax = float(input('''Type in the maximum x value.
##>>> '''))
##
##ymin = float(input('''Type in the minimum y value.
##>>> '''))
##
##ymax = float(input('''Type in the maximum y value.
##>>> '''))
##
##graph(xmin, xmax)

