# calculator.py
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
class Calculator:
    def add(self, a, b):
        args = [a, b]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCalculatorǁadd__mutmut_orig'), object.__getattribute__(self, 'xǁCalculatorǁadd__mutmut_mutants'), args, kwargs, self)
    def xǁCalculatorǁadd__mutmut_orig(self, a, b):
        return a + b
    def xǁCalculatorǁadd__mutmut_1(self, a, b):
        return a - b
    
    xǁCalculatorǁadd__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCalculatorǁadd__mutmut_1': xǁCalculatorǁadd__mutmut_1
    }
    xǁCalculatorǁadd__mutmut_orig.__name__ = 'xǁCalculatorǁadd'

    def subtract(self, a, b):
        args = [a, b]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCalculatorǁsubtract__mutmut_orig'), object.__getattribute__(self, 'xǁCalculatorǁsubtract__mutmut_mutants'), args, kwargs, self)

    def xǁCalculatorǁsubtract__mutmut_orig(self, a, b):
        return a - b

    def xǁCalculatorǁsubtract__mutmut_1(self, a, b):
        return a + b
    
    xǁCalculatorǁsubtract__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCalculatorǁsubtract__mutmut_1': xǁCalculatorǁsubtract__mutmut_1
    }
    xǁCalculatorǁsubtract__mutmut_orig.__name__ = 'xǁCalculatorǁsubtract'

    def multiply(self, a, b):
        args = [a, b]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCalculatorǁmultiply__mutmut_orig'), object.__getattribute__(self, 'xǁCalculatorǁmultiply__mutmut_mutants'), args, kwargs, self)

    def xǁCalculatorǁmultiply__mutmut_orig(self, a, b):
        return a * b

    def xǁCalculatorǁmultiply__mutmut_1(self, a, b):
        return a / b
    
    xǁCalculatorǁmultiply__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCalculatorǁmultiply__mutmut_1': xǁCalculatorǁmultiply__mutmut_1
    }
    xǁCalculatorǁmultiply__mutmut_orig.__name__ = 'xǁCalculatorǁmultiply'

    def divide(self, a, b):
        args = [a, b]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCalculatorǁdivide__mutmut_orig'), object.__getattribute__(self, 'xǁCalculatorǁdivide__mutmut_mutants'), args, kwargs, self)

    def xǁCalculatorǁdivide__mutmut_orig(self, a, b):
        if b == 0:
            return "Error"
        return a / b

    def xǁCalculatorǁdivide__mutmut_1(self, a, b):
        if b != 0:
            return "Error"
        return a / b

    def xǁCalculatorǁdivide__mutmut_2(self, a, b):
        if b == 1:
            return "Error"
        return a / b

    def xǁCalculatorǁdivide__mutmut_3(self, a, b):
        if b == 0:
            return "XXErrorXX"
        return a / b

    def xǁCalculatorǁdivide__mutmut_4(self, a, b):
        if b == 0:
            return "error"
        return a / b

    def xǁCalculatorǁdivide__mutmut_5(self, a, b):
        if b == 0:
            return "ERROR"
        return a / b

    def xǁCalculatorǁdivide__mutmut_6(self, a, b):
        if b == 0:
            return "Error"
        return a * b
    
    xǁCalculatorǁdivide__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCalculatorǁdivide__mutmut_1': xǁCalculatorǁdivide__mutmut_1, 
        'xǁCalculatorǁdivide__mutmut_2': xǁCalculatorǁdivide__mutmut_2, 
        'xǁCalculatorǁdivide__mutmut_3': xǁCalculatorǁdivide__mutmut_3, 
        'xǁCalculatorǁdivide__mutmut_4': xǁCalculatorǁdivide__mutmut_4, 
        'xǁCalculatorǁdivide__mutmut_5': xǁCalculatorǁdivide__mutmut_5, 
        'xǁCalculatorǁdivide__mutmut_6': xǁCalculatorǁdivide__mutmut_6
    }
    xǁCalculatorǁdivide__mutmut_orig.__name__ = 'xǁCalculatorǁdivide'

    def power(self, base, exp):
        args = [base, exp]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCalculatorǁpower__mutmut_orig'), object.__getattribute__(self, 'xǁCalculatorǁpower__mutmut_mutants'), args, kwargs, self)

    def xǁCalculatorǁpower__mutmut_orig(self, base, exp):
        return base ** exp

    def xǁCalculatorǁpower__mutmut_1(self, base, exp):
        return base * exp
    
    xǁCalculatorǁpower__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCalculatorǁpower__mutmut_1': xǁCalculatorǁpower__mutmut_1
    }
    xǁCalculatorǁpower__mutmut_orig.__name__ = 'xǁCalculatorǁpower'

    def sqrt(self, a):
        args = [a]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCalculatorǁsqrt__mutmut_orig'), object.__getattribute__(self, 'xǁCalculatorǁsqrt__mutmut_mutants'), args, kwargs, self)

    def xǁCalculatorǁsqrt__mutmut_orig(self, a):
        if a < 0:
            return "Error"
        return a ** 0.5

    def xǁCalculatorǁsqrt__mutmut_1(self, a):
        if a <= 0:
            return "Error"
        return a ** 0.5

    def xǁCalculatorǁsqrt__mutmut_2(self, a):
        if a < 1:
            return "Error"
        return a ** 0.5

    def xǁCalculatorǁsqrt__mutmut_3(self, a):
        if a < 0:
            return "XXErrorXX"
        return a ** 0.5

    def xǁCalculatorǁsqrt__mutmut_4(self, a):
        if a < 0:
            return "error"
        return a ** 0.5

    def xǁCalculatorǁsqrt__mutmut_5(self, a):
        if a < 0:
            return "ERROR"
        return a ** 0.5

    def xǁCalculatorǁsqrt__mutmut_6(self, a):
        if a < 0:
            return "Error"
        return a * 0.5

    def xǁCalculatorǁsqrt__mutmut_7(self, a):
        if a < 0:
            return "Error"
        return a ** 1.5
    
    xǁCalculatorǁsqrt__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCalculatorǁsqrt__mutmut_1': xǁCalculatorǁsqrt__mutmut_1, 
        'xǁCalculatorǁsqrt__mutmut_2': xǁCalculatorǁsqrt__mutmut_2, 
        'xǁCalculatorǁsqrt__mutmut_3': xǁCalculatorǁsqrt__mutmut_3, 
        'xǁCalculatorǁsqrt__mutmut_4': xǁCalculatorǁsqrt__mutmut_4, 
        'xǁCalculatorǁsqrt__mutmut_5': xǁCalculatorǁsqrt__mutmut_5, 
        'xǁCalculatorǁsqrt__mutmut_6': xǁCalculatorǁsqrt__mutmut_6, 
        'xǁCalculatorǁsqrt__mutmut_7': xǁCalculatorǁsqrt__mutmut_7
    }
    xǁCalculatorǁsqrt__mutmut_orig.__name__ = 'xǁCalculatorǁsqrt'

    def modulo(self, a, b):
        args = [a, b]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCalculatorǁmodulo__mutmut_orig'), object.__getattribute__(self, 'xǁCalculatorǁmodulo__mutmut_mutants'), args, kwargs, self)

    def xǁCalculatorǁmodulo__mutmut_orig(self, a, b):
        return a % b  

    def xǁCalculatorǁmodulo__mutmut_1(self, a, b):
        return a / b  
    
    xǁCalculatorǁmodulo__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCalculatorǁmodulo__mutmut_1': xǁCalculatorǁmodulo__mutmut_1
    }
    xǁCalculatorǁmodulo__mutmut_orig.__name__ = 'xǁCalculatorǁmodulo'
