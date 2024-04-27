# Sequencia em iteratividade

def fibonnaci(n):
    
    fib = [0,1]
    
    for i in range(2, n+1):
        nextfib= fib[-1] + fib[-2]
        fib.append(nextfib)
        soma = sum(fib)
        
    print(soma)
    return fib[:n+1]
    
        
# Mostrando a soma dos valores correspondente ao número solicitado, e uma lista com a sequencia.
# print(fibonnaci(10))

# Modo recursivo
