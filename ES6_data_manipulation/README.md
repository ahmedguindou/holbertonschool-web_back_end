# JavaScript Advanced Data Concepts 🚀

This README provides a comprehensive guide to advanced JavaScript array methods and data structures including map, filter, reduce, typed arrays, Set, Map, and WeakMap/WeakSet.

## Table of Contents
- [Array Methods](#array-methods)
  - [Map](#map-)
  - [Filter](#filter-)
  - [Reduce](#reduce-)
- [Typed Arrays](#typed-arrays-)
- [Modern Data Structures](#modern-data-structures)
  - [Set](#set-)
  - [Map](#map--1)
  - [WeakMap and WeakSet](#weakmap-and-weakset-)

## Array Methods

JavaScript provides powerful higher-order functions to transform arrays in elegant and concise ways.

### Map 🗺️

The `map()` method creates a new array with the results of calling a provided function on every element in the calling array.

```javascript
const numbers = [1, 2, 3, 4, 5];
const squared = numbers.map(num => num * num);
// squared: [1, 4, 9, 16, 25]
```

#### Real-world Examples:

```javascript
// Converting Celsius to Fahrenheit
const celsiusTemps = [0, 15, 30, 45];
const fahrenheitTemps = celsiusTemps.map(temp => (temp * 9/5) + 32);
// fahrenheitTemps: [32, 59, 86, 113]

// Extracting property from objects
const users = [
  { name: 'Alice', age: 25 },
  { name: 'Bob', age: 30 },
  { name: 'Charlie', age: 35 }
];
const names = users.map(user => user.name);
// names: ['Alice', 'Bob', 'Charlie']
```

### Filter 🧹

The `filter()` method creates a new array with all elements that pass the test implemented by the provided function.

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = numbers.filter(num => num % 2 === 0);
// evenNumbers: [2, 4, 6, 8, 10]
```

#### Real-world Examples:

```javascript
// Filtering products by price
const products = [
  { name: 'Laptop', price: 999 },
  { name: 'Phone', price: 699 },
  { name: 'Tablet', price: 399 },
  { name: 'Headphones', price: 199 }
];
const affordableProducts = products.filter(product => product.price < 500);
// affordableProducts: [{ name: 'Tablet', price: 399 }, { name: 'Headphones', price: 199 }]

// Filtering out null and undefined values
const mixedArray = [0, null, 'hello', undefined, 42, ''];
const cleanArray = mixedArray.filter(item => item !== null && item !== undefined);
// cleanArray: [0, 'hello', 42, '']
```

### Reduce 📊

The `reduce()` method applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value.

```javascript
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
// sum: 15
```

#### Real-world Examples:

```javascript
// Calculating total price of items in a cart
const cart = [
  { item: 'Book', price: 20 },
  { item: 'Pen', price: 5 },
  { item: 'Notebook', price: 10 }
];
const totalPrice = cart.reduce((total, product) => total + product.price, 0);
// totalPrice: 35

// Grouping objects by a property
const people = [
  { name: 'Alice', age: 25, department: 'Engineering' },
  { name: 'Bob', age: 30, department: 'Marketing' },
  { name: 'Charlie', age: 35, department: 'Engineering' },
  { name: 'Diana', age: 28, department: 'Marketing' }
];

const departmentGroups = people.reduce((groups, person) => {
  const { department } = person;
  if (!groups[department]) {
    groups[department] = [];
  }
  groups[department].push(person);
  return groups;
}, {});
// departmentGroups: {
//   Engineering: [
//     { name: 'Alice', age: 25, department: 'Engineering' },
//     { name: 'Charlie', age: 35, department: 'Engineering' }
//   ],
//   Marketing: [
//     { name: 'Bob', age: 30, department: 'Marketing' },
//     { name: 'Diana', age: 28, department: 'Marketing' }
//   ]
// }
```

### Chaining Array Methods 🔗

These methods can be chained together for more complex operations:

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const sumOfSquaresOfEvenNumbers = numbers
  .filter(num => num % 2 === 0)    // Filter even numbers: [2, 4, 6, 8, 10]
  .map(num => num * num)           // Square them: [4, 16, 36, 64, 100]
  .reduce((sum, num) => sum + num, 0);  // Sum them: 220
```

## Typed Arrays 📏

Typed arrays are array-like objects that provide a mechanism for accessing raw binary data. They're particularly useful for handling binary data efficiently and for working with WebGL, Web Audio API, or reading/writing files.

### Overview of Typed Arrays

1. **ArrayBuffer**: The base object that represents a chunk of binary data
2. **TypedArray Views**: Various views into the buffer with specific data types

```javascript
// Create a buffer with 16 bytes
const buffer = new ArrayBuffer(16);

// Create different views of the same buffer
const int32View = new Int32Array(buffer);    // View as 4 32-bit integers
const float64View = new Float64Array(buffer); // View as 2 64-bit floats
const uint8View = new Uint8Array(buffer);    // View as 16 8-bit unsigned integers
```

### Types of Typed Arrays

| Type | Bytes per Element | Description |
|------|------------------|-------------|
| Int8Array | 1 | 8-bit signed integers |
| Uint8Array | 1 | 8-bit unsigned integers |
| Uint8ClampedArray | 1 | 8-bit unsigned integers (clamped) |
| Int16Array | 2 | 16-bit signed integers |
| Uint16Array | 2 | 16-bit unsigned integers |
| Int32Array | 4 | 32-bit signed integers |
| Uint32Array | 4 | 32-bit unsigned integers |
| Float32Array | 4 | 32-bit floating point |
| Float64Array | 8 | 64-bit floating point |

### Examples of Typed Arrays

```javascript
// Create a typed array directly
const floatArray = new Float32Array([1.1, 2.2, 3.3, 4.4]);

// Modify values
floatArray[0] = 5.5;
console.log(floatArray); // Float32Array [5.5, 2.2, 3.3, 4.4]

// Practical use case: Working with colors in image processing
const rgbaData = new Uint8ClampedArray([255, 0, 0, 255, 0, 255, 0, 255]);
// This represents two pixels: red and green in RGBA format
```

## Modern Data Structures

JavaScript offers several modern data structures that solve specific problems efficiently.

### Set 🔢

A `Set` object stores unique values of any type. A value can only occur once in a Set.

```javascript
// Creating a Set
const uniqueNumbers = new Set([1, 2, 3, 3, 4, 4, 5]);
console.log(uniqueNumbers); // Set {1, 2, 3, 4, 5} (no duplicates)

// Basic operations
uniqueNumbers.add(6);           // Add a new value
uniqueNumbers.has(3);           // Check if value exists (returns true)
uniqueNumbers.delete(4);        // Remove a value
console.log(uniqueNumbers.size); // Get the size (5)

// Converting Set back to array
const numbersArray = [...uniqueNumbers]; // [1, 2, 3, 5, 6]
```

#### Common Set Use Cases:

```javascript
// Remove duplicates from an array
const numbers = [1, 2, 2, 3, 4, 4, 5];
const uniqueNumbers = [...new Set(numbers)]; // [1, 2, 3, 4, 5]

// Set operations
const setA = new Set([1, 2, 3, 4, 5]);
const setB = new Set([4, 5, 6, 7, 8]);

// Union
const union = new Set([...setA, ...setB]); // Set {1, 2, 3, 4, 5, 6, 7, 8}

// Intersection
const intersection = new Set([...setA].filter(x => setB.has(x))); // Set {4, 5}

// Difference (A - B)
const difference = new Set([...setA].filter(x => !setB.has(x))); // Set {1, 2, 3}
```

### Map 🗺️ 

A `Map` object holds key-value pairs where keys can be any data type (unlike objects where keys must be strings or symbols).

```javascript
// Creating a Map
const userRoles = new Map();

// Adding entries
userRoles.set('John', 'Admin');
userRoles.set('Jane', 'Editor');
userRoles.set('Bob', 'Subscriber');

// Objects as keys
const user1 = { name: 'Alice' };
const user2 = { name: 'Charlie' };
userRoles.set(user1, 'Moderator');
userRoles.set(user2, 'Guest');

// Basic operations
console.log(userRoles.get('Jane')); // 'Editor'
console.log(userRoles.has('Bob'));  // true
userRoles.delete('Bob');           // Remove entry
console.log(userRoles.size);       // 4
```

#### Iterating Over Maps:

```javascript
// Iterating over a Map
const fruitInventory = new Map([
  ['apples', 10],
  ['bananas', 20],
  ['oranges', 15]
]);

// Iterating over keys
for (const fruit of fruitInventory.keys()) {
  console.log(fruit); // 'apples', 'bananas', 'oranges'
}

// Iterating over values
for (const quantity of fruitInventory.values()) {
  console.log(quantity); // 10, 20, 15
}

// Iterating over entries
for (const [fruit, quantity] of fruitInventory.entries()) {
  console.log(`${fruit}: ${quantity}`); // 'apples: 10', etc.
}

// Using forEach
fruitInventory.forEach((quantity, fruit) => {
  console.log(`${fruit}: ${quantity}`);
});
```

### WeakMap and WeakSet 🔗

These are special versions of Map and Set that don't prevent their entries from being garbage-collected when no other references to the keys exist.

#### WeakMap:

```javascript
// Creating a WeakMap
const weakMap = new WeakMap();

// Working with WeakMap
let obj1 = { name: 'Object 1' };
let obj2 = { name: 'Object 2' };

weakMap.set(obj1, 'Metadata for Object 1');
weakMap.set(obj2, 'Metadata for Object 2');

console.log(weakMap.get(obj1)); // 'Metadata for Object 1'

// If obj1 is set to null and no other references exist,
// both obj1 and its value in weakMap can be garbage-collected
obj1 = null;
```

Key differences between WeakMap and Map:
- Keys must be objects
- Keys are weakly referenced (can be garbage-collected)
- Cannot be iterated (no `keys()`, `values()`, `entries()`)
- No `size` property
- No `clear()` method

#### WeakSet:

```javascript
// Creating a WeakSet
const visitedObjects = new WeakSet();

// Tracking objects
let user1 = { id: 1, name: 'Alice' };
let user2 = { id: 2, name: 'Bob' };

visitedObjects.add(user1);
visitedObjects.add(user2);

console.log(visitedObjects.has(user1)); // true

// If user1 is set to null and no other references exist,
// it can be garbage-collected and removed from the WeakSet
user1 = null;
```

## Use Cases and Best Practices 💡

### When to Use Map vs. Object
- Use **Map** when:
  - Keys are not strings/symbols (e.g., objects as keys)
  - You need to preserve insertion order
  - You frequently add/remove entries
  - You need to know the size easily
  
- Use **Object** when:
  - JSON serialization is needed
  - Working with simple key-value structures
  - Default values via prototype chain are useful

### When to Use Set vs. Array
- Use **Set** when:
  - You need to ensure unique values
  - You frequently check if a value exists
  - You need to easily add/remove items
  
- Use **Array** when:
  - Order matters and you need indexed access
  - You need array methods like map, filter, etc.
  - You may have duplicate values

### When to Use WeakMap/WeakSet
- Use these when:
  - You need to associate metadata with objects
  - You don't want to prevent garbage collection
  - You're implementing caches or storing private data

## Performance Considerations 🚀

- **Typed Arrays** are much more efficient for binary data operations than regular arrays
- **Set** lookup time is O(1) vs. O(n) for arrays
- **Map** provides better performance for frequent additions/removals than objects
- **WeakMap/WeakSet** help prevent memory leaks when working with objects

## Example: Putting It All Together

```javascript
// Processing student exam scores
const studentScores = [
  { id: 1, name: 'Alice', scores: [85, 90, 92] },
  { id: 2, name: 'Bob', scores: [75, 80, 85] },
  { id: 3, name: 'Charlie', scores: [90, 95, 85] },
  { id: 4, name: 'Diana', scores: [95, 100, 98] }
];

// Using map, filter, reduce
const highPerformers = studentScores
  .map(student => {
    // Calculate average score
    const avgScore = student.scores.reduce((sum, score) => sum + score, 0) / student.scores.length;
    return { ...student, avgScore };
  })
  .filter(student => student.avgScore >= 90)
  .map(student => student.name);

console.log('High performers:', highPerformers); // ['Alice', 'Charlie', 'Diana']

// Using Set for unique subjects taken by students
const studentSubjects = [
  { student: 'Alice', subjects: ['Math', 'Science', 'History'] },
  { student: 'Bob', subjects: ['Math', 'Art', 'Geography'] },
  { student: 'Charlie', subjects: ['Science', 'History', 'Literature'] }
];

const allSubjects = new Set();
studentSubjects.forEach(entry => {
  entry.subjects.forEach(subject => allSubjects.add(subject));
});

console.log('All subjects:', [...allSubjects]); 
// ['Math', 'Science', 'History', 'Art', 'Geography', 'Literature']

// Using Map to track assignments per subject
const subjectAssignments = new Map();

// Initialize map
allSubjects.forEach(subject => subjectAssignments.set(subject, []));

// Add assignments
subjectAssignments.get('Math').push('Algebra Quiz', 'Geometry Project');
subjectAssignments.get('Science').push('Lab Report', 'Research Paper');

console.log('Math assignments:', subjectAssignments.get('Math'));
// ['Algebra Quiz', 'Geometry Project']
```

By mastering these powerful JavaScript features, you'll be able to write more concise, efficient, and maintainable code! 🎉