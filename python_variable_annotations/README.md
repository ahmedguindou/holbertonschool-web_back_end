# Python Type Annotations 🐍✨

## Table of Contents
- [Introduction](#introduction)
- [Type Annotations in Python 3](#type-annotations-in-python-3-)
- [Using Type Annotations for Functions and Variables](#using-type-annotations-for-functions-and-variables-)
- [Duck Typing](#duck-typing-)
- [Validating Code with mypy](#validating-code-with-mypy-)
- [Resources](#resources-)

## Introduction

This README provides a comprehensive guide to Python type annotations, an important feature introduced in Python 3.5 that enhances code quality, readability, and maintainability.

## Type Annotations in Python 3 📝

Type annotations allow you to specify the expected types of variables, function parameters, and return values.

### Basic Type Annotations

```python
# Variable annotations
name: str = "Alice"
age: int = 30
is_student: bool = True
height: float = 5.9

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### Complex Type Annotations

```python
from typing import List, Dict, Tuple, Optional, Union

# List of integers
numbers: List[int] = [1, 2, 3]

# Dictionary mapping strings to integers
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# Tuple of specific types
person: Tuple[str, int, float] = ("Charlie", 32, 5.8)

# Optional type (can be None)
maybe_name: Optional[str] = None

# Union type (can be one of multiple types)
id_number: Union[int, str] = "A12345"
```

> 💡 **Note**: Since Python 3.9, you can use built-in collection types for annotations:
> ```python
> # Python 3.9+
> numbers: list[int] = [1, 2, 3]
> scores: dict[str, int] = {"Alice": 95}
> ```

## Using Type Annotations for Functions and Variables 🔍

Type annotations help document your code's intent and enable static type checking:

```python
from typing import List, Dict, Optional

def process_user_data(
    user_id: int,
    name: str,
    scores: List[int],
    metadata: Optional[Dict[str, str]] = None
) -> float:
    """
    Process user data and return average score.
    
    Args:
        user_id: Unique identifier for the user
        name: User's full name
        scores: List of test scores
        metadata: Optional additional information
        
    Returns:
        Average score as a float
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
```

### Benefits of using type annotations ✅

- Self-documenting code
- Better IDE support (auto-completion, error detection)
- Easier refactoring
- Catch type-related errors before runtime
- Improved code maintenance and readability

## Duck Typing 🦆

Duck typing is a programming concept used in dynamically typed languages like Python. The name comes from the saying:

> "If it walks like a duck and quacks like a duck, then it's a duck."

In duck typing, the type or class of an object is less important than the methods it defines or properties it has. What matters is whether an object has the attributes and methods needed for a particular context.

### Example

```python
# Duck typing example
class Duck:
    def swim(self):
        return "Swimming like a duck"
        
    def quack(self):
        return "Quack!"

class Person:
    def swim(self):
        return "Swimming like a human"
        
    def quack(self):
        return "I'm imitating a duck!"

def make_it_swim_and_quack(entity):
    # We don't care about the type of entity
    # as long as it has swim() and quack() methods
    print(entity.swim())
    print(entity.quack())

duck = Duck()
person = Person()

# Both work because both have the required methods
make_it_swim_and_quack(duck)
make_it_swim_and_quack(person)
```

### Protocols (Python 3.8+)

Type annotations can work alongside duck typing through protocols:

```python
from typing import Protocol

class Quacker(Protocol):
    def quack(self) -> str: ...

def make_it_quack(entity: Quacker) -> None:
    print(entity.quack())
    
# Any class with a quack method can be used
# without explicitly inheriting from Quacker
```

## Validating Code with mypy 🔎

`mypy` is a static type checker for Python that can validate your type annotations and catch potential errors before runtime.

### Installation

```bash
pip install mypy
```

### Basic Usage

```bash
mypy your_script.py
```

### Example

Let's say you have a file `example.py`:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("hello", 5)  # Type error
```

Running `mypy example.py` would show:

```
example.py:4: error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

### mypy Configuration

You can configure mypy using a `mypy.ini` file:

```ini
[mypy]
python_version = 3.9
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True

[mypy.plugins.numpy.ndarray]
plugin_is_directory = True
```

### Gradual Typing 📈

One advantage of mypy is that it supports gradual typing - you can add type annotations to your codebase incrementally:

```python
# This function has type annotations
def double(x: int) -> int:
    return x * 2

# This function doesn't, but mypy can still check code that calls it
def triple(x):
    return x * 3
```

## Resources 📚

- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [mypy documentation](https://mypy.readthedocs.io/)
- [Python typing module documentation](https://docs.python.org/3/library/typing.html)
- [Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)