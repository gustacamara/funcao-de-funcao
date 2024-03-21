def funçãoDeF(x):
    resultado = (x**2)+1
    return resultado

def funçãoDeG(x):
    resultado = (2*x) - 3
    return resultado

print("g(f(4)) = ",funçãoDeG(funçãoDeF(4)))
