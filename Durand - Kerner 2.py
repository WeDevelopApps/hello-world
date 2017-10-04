import copy

n = 0
i = (-1)**.5
f = input("Function?")
x = 0
d = int(input("Highest Degree?"))
iterations = int(input("Number of iterations?"))
P = list(range(d))
R = list(range(d))
L = copy.copy(P)
for n in P:
    
    L[n] = (x - (0.4 + 0.9*i) ** n)
    #print(str(L[n]))
    P[n] = ('x - ' + str(eval('(0.4 + .9*i) ** n')))
##    print(len(P))
##    print(P)
##    print(n)



n1 = 0
#print(n)
while (n1 < iterations):
    n = 0
    while (n < (len(P))):
        #print(x)
        x = L[n]
        U = copy.copy(P)
        
        #print(P)
        del U[n]
        
        #print(U)
        Q = str(U)
        #print(U)
        Q = Q.replace('[', '(')
        #print(U)
        Q = Q.replace(']', ')')
        #print(U)
        Q = Q.replace(', ', '*')
        #print(U)
        #print(n)
        #print(str(P[n]))
        U = eval(Q)
        #print(U)

        R[n] = x - ((eval(f))/eval(U))
        #print(R[n])
        L[n] = R[n]
        P[n] = ('x - ' + str(L[n]))
        
        n = n + 1
    n1 = n1 + 1

for n in range(0, (len(P))):
    #print(n)
    print("x" + str(n) + " = " + str(R[n]))
