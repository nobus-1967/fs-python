// Модуль C3.3
// Задание 2
/* Написать функцию, которая принимает в качестве аргументов строку и объект, а затем проверяет есть ли у переданного объекта свойство с данным именем. Функция должна возвращать true или false. */

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
console.log(`Is the cat domestic? - ${harry.domestic}`);
harry.meaow();

// Функция checkObjectKeys проверяет наличие у объекта данного свойства
const checkObjectKeys = (obj, key) => key in obj;

// Проверяем функцию checkObjectKeys на созданном объекте harry
console.log(checkObjectKeys(harry, 'color'));
console.log(checkObjectKeys(harry, 'domestic'));
console.log(checkObjectKeys(harry, 'age'));
