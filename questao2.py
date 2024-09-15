def fibonacci(numero):
    primeironumero, segundonumero = 0,1
    while primeironumero <= numero:
        if primeironumero == numero:
            return f"{numero} pertence á sequencia de fibonacci"
        primeironumero,segundonumero = segundonumero, primeironumero+segundonumero
    return(f"{numero} nao pertence a sequencia de fibonacci")
numero = int(input("Informe seu numero:"))
print(fibonacci(numero))