# JavaScript Classes & Metaprogramming 🚀

## Learning Objectives ✨

By the end of this project, you'll understand:

* Defining JavaScript Classes 📝
* Adding methods to classes 🔧
* Working with static methods ⚡
* Class inheritance 🌱
* Metaprogramming with symbols 🔮

## Classes in JavaScript 📚

### Defining a Class 📝

Classes provide a cleaner way to implement object-oriented programming in JavaScript:

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
}

const user = new User('Alice');
```

The `constructor` is a special method that runs when you create a new instance with `new`.

### Adding Methods 🔧

Methods are functions that belong to class instances:

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
  
  greet() {
    return `Hello, I'm ${this.name}`;
  }
}

const user = new User('Bob');
console.log(user.greet()); // "Hello, I'm Bob"
```

### Static Methods ⚡

Static methods belong to the class itself, not instances. They're perfect for utility functions:

```javascript
class Calculator {
  static add(a, b) {
    return a + b;
  }
}

console.log(Calculator.add(5, 3)); // 8
```

Why use static methods?
- For utility functions related to the class
- When you don't need instance data
- To create factory methods

### Class Inheritance 🌱

Classes can inherit from other classes using the `extends` keyword:

```javascript
class Animal {
  speak() {
    return "Some sound";
  }
}

class Dog extends Animal {
  speak() {
    return "Woof!";
  }
}

const dog = new Dog();
console.log(dog.speak()); // "Woof!"
```

The `super` keyword lets you call the parent class methods:

```javascript
class Cat extends Animal {
  speak() {
    return `${super.speak()} but cuter: Meow!`;
  }
}
```

## Metaprogramming & Symbols 🔮

Metaprogramming is code that manipulates code. Symbols help with this by creating unique property keys.

### Symbols Basics

Symbols are always unique:

```javascript
const id = Symbol('id');
const user = {
  name: 'Alice',
  [id]: 12345
};

console.log(user[id]); // 12345
```

No one can accidentally access or overwrite your symbol properties!

### Well-known Symbols

JavaScript has built-in symbols that let you customize object behavior:

```javascript
class Collection {
  constructor() {
    this.items = [];
  }

  add(item) {
    this.items.push(item);
  }

  // Makes your object iterable with for...of
  [Symbol.iterator]() {
    let i = 0;
    return {
      next: () => {
        return i < this.items.length ? 
          { value: this.items[i++], done: false } : 
          { done: true };
      }
    };
  }
}

const fruits = new Collection();
fruits.add('🍎');
fruits.add('🍌');

for (let fruit of fruits) {
  console.log(fruit); // Prints 🍎, then 🍌
}
```

### Property Manipulation

You can dynamically define and modify properties:

```javascript
class Product {
  constructor(name, price) {
    this.name = name;
    this._price = price;
  }
}

// Add a getter/setter after class definition
Object.defineProperty(Product.prototype, 'price', {
  get() { return this._price; },
  set(value) { 
    if (value < 0) throw new Error('Price cannot be negative');
    this._price = value;
  }
});

const phone = new Product('Phone', 500);
phone.price = 450; // Works
// phone.price = -50; // Throws error
```

### Proxy Objects

Proxies let you intercept operations on objects:

```javascript
const user = { name: 'Alex' };

const userProxy = new Proxy(user, {
  get(target, prop) {
    console.log(`Reading ${prop}`);
    return target[prop];
  },
  set(target, prop, value) {
    console.log(`Setting ${prop} to ${value}`);
    target[prop] = value;
    return true;
  }
});

userProxy.name; // Logs: "Reading name"
userProxy.age = 30; // Logs: "Setting age to 30"
```

### Reflect API

The Reflect API provides methods for interceptable JavaScript operations:

```javascript
// Instead of using direct property access
const value = obj[prop];

// You can use:
const value = Reflect.get(obj, prop);

// Or to define properties:
Reflect.defineProperty(obj, 'newProp', {
  value: 42,
  writable: true
});
```

## Practical Examples 💡

### Dynamic Form Validator

```javascript
class Validator {
  static email(value) {
    return /\S+@\S+\.\S+/.test(value);
  }
  
  static required(value) {
    return value !== undefined && value !== '';
  }
}

const validateForm = (data, rules) => {
  const errors = {};
  
  for (const [field, rule] of Object.entries(rules)) {
    if (!Validator[rule](data[field])) {
      errors[field] = `Failed ${rule} validation`;
    }
  }
  
  return errors;
};

// Usage
const userData = { name: 'Sam', email: 'bad-email' };
const rules = { name: 'required', email: 'email' };
console.log(validateForm(userData, rules));
// { email: 'Failed email validation' }
```

### Enhanced Array with Mixins

```javascript
const MathMixin = {
  sum() {
    return this.reduce((a, b) => a + b, 0);
  },
  average() {
    return this.sum() / this.length;
  }
};

// Apply the mixin to Array prototype
Object.assign(Array.prototype, MathMixin);

const prices = [10, 20, 30];
console.log(prices.sum());     // 60
console.log(prices.average()); // 20
```

## Key Takeaways 🔑

1. Classes provide a clean syntax for object-oriented programming
2. Static methods live on the class, not instances
3. Inheritance lets you extend existing classes
4. Symbols create unique, non-enumerable properties
5. Metaprogramming lets you write code that modifies other code

These concepts are foundational to modern JavaScript and crucial for advanced programming patterns!