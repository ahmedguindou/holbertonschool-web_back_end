# Node.js Learning Guide

A simple guide to learn Node.js fundamentals step by step.

## What You'll Learn

- Run JavaScript with Node.js
- Work with Node.js modules
- Read files
- Use command line arguments
- Create HTTP servers
- Build apps with Express.js
- Use modern JavaScript (ES6)
- Speed up development with Nodemon

---

## 1. Running JavaScript with Node.js

Node.js runs JavaScript outside the browser.

```bash
# Check if Node.js is installed
node --version

# Run a JavaScript file
node app.js
```

**Example: hello.js**
```javascript
console.log("Hello from Node.js!");
```

Run it: `node hello.js`

---

## 2. Using Node.js Modules

Modules let you organize and reuse code.

**Using built-in modules:**
```javascript
const fs = require('fs');        // File system
const path = require('path');    // File paths
const os = require('os');        // Operating system info

console.log('Your OS:', os.platform());
```

**Creating your own modules:**
```javascript
// math.js
function add(a, b) {
    return a + b;
}
module.exports = { add };

// main.js
const { add } = require('./math');
console.log(add(2, 3)); // 5
```

---

## 3. Reading Files

Use the `fs` module to read files.

```javascript
const fs = require('fs');

// Read file (simple way)
const data = fs.readFileSync('myfile.txt', 'utf8');
console.log(data);

// Read file (better way - doesn't block)
fs.readFile('myfile.txt', 'utf8', (err, data) => {
    if (err) {
        console.log('Error:', err);
        return;
    }
    console.log(data);
});
```

---

## 4. Command Line Arguments & Environment Variables

**Command line arguments:**
```javascript
// script.js
const args = process.argv.slice(2);
console.log('Arguments:', args);

// Run: node script.js hello world
// Output: Arguments: ['hello', 'world']
```

**Environment variables:**
```javascript
const port = process.env.PORT || 3000;
const env = process.env.NODE_ENV || 'development';

console.log(`Running on port ${port} in ${env} mode`);
```

---

## 5. HTTP Server with Node.js

Create a web server using built-in modules.

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    
    if (req.url === '/') {
        res.end(JSON.stringify({ message: 'Hello World!' }));
    } else {
        res.end(JSON.stringify({ error: 'Not Found' }));
    }
});

server.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
```

---

## 6. HTTP Server with Express.js

Express makes server creation much easier.

**Install Express:**
```bash
npm init -y
npm install express
```

**Create server:**
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({ message: 'Hello Express!' });
});

app.get('/users', (req, res) => {
    res.json({ users: ['Alice', 'Bob'] });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
```

---

## 7. Advanced Express Routes

Handle different types of routes and data.

```javascript
const express = require('express');
const app = express();

// Parse JSON data
app.use(express.json());

// Route with parameter
app.get('/users/:id', (req, res) => {
    const userId = req.params.id;
    res.json({ userId: userId });
});

// Route with query parameters
// Example: /search?q=nodejs&limit=5
app.get('/search', (req, res) => {
    const query = req.query.q;
    const limit = req.query.limit || 10;
    res.json({ query, limit });
});

// POST route
app.post('/users', (req, res) => {
    const { name, email } = req.body;
    res.json({ message: `User ${name} created` });
});

app.listen(3000);
```

---

## 8. Using ES6 with Babel

Use modern JavaScript features in Node.js.

**Install Babel:**
```bash
npm install --save-dev @babel/core @babel/node @babel/preset-env
```

**Create .babelrc file:**
```json
{
  "presets": ["@babel/preset-env"]
}
```

**Use ES6 features:**
```javascript
// ES6 imports instead of require
import express from 'express';

const app = express();

// Arrow functions
const greet = (name) => `Hello, ${name}!`;

// Template literals
const message = `Server running on port ${PORT}`;

// Destructuring
const { PORT = 3000 } = process.env;

app.get('/', (req, res) => {
    res.json({ message: greet('World') });
});

app.listen(PORT);
```

**Run with Babel:**
```bash
npx babel-node server.js
```

---

## 9. Using Nodemon for Development

Nodemon automatically restarts your server when files change.

**Install Nodemon:**
```bash
npm install --save-dev nodemon
```

**Add to package.json:**
```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "dev:babel": "nodemon --exec babel-node server.js"
  }
}
```

**Run development server:**
```bash
npm run dev
```

Now your server restarts automatically when you save files!

---

## Complete Example

**package.json:**
```json
{
  "name": "my-node-app",
  "version": "1.0.0",
  "scripts": {
    "dev": "nodemon --exec babel-node server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "@babel/core": "^7.22.0",
    "@babel/node": "^7.22.0",
    "@babel/preset-env": "^7.22.0",
    "nodemon": "^3.0.0"
  }
}
```

**server.js:**
```javascript
import express from 'express';
import { readFile } from 'fs/promises';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', async (req, res) => {
    res.json({ 
        message: 'Node.js API is working!',
        timestamp: new Date().toISOString()
    });
});

app.get('/users/:id', (req, res) => {
    const { id } = req.params;
    res.json({ userId: id, name: `User ${id}` });
});

app.post('/users', (req, res) => {
    const { name } = req.body;
    res.status(201).json({ message: `Created user: ${name}` });
});

app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
```

**.babelrc:**
```json
{
  "presets": ["@babel/preset-env"]
}
```

**Run the app:**
```bash
npm run dev
```

---
