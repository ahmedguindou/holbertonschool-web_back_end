# 🚀 Python Async Generators & Comprehensions 🐍✨

This repository contains examples and explanations of asynchronous generators, async comprehensions, and type annotations for generators in Python.

## 📚 Learning Objectives

At the end of this project, you will be able to explain to anyone, **without the help of Google**:
* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators

## 💫 Asynchronous Generators Explained

Async generators are magical beasts that combine two powerful Python concepts:
- 🔄 Generators (yield values incrementally)
- ⏱️ Async programming (non-blocking I/O operations)

### 🏗️ Creating an Async Generator

```python
import asyncio
import random
from typing import AsyncGenerator

async def temperature_sensor() -> AsyncGenerator[float, None]:
    """Simulates reading temperatures from a sensor every 2 seconds"""
    temp = 20.0  # Start at 20°C
    while True:
        # Simulate sensor reading delay
        await asyncio.sleep(2)  # ⏳ Non-blocking wait!
        
        # Update temperature with some variation
        temp += (0.5 - random.random())  # 🌡️ Temperature fluctuates
        
        yield temp  # 📤 Send out current temperature
```

### 🔑 Key Differences from Regular Generators:

1. 🔮 Declaration uses `async def` instead of just `def`
2. 🧠 Can use `await` inside the generator body
3. 📥 Consumers must use `async for` or `await anext()` to get values
4. 🛑 Raises `StopAsyncIteration` instead of `StopIteration` when done

### 🎯 Real-World Use Cases:

- 📊 Streaming data processing
- 🌐 Web scraping with rate limiting
- 🔌 IoT sensor monitoring
- 🗄️ Processing large files without loading into memory

## 🧩 Async Comprehensions in Detail

Async comprehensions let you build collections from async generators in a concise way! 🎨

### 📝 Examples:

```python
async def main():
    # 📋 List from async generator
    temps = [temp async for temp in temperature_sensor() if temp > 21.0][:5]
    
    # 📊 Dict with calculated values
    readings = {i: temp async for i, temp in enumerate(temperature_sensor()) if i < 5}
    
    # 🔢 Set of unique values
    unique_temps = {round(temp) async for temp in temperature_sensor()}
    
    # 🔄 Nested comprehension with async_range (hypothetical)
    async def async_range(n):
        for i in range(n):
            await asyncio.sleep(0.1)
            yield i
            
    matrix = [[i*j async for j in async_range(5)] for i in range(3)]
```

### 💡 Why Use Async Comprehensions?

1. 📝 Clean, readable code
2. 🚀 Non-blocking operations
3. 🧰 Familiar syntax to regular comprehensions
4. 🔍 Filtering with conditions
5. 🔄 Transformation in a single expression

## 🏷️ Type Annotations for Generators

Type hints make your code more maintainable and help IDE tools understand your intentions! 🔮

### 🧬 Understanding the Type Signature:

For regular generators: `Generator[YieldType, SendType, ReturnType]`
- 📤 **YieldType**: What type of values are yielded
- 📥 **SendType**: What type can be sent back via .send()
- 🏁 **ReturnType**: What type is returned at the end

For async generators: `AsyncGenerator[YieldType, SendType]`
- Note: Async generators don't support explicit return values like regular generators!

### 🔬 Type Annotation Examples:

```python
from typing import Generator, AsyncGenerator, Iterator, AsyncIterator, TypeVar, List, Dict

T = TypeVar('T')  # Generic type variable

# Regular generator
def simple_gen() -> Generator[int, None, None]:
    yield 1
    yield 2

# Generator that accepts input via send()
def echo_gen() -> Generator[int, str, None]:
    msg = yield 0
    while msg != "stop":
        msg = yield len(msg)

# Alternative syntax
def another_gen() -> Iterator[str]:
    yield "hello"
    yield "world"

# Async generator
async def async_str_gen() -> AsyncGenerator[str, None]:
    await asyncio.sleep(1)
    yield "hello"
    await asyncio.sleep(1)
    yield "world"

# Alternative syntax for async
async def another_async_gen() -> AsyncIterator[int]:
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i

# Advanced generator with generics
def transform_gen(items: List[T]) -> Generator[str, None, Dict[str, int]]:
    count = 0
    for item in items:
        count += 1
        yield f"Item {count}: {item}"
    return {"total": count}  # Return value when generator completes
```

## 🌟 Complete Working Example

Here's a practical example bringing everything together:

```python
import asyncio
import random
from typing import AsyncGenerator, Dict, List

async def fetch_data(user_id: int) -> AsyncGenerator[Dict[str, any], None]:
    """Simulate fetching user activity metrics"""
    activities = ["login", "purchase", "pageview", "click"]
    
    for _ in range(5):  # Simulate 5 data points per user
        await asyncio.sleep(random.uniform(0.1, 0.5))  # 🌐 Network delay
        
        activity = random.choice(activities)
        value = random.uniform(0, 100)
        
        yield {
            "user_id": user_id,
            "activity": activity,
            "value": round(value, 2)
        }

async def process_user_data(user_ids: List[int]):
    # 📊 Create list of async generator tasks
    user_tasks = [fetch_data(uid) for uid in user_ids]
    
    # 📋 Using async comprehension to collect all data
    all_data = []
    for task in user_tasks:
        data_points = [data_point async for data_point in task]
        all_data.extend(data_points)
    
    # 🔍 Finding high values using async comprehension
    test_user = random.choice(user_ids)
    high_values = [data["value"] 
                  async for data in fetch_data(test_user)
                  if data["value"] > 75]
    
    # 📈 Create summary using dict comprehension
    activity_counts = {}
    for activity in ["login", "purchase", "pageview", "click"]:
        count = 0
        async for data in fetch_data(user_ids[0]):
            if data["activity"] == activity:
                count += 1
        activity_counts[activity] = count
    
    return all_data, high_values, activity_counts

async def main():
    user_ids = [101, 202, 303, 404, 505]
    results = await process_user_data(user_ids)
    print(f"✅ Processed {len(results[0])} data points")
    print(f"🔝 Found {len(results[1])} high-value activities")
    print(f"📊 Activity summary: {results[2]}")

# 🚀 Run the program
if __name__ == "__main__":
    asyncio.run(main())
```

## 🎓 Advanced Tips & Tricks

1. 🧪 **Exception Handling**: Use try/except inside async generators to gracefully handle errors
2. 🔌 **Cleanup**: Use `try/finally` to ensure resources are released properly
3. 🧠 **Memory Efficiency**: Process data in chunks to maintain low memory usage
4. 🔄 **Chaining**: Feed one async generator's output into another
5. 🏎️ **Performance**: Use `asyncio.gather()` to run multiple async generators in parallel

## 📝 Practice Exercises

1. Create an async generator that reads lines from a large file without loading the entire file into memory
2. Implement an async generator that paginates through an API, yielding results page by page
3. Write type-annotated generator functions that transform data types during iteration
4. Create a pipeline of multiple async generators that process data in stages

## 📚 Further Resources

- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [PEP 525 – Asynchronous Generators](https://peps.python.org/pep-0525/)
- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [typing module Documentation](https://docs.python.org/3/library/typing.html)