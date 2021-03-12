// Модуль C3.4
// Задание 4
/* Определить иерархию электроприборов. Включить некоторые в розетку. Посчитать потребляемую мощность. 
Таких приборов должно быть, как минимум, два (например, настольная лампа и компьютер). */

// Функция ElectricDevice - прототип электрического прибора
function ElectricDevice(power) {
  this.power = power;
  this.plugIn = false;
}

// Метод connect для включения и метод disconnect для выключения прибора
ElectricDevice.prototype.connect = function() {
  console.log('The device is on!');
  this.plugIn = true;
};

ElectricDevice.prototype.disconnect = function() {
  console.log('The device is off!');
  this.plugIn = false;
};

// Ноутбук Laptop (на базе прототипа ElectricDevice)
function Laptop(power, model) {
  this.power = power;
  this.model = model;
  this.WiFi = false;
  this.WiFiOn = function() {
    console.log('WiFi is turned on!');
    this.WiFi = true;
  };
  this.WiFiOff = function() {
    console.log('WiFi is turned off!');
    this.WiFi = false;
  };
}

Laptop.prototype = new ElectricDevice();

// Настольная лампа Lamp (на базе ElectricDevice)
function Lamp(power, color) {
  this.power = power;
  this.color = color;
}

Lamp.prototype = new ElectricDevice();

// Создаём экземпляры ноутбука и лампы
const acer = new Laptop(115, 'acer ASPIRE');
const tableLamp = new Lamp(60, 'cold white');

// Выводим информацию об электрических приборах
console.group('LAPTOP')
console.log(`My laptop model is ${acer.model}`);
acer.connect();
console.log(`My laptop power is ${acer.power} W`);
acer.WiFiOn();
console.groupEnd();

console.group('LAMP')
console.log(`My lamp color is ${tableLamp.color}`);
tableLamp.connect();
console.log(`My lamp power is ${tableLamp.power} W`);
console.groupEnd();

// Подсчитываем суммарную мощность потребляемой приборами электроэнергии
let powerSum = acer.power + tableLamp.power;
console.log(`The total power is ${powerSum} W`);

