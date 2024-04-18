
let matrix = [[1, 2], [3, 4]]


let clientes = [['Marcos', '99999-9999'], ['Caroline', '88888-8888']]


// Imprimindo apenas um dos clientes
console.log(clientes[0])

// Imprimindo apenas o telefone do cliente Marcos
console.log(clientes[0][1])

// Imprimindo de forma bonita todos os clientes
console.table(clientes)

// Adiciona
clientes.splice(1, 0, ['Lennon', '77777-7777'])

console.table(clientes)


