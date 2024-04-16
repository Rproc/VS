lista = []
console.log(lista)

lista = ['HTML', 'CSS', 'JS', 'Python']


lista2=[...lista]

lista.forEach(element => {
    console.log(element)
});

for(var i=0; i<lista.length;i++){
    console.log(i + ": " + lista[i])
}

lista.sort()

lista.forEach(element => {
    console.log(element)
});