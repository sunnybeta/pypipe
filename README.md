# Pypipe

*A python function to pipe functions to return a single value*


## Features

* Validates parameter types and return types based on annotations

## Install

```python
pip install git+https://github.com/sunnybeta/pypipe
```

## Usage

```python
from pypipe import Pipe

def foo(x) -> int:
    return x+1

def bar(x: int) -> int:
    return x ** 2

def baz(x: int) -> int:
    return x - 1

print(Pipe(6, [foo,bar]).run())
# >>> 49

print(Pipe(6, [foo,bar]).add(baz).run())
# >>> 48
```

:)
