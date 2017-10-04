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
            print(N)
            L[n] = L[n] - (eval(f)/N)
            M[n] = "L[n] - " + str(L[n])
            n = n + 1
        p = p + 1
    n = 0
    while (n < d):
        print("x" + str(n+1) + " = " + str(L[n]))
        n = n + 1
def mean(s):
    s = s.replace(",", "")
    s = s.replace(" ", "")
    d = list(range(len(s)))
    n = 0
    while (n < (len(s))):
        d[n] = int(s[n])
        n = n + 1

    s = (sum(d)/len(s))
    print('The mean of the data set is ' + str(s))
def median(s):
    s = s.replace(",", "")
    s = s.replace(" ", "")
    d = list(range(len(s)))
    n = 0
    while (n < (len(s))):
        d[n] = int(s[n])
        n = n + 1
    d = sorted(d)
    if (((-1)**len(s)) == 1):
        s = (d[int((len(s)/2))] + d[int((len(s)-2)-1)])/2
    else:
        s = d[int(((len(s) + 1)/2) - 1)]
    print('The median of the data set is ' + str(s))
def mode(s):
    s = s.replace(",", "")
    s = s.replace(" ", "")
    d = list(range(len(s)))
    d2 = list(range(len(s)))
    print(d2)
    n = 0
    while (n < (len(s))):
        d[n] = int(s[n])
        n = n + 1
    d = sorted(d)
    a = 0
    b = 0
    while (n < len(s)):
        for d[a] in d:
            b = b + 1
            d2[a] = b
            a = a + 1
            print(b)
            print(a)
            print(d2)
        b = 0
        n = n + 1
    print("The mode of the data set is " + str(d2[len(d2)-1]))
def integrate(f, a, b, d):
    import math
    import operator
    import functools
    f1 = f
    f = f.replace('^', '**')
    f = f.replace('(', '*')
    f = f.replace(')', '')
    i = a
    fint = 0
    while (i <= ((a*(d-1)+b)/d)):
        x = a + (i-a)*d
        base1 = eval(f)
        x = a + ((i-a)+1)*d
        base2 = eval(f)
        fint = fint + base1 + base2
        i = i + 1
    fint = .5*d*fint
    print("The integral of " + str(f1) + " from " + str(a) + " to " + str(b) + " is " + str(fint) + ".")
def differentiate(f, a, d, n):
    import math
    import operator
    import functools
    f1 = f
    f = f.replace('^', '**')
    f = f.replace('(', '*')
    f = f.replace(')', '')
    print(f)
    x = a + d
    print(x)
    y2 = eval(f)
    print(y2)
    x = a
    print(x)
    y1 = eval(f)
    print(y1)
    fderiv = (y2 - y1)/(d**n)
    print("The " + str(n) + "th derivative of " + str(f1) + " at " + str(a) + " is " + str(fderiv) + ".")

    
from tkinter import *


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num == True:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.' and '.' in temp:
                    return
            self.current = temp + temp2
            while len(self.current) > 1 and self.current[0] == '0' and self.current[1] != '.':
                self.current = self.current[1:]
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "minus":
            self.total -= self.current
        elif self.op == "times":
            self.total *= self.current
        elif self.op == "divide" and self.current:
            self.total /= self.current
        else:
            self.total = 0
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        elif self.eq == False:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        if self.new_num == False:
            self.current = "0"
            self.display(0)
            self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.new_num = False
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)


class My_Btn(Button):
    def btn_cmd(self, num):
        self["command"] = lambda: sum1.num_press(num)


sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")


numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(My_Btn(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, pady = 5)
        bttn[i].btn_cmd(numbers[i])
        i += 1
bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1, pady = 5)

bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3, pady = 5)

bttn_mult = Button(calc, text = "x")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3, pady = 5)

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, pady = 5)

point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, pady = 5)

add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, pady = 5)

neg= Button(calc, text = "+/-")
neg["command"] = sum1.sign
neg.grid(row = 5, column = 0, pady = 5)

clear = Button(calc, text = "C")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, pady = 5)

all_clear = Button(calc, text = "AC")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 5, column = 2, pady = 5)

equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = 5)

root.mainloop()


