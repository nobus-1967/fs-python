// Модуль C3.3
// Задание 1
/* Написать, функцию, которая принимает в качестве аргумента объект и выводит в консоль все ключи и значения только собственных свойств. Данная функция не должна возвращать значение. */

// Создаём прототип объекта catPrototype
const catPrototype = {
  domestic: true,
  meaow: function () {
    console.log(`${this.name} says: 'Meaow!'`);
  },
};

// Фукция createCat по созданию объектов из прототипа
function createCat(name, color) {
  const result = { name, color };
  Object.setPrototypeOf(result, catPrototype);
  return result;
}

// Создаем объект harry
const harry = createCat('Harry Potter', 'grey');

// Проверяяем собственные свойства объекта
console.log(
  `The cat\'s name is ${harry.name} and it\'s color is ${harry.color}.`
);
// Проверяем унаследованные свойство и метод объекта
console.log(`Is the cat domestic? - ${harry.domestic}`)
harry.meaow();

// Функция showObjectKeys выводит все ключи собственных свойств объекта
function showObjectKeys(obj) {
  console.log('Own object properties:');
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      console.log(`Object key: ${key}, value: ${obj[key]}`);
    }
  }
}

// Проверяем функцию showObjectKeys на созданном объекте harry
showObjectKeys(harry);
