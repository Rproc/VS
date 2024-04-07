// const readline = require('readline').createInterface({
//     input: process.stdin,
//     output: process.stdout
//   })
  
// readline.question(`What is your name? `, name => {
//     console.log(`Hello ${name}!`)
//     readline.close()
// })

const readline = require('readline');

// Create an interface for reading input from 'stdin'
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter your age: ', (age) => {
    if (isNaN(age)) {
      console.log('Invalid input. Please enter a valid number for your age.');
    } else {
      console.log(`You entered: ${age}`);
    }
    rl.close();
  });
  