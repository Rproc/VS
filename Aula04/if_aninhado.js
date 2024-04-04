let estado = '?'
let contaCorrente = 1000
let dia = 'sabado'

if (contaCorrente > 500){
    if (dia == 'sexta')
    estado = 'feliz'
    else
    estado = 'triste'
} 
else{
    estado = 'triste'
}

console.log(estado)