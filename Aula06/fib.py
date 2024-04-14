def fibonacci(n):
    fib_anterior = 0
    fib_atual = 1
    print(fib_anterior)
    print(fib_atual)
    while True:
        prox_fib = fib_anterior + fib_atual  # Calcula o próximo número da sequência
        if prox_fib > n:
            break  # Se o próximo número ultrapassar o limite, sai do loop
        print(prox_fib)
        fib_anterior = fib_atual
        fib_atual=prox_fib

numero_limite = 2000  # Defina o número máximo até o qual deseja gerar a sequência
fibonacci(numero_limite)
