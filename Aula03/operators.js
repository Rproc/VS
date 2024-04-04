let x = 7; 

let y = 5

console.log(x+y)
console.log(x-y)
console.log(x*y)
console.log(x/y)
console.log(x**y)
console.log(x%y)






//Incremento
++x
console.log(x)
x++
console.log(x)




// // postfix
// let i = 3;
// const j = i++;

// console.log({ i, j });

// // prefix
// let i = 3;
// const j = ++i;

// console.log({ i, j }); 

i = 10;   // (1)
j = ++i;  // (2)
k = i++;  // (3)

//i é definido como 10 (fácil).
// Duas coisas nessa linha:
// i é incrementado para 11.
// O novo valor de i é copiado para j. Portanto, j agora é igual a 11.
// Também há duas coisas nessa linha:
// i é incrementado para 12.
// O valor original de i (que é 11) é copiado em k. Portanto, k agora é igual a 11.
// Portanto, depois de executar o código, i será 12, mas j e k serão 11.


//unário
const str = "10"; 
let str_to_num; 
str_to_num = +str; 
console.log(str_to_num); 
console.log(typeof str_to_num);

//negação
neg = -str_to_num
console.log(neg); 
