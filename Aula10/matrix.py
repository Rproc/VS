matrix = [[1, 2], [3, 4]]

clientes = [['Marcos', '99999-9999'], ['Caroline', '88888-8888']]

# Imprimindo apenas um dos clientes
# print(clientes[0])

# Imprimindo apenas o telefone do cliente Marcos
# print(clientes[0][1])

# Adiciona
clientes.append(['Lennon', '77777-7777'])

# print(clientes)

# remover
clientes.pop(2)
# print(clientes)

# iterando
for cliente in clientes:
    print(cliente)


for i in range(len(clientes)):
    for j in range(len(clientes[i])):
        print(clientes[i][j])