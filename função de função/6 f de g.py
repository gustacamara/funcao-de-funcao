def funçãoDeF(x):
    resultado = (x**2)+1
    return resultado

def funçãoDeG(x):
    resultado = (2*x) - 3
    return resultado

print("f(g(4)) = ",funçãoDeF(funçãoDeG(4)))
