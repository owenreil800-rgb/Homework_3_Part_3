import math

X_1 = 1
X_2 = 12
Y_1 = 7
Y_2 = 25

def func_Hav_Dist(X_1, X_2, Y_1, Y_2):
    a = (math.sin((X_2-X_1)/2))**2
    b = (math.cos((Y_2-Y_1)/2))**2
    c = (math.cos((X_1+X_2)/2))**2
    d = (math.sin((Y_2-Y_1)/2))**2
    hav = a * b * c * d
    theta = 2 * (math.sin(math.sqrt(hav)))**(-1)
    return theta

def func_Man_Dist(X_1, X_2, Y_1, Y_2):
    a = math.fabs(X_2 - X_1)
    b = math.fabs(Y_2 - Y_1)
    return a + b

Difference = math.fabs(func_Hav_Dist(X_1, X_2, Y_1, Y_2) - func_Man_Dist(X_1, X_2, Y_1, Y_2))

print(Difference)