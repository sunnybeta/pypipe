from typing import Any, Callable, List
from functools import reduce
from warnings import warn

class Pipe:

    def __init__(self, x: Any, funcs: List[Callable]) -> None:
        self.__x = x
        self.__funcs = funcs

    def add(self, func: Callable) -> "Pipe":
        """Add a Function to the list of functions to be executed
        """
        self.__funcs.append(func)
        return self

    def validate(self) -> "Pipe":
        """Validate all the functions are 'pipeable'
        """
        for i in range(len(self.__funcs)-1):
            first = self.__funcs[i]
            second = self.__funcs[i+1]
            return_type = first.__annotations__.get('return')
            if return_type == None:
                msg = f"The function '{first.__name__}' do not have a return type. Make sure the function results can be piped correctly"
                warn(msg)
                continue
            arg_types = [v for k,v in second.__annotations__.items() if k != 'return']
            if not arg_types:
                msg = f"The function '{second.__name__}' do not have annotated parameters. Make sure the function results can be piped correctly"
                warn(msg)
                continue
            if return_type not in arg_types:
                raise TypeError(f"Functions '{first.__name__}' and '{second.__name__}' are not pipeable. ;_;")
        return self

    def run(self) -> Any:
        """Execute the list of functions by passing their outputs to the next
        """
        return reduce(lambda x,func: func(x), self.__funcs, self.__x)


# FUNCTION ONLY IMPLEMENTATION
# 
# def pipe(x: Any, funcs: List[Callable]) -> Any:
# 
#     for i in range(len(funcs)-1):
# 
#         first = funcs[i]
#         second = funcs[i+1]
# 
#         return_type = first.__annotations__.get('return')
# 
#         if return_type == None:
#             msg = f"The function '{first.__name__}' do not have a return type. Make sure the function results can be piped correctly"
#             warn(msg)
#             continue
#         arg_types = [v for k,v in second.__annotations__.items() if k != 'return']
# 
#         if not arg_types:
#             msg = f"The function '{second.__name__}' do not have annotated parameters. Make sure the function results can be piped correctly"
#             warn(msg)
#             continue
# 
#         if return_type not in arg_types:
#             raise TypeError(f"Functions '{first.__name__}' and '{second.__name__}' are not pipeable. ;_;")
# 
#     return reduce(lambda x,func: func(x), funcs, x)


if __name__ == '__main__':

    def foo(x) -> int:
        return x+1

    def bar(x: int) -> int:
        return x ** 2

    def baz(x: int) -> int:
        return x - 1

    # print(pipe(6, [foo,bar,baz]))
    print(Pipe(6, [foo,bar]).add(baz).run())
