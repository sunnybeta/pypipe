from pypipe import Pipe

def foo(x) -> int:
    return x+1

def bar(x: int) -> int:
    return x ** 2

def baz(x: int) -> int:
    return x - 1

print(Pipe(6, [foo,bar]).add(baz).run())
print(Pipe(6, [foo,bar]).run())
