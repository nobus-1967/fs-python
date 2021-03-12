// Модуль C3.2
// Задание
/* 1. Создайте пустой объект; 
   2. Добавьте несколько свойств со значениями разных типов;
   3. Добавьте метод;
   4. Удалите одно из созданных свойств. */

const cat = new Object();

cat.name = 'Harry Potter';
cat.color = 'grey';
cat.meaow = function() {
  console.log(`${this.name} says: 'Meaow!'`)
}

console.log(`The cat\'s name is ${cat.name} and it\'s color is ${cat.color}.`);
cat.meaow();

cat.age = 10;
console.log(`The cat is ${cat.age} years old.`);

delete cat.age;
console.log(`The cat is ${cat.age} years old.`);
