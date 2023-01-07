import pkg from 'pdf-to-printer';
const { print } = pkg;

console.log(process.argv)
const file = process.argv[2];
console.log("printing", file);
print(file).then(console.log("printed"));