# 🚀 Asynchronous Python Programming Guide 🚀

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- ⏳ `async` and `await` syntax
- 🔄 How to execute an async program with `asyncio`
- 🔀 How to run concurrent coroutines
- 📋 How to create asyncio tasks
- 🎲 How to use the random module

## ⏳ Async and Await Syntax

Async/await is Python's syntax for defining and working with coroutines - functions that can pause and resume execution.

- `async def` declares an asynchronous function (coroutine)
- `await` pauses the execution of the current coroutine until the awaited task completes

```python
async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # Pause execution for 1 second
    print("End")
```

## 🔄 Executing an Async Program with Asyncio

The `asyncio` module provides the infrastructure to run and manage coroutines:

```python
import asyncio

async def main():
    await my_coroutine()

# Run the event loop
asyncio.run(main())  # Python 3.7+
```

`asyncio.run()` creates an event loop, runs the coroutine, and closes the loop when complete.

## 🔀 Running Concurrent Coroutines

Multiple coroutines can run concurrently using functions like `asyncio.gather()`:

```python
async def main():
    # Run three coroutines concurrently
    results = await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3()
    )
```

## 📋 Creating Asyncio Tasks

Tasks are higher-level abstractions built on coroutines:

```python
async def main():
    # Create and schedule a task
    task = asyncio.create_task(my_coroutine())
    
    # Do other work while the task runs
    await asyncio.sleep(0.1)
    
    # Wait for the task to complete
    await task
```

Tasks allow coroutines to run in the background while you do other operations.

## 🎲 Using the Random Module

The `random` module provides functions for generating random numbers:

```python
import random

# Random float between 0 and 1
random.random()  

# Random integer between a and b (inclusive)
random.randint(1, 10)  

# Random choice from a sequence
random.choice(['apple', 'banana', 'cherry'])  

# Shuffle a list in-place
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  
```

## 🔍 Complete Example

Here's a complete example combining all concepts:

```python
import asyncio
import random

async def random_sleep(name):
    sleep_time = random.uniform(0.5, 3)
    print(f"🛌 {name} sleeping for {sleep_time:.2f} seconds")
    await asyncio.sleep(sleep_time)
    print(f"⏰ {name} woke up!")
    return sleep_time

async def main():
    print("🚀 Starting program")
    
    # Create and schedule tasks
    tasks = [
        asyncio.create_task(random_sleep(f"Task {i}")) 
        for i in range(5)
    ]
    
    # Run another coroutine while tasks are running
    await asyncio.sleep(0.1)
    print("🔄 Main program continues while tasks run")
    
    # Wait for all tasks to complete and collect results
    results = await asyncio.gather(*tasks)
    
    print(f"✅ All tasks completed")
    print(f"📊 Sleep times: {[f'{t:.2f}' for t in results]}")
    print(f"⭐ Longest sleep: {max(results):.2f}s")

# Run the program
if __name__ == "__main__":
    asyncio.run(main())
```

## 📚 Further Reading

- [Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Random Module Documentation](https://docs.python.org/3/library/random.html)
