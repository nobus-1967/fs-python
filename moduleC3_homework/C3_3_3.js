// Модуль C3.3
// Задание 3
/* Написать функцию, которая создает пустой объект, но без прототипа. */

// Функция createNoPrototypeObject создает пустой объект
// и передаёт ему null (отсутствие прототипа)
function createObjectWithNoPrototype() {
  return Object.create(null);
}

// Создаём объект emptyObject
const emptyObject = createObjectWithNoPrototype();

// Выводим объект emptyObject
console.log(emptyObject);

// Проверяем наличие прототипа у объекта
console.log(Object.getPrototypeOf(emptyObject));

// Несмотря на нежелательность использования свойство __proto__,
// оно позволит нам удостовериться в отсутствии прототипа у emptyObject
console.log(emptyObject.__proto__);
