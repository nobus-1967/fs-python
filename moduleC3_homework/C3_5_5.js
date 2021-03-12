// Модуль C3.5
// Задание 5
/* Переписать задание 4 (модуль С3.4) с использованием классов. */

// Class ElectricDevice для электрического прибора
// (с включенными свойствами и методами)
class ElectricDevice {
  constructor(power) {
    this.power = power;
    this.plugIn = false;
  }
  connect() {
    this.plugIn = true;
    console.log('The device is on!');
  }
  disconnect() {
    this.plugIn = false;
    console.log('The device is off!');
  }
}

// Класс Laptop (на базе класса ElectricDevice)
class Laptop extends ElectricDevice {
  constructor(power, model) {
    super(power);
    this.model = model;
    this.WiFi = false;
  }
  WiFiOn() {
    this.WiFi = true;
    console.log('WiFi is turned on!');
  }
  WiFiOff() {
    this.WiFi = false;
    console.log('WiFi is turned off!');
  }
}

// Класс Lamp (на базе класса ElectricDevice)
class Lamp extends ElectricDevice {
  constructor(power, color) {
    super(power);
    this.color = color;
  }
}

// Создаём экземпляры ноутбука и лампы
const acer = new Laptop(115, 'acer ASPIRE');
const tableLamp = new Lamp(60, 'cold white');

// Выводим информацию об электрических приборах
console.group('LAPTOP');
console.log(`My laptop model is ${acer.model}`);
acer.connect();
console.log(`My laptop power is ${acer.power} W`);
acer.WiFiOn();
console.groupEnd();

console.group('LAMP');
console.log(`My lamp color is ${tableLamp.color}`);
tableLamp.connect();
console.log(`My lamp power is ${tableLamp.power} W`);
console.groupEnd();

// Подсчитываем суммарную мощность потребляемой приборами электроэнергии
let powerSum = acer.power + tableLamp.power;
console.log(`The total power is ${powerSum} W`);

// Проверим, потомками какого класса являются объекты acer и tableLamp
console.log(acer instanceof ElectricDevice);
console.log(acer instanceof Laptop);
console.log(acer instanceof Lamp);
console.log(tableLamp instanceof ElectricDevice);
console.log(tableLamp instanceof Lamp);
console.log(tableLamp instanceof Laptop);

