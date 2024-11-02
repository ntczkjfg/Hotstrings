import re
import cmath
import math
from math import ceil, floor, cbrt, factorial, gamma, comb, perm, radians, degrees, e, pi, tau
import random

class Calc:
    def __init__(self, hotstrings = None):
        self.hotstrings = hotstrings
        self.user_vars = {}
        self.user_funcs_raw = {}
        self.user_funcs = {}
        self.last_output = ''

    def update_user_funcs(self):
        # Do it 2 times to allow earlier functions to reference later functions successfully
        for _ in range(2):
            for func in self.user_funcs_raw.values():
                func_name = func[0]
                func_args = func[1]
                func_expr = func[2]
                self.user_funcs[func_name] = eval(f'lambda {func_args}: {func_expr}', globals() | self.user_vars | self.user_funcs)

    def format_expression(self, expression):
        expression = expression.lower().replace(' ', '')
        bin_oct_hex = {}
        # Substitute out hex, octal, and binary values so the below string manipulations don't mess them up
        # Temporarily replace them with unique integers that are unlikely to cause problems
        while match := re.search(r'(0x[0-9a-f]*)|(0b[01]*)|(0o[1-7]*)', expression):
            key = str(random.randint(1000000, 2000000))
            while key in expression:
                key = str(random.randint(1000000, 2000000))
            bin_oct_hex[key] = match.group(1)
            expression = expression.replace(match.group(1), key)
        # Number dot or close paren followed by a letter is implied multiplication: 3sin -> 3*sin
        expression = re.sub(r'([\d.)])([a-df-zA-DF-Z]|e(?![-+]?\d+))', r'\1*\2', expression)
        # Letter followed by  dot is implied multiplication: x.3 -> x*.3
        expression = re.sub(r'([a-df-zA-DF-Z]|e(?!-?\d+))(\.)', r'\1*\2', expression)
        #  Turn 3(4+5) into 3*(4+5)
        expression = re.sub(r'(\d)\(', r'\1*(', expression)
        # Turn (4+5)3 into (4+5)*3
        expression = re.sub(r'\)(\d|\.)', r')*\1', expression)
        # Turn (3+4)(5+6) into (3+4)*(5+6)
        expression = re.sub(r'\)\(', ')*(', expression)
        # Turn |3+4||5+6| into |3+4|*|5+6|
        expression = re.sub(r'\|\|', '|*|', expression)
        # Below 9 just map from ways I may want to type things to the actual function names
        expression = expression.replace('arc', 'a')
        expression = expression.replace('ceiling', 'ceil')
        expression = expression.replace('fact(', 'factorial(')
        expression = expression.replace('rad(', 'radians(')
        expression = expression.replace('deg(', 'degrees(')
        expression = expression.replace('log', 'log10')
        expression = expression.replace('ln', 'log')
        expression = expression.replace('^', '**')
        expression = expression.replace('[', '(').replace(']', ')')
        expression = expression.replace('pi!', 'gamma(pi+1)').replace('e!', 'gamma(e+1)').replace('phi!', 'gamma(phi+1)')
        expression = re.sub(r'([a-z][a-z0-9_]*)!', r'gamma((\g<1>) + 1)', expression)
        # Turn .3 into 0.3
        expression = re.sub(r'([^\d])\.', r'\g<1>0.', expression)
        # Turn 3.3! into gamma(3.3 + 1)
        expression = re.sub(r'(\d+\.?\d*)!', r'gamma(\1+1)', expression)
        # Turn (3+4)! into gamma((3+4)+1), or sin(3+4)! into gamma(sin(3+4)+1)
        while ')!' in expression:
            right_index = expression.index(')!')
            unclosed_parens = 1
            for i in range(right_index - 1, -1, -1):
                if expression[i] == ')':
                    unclosed_parens += 1
                elif expression[i] == '(':
                    unclosed_parens -= 1
                if unclosed_parens == 0:
                    left_index = i
                    break
            while left_index > 0 and expression[left_index - 1].isalpha():
                left_index -= 1
            expression = expression[:left_index] + 'gamma(' + expression[left_index:right_index + 1] + '+1)' + expression[right_index + 2:]
        if expression.count('|') % 2 != 0:
            raise Exception('AbsBarError')
        # Turn |anything_at_all| into abs(anything_at_all)
        while '|' in expression:
            first_index = expression.index('|')
            expression = expression[:first_index] + 'abs(' + expression[first_index + 1:]
            second_index = expression.index('|')
            expression = expression[:second_index] + ')' + expression[second_index + 1:]
        for key, value in bin_oct_hex.items():
            expression = expression.replace(key, value)
        return expression

    def evaluate(self, expression):
        try:
            expression = self.format_expression(expression)
        except Exception as e:
            if e.args[0] == 'AbsBarError':
                return 'Error: Unmatched absolute value'
            raise e
        phi = 1.6180339887498948
        i = 1j
        try:
            output = eval(expression, globals() | self.user_vars | self.user_funcs, locals())
        except ZeroDivisionError:
            return 'Error: Division by zero'
        except NameError as e:
            for func in self.user_funcs_raw.values():
                if expression == f'{func[0]}({func[1]})':
                    return f'{func[0]}({func[1]}) = {func[2].replace("**", "^")}'
            return f'Error: {e.args[0][5:]}'
        except Exception as e:
            if e.args[0] == 'ZeroLogError':
                return 'Error: log of 0'
            raise e
        if isinstance(output, complex):
            if output.imag == 0:
                output = output.real
                if output == int(output):
                    output = int(output)
        elif isinstance(output, str):
            if output[:2] in ['0b', '0o', '0x']:
                return output
            raise ValueError(f'Unexpected string output: {output}')
        elif output == int(output):
            output = int(output)
        real = round(output.real, 12)
        imag = round(output.imag, 12)
        # Some weird edge cases give -0.0 as results, like e^7 - exp(7)
        if real == 0: real = 0
        if imag == 0: imag = 0
        if imag != 0:
            output = real + imag*1j
        else:
            output = real
        output = str(output).replace('j', 'i').replace('(', '').replace(')', '')
        if '.' in output:
            output = output.rstrip('0')
        output = output.rstrip('.')
        return output

    def calculator(self, user_input = None):
        if user_input is None:
            return {'func': self.calculator,
                    'max': 500,
                    'time': 3600}
        if user_input == '':
            return 'end_calculator'
        user_input = user_input.strip()
        if not user_input.endswith('='):
            user_input += '='
        return self.calc(user_input) + '\n'

    def calc(self, user_input = None):
        if user_input is None:
            return {'func': self.calc,
                    'max': 500,
                    'time': 90}
        user_input = user_input.replace(' ', '')
        if user_input == 'clear':
            return self.clear()
        elif user_input == 'vars':
            output = 'Default vars: pi, e, phi'
            if self.user_vars:
                output += '\nUser vars: '
                for user_var in self.user_vars:
                    output += user_var + ', '
                output = output[:-2]
            else:
                output += '\nNo user vars.'
            return output
        elif user_input in ['funcs', 'functions']:
            output = 'Default functions: exp, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, sqrt, cbrt, ln, log, ceil, floor, factorial, gamma, comb, perm, radians, degrees, round (among others)'
            if self.user_funcs_raw:
                output += '\nUser functions: '
                for user_func in self.user_funcs_raw.values():
                    output += f'{user_func[0]}({user_func[1]}), '
                output = output[:-2]
            else:
                output += '\nNo user functions.'
            return output
        # How the user indicates a specific rounding amount
        #if rounding := (',' in user_input):
        #    index = user_input.index(',')
        #    round_num = user_input[index + 1:]
        #    user_input = user_input[:index]
        rounding = False
        output = ''
        user_input = re.sub(r'([^a-z0-9_]|^)(_|ans)([^a-z0-9_]|$)', rf'\g<1>({self.last_output})\g<3>', user_input)
        # If user_input ends in =, write result as an equation
        if user_input.endswith('='):
            user_input = user_input[:-1]
            output += user_input + ' = '
        if '=' in user_input:
            if match := re.match(r'^([a-z]+[a-z0-9]*)\(((?:[a-z]+[a-z0-9_]*,)*(?:[a-z]+[a-z0-9_]*))\)=(.+)$', user_input):
                return self.func(match)
            elif match := re.match(r'^([a-z]+[a-z0-9_]*)=(.+)$', user_input):
                return self.var(match)
        if user_input:
            result = self.evaluate(user_input)
        else:
            return
        self.last_output = round(result, round_num) if rounding else result
        output = output + self.last_output
        return output

    def solve(self, user_input = None):
        if not user_input:
            return {'func': self.solve,
                    'max': 500,
                    'time': 90}
        equation = self.format_expression(user_input).split('=')
        equation = f'{equation[0]} - ({equation[1]})'
        def f(x):
            return float(self.evaluate(equation.replace('x', f'({x})')))
        def df(x, h=1e-10):
            return (f(x + h) - f(x)) / h
        x = 0.01
        tolerance = 1e-14
        max_iterations = 1000
        for _ in range(max_iterations):
            y = f(x)
            dy = df(x)
            if abs(dy) < tolerance:
                return 'No solution found'
            x = x - y/dy
            if abs(f(x)) < tolerance:
                break
        else:
            return 'No solution found'
        self.last_output = str(round(x, 10))
        return 'x = ' + self.last_output

    def func(self, match):
        func_name = match.group(1)
        func_args = match.group(2)
        func_expr = self.format_expression(match.group(3))
        if func_name in globals():
            return f'Error: Name \'{func_name}\' is reserved'
        self.user_funcs_raw[func_name] = [func_name, func_args, func_expr]
        if func_name in self.user_vars:
            del self.user_vars[func_name]
        self.update_user_funcs()
        self.hotstrings.save_settings()
        return f'{func_name}({func_args}) = {func_expr}'

    def var(self, match):
        var_name = match.group(1)
        var_expr = self.format_expression(match.group(2))
        if var_name in globals():
            return f'Error: Name \'{var_name}\' is reserved'
        try:
            var_expr = self.evaluate(var_expr)
            var_expr = float(var_expr)
        except ValueError:
            if 'i' in var_expr:
                var_expr = var_expr.replace('i', 'j')
                try:
                    var_expr = complex(var_expr)
                except ValueError:
                    return 'Invalid expression'
            else:
                return 'Invalid expression'
        self.user_vars[var_name] = var_expr
        if var_name in self.user_funcs_raw:
            del self.user_funcs_raw[var_name]
        self.update_user_funcs()
        self.hotstrings.save_settings()
        return f'{var_name} = {var_expr}'

    def clear(self):
        self.user_vars, self.user_funcs_raw = {}, {}
        self.update_user_funcs()
        self.hotstrings.save_settings()
        return


# Custom logic for each of the following to use math version when possible, and cmath version otherwise
def exp(x):
    return cmath.exp(x) if isinstance(x, complex) else math.exp(x)

def sin(x):
    return cmath.sin(x) if isinstance(x, complex) else math.sin(x)
def cos(x):
    return cmath.cos(x) if isinstance(x, complex) else math.cos(x)
def tan(x):
    return cmath.tan(x) if isinstance(x, complex) else math.tan(x)
def asin(x):
    if (isinstance(x, complex)
        or x < -1
        or x > 1):
        return cmath.asin(x)
    return math.asin(x)
def acos(x):
    if (isinstance(x, complex)
        or x < -1
        or x > 1):
        return cmath.acos(x)
    return math.acos(x)
def atan(x):
    return cmath.atan(x) if isinstance(x, complex) else math.atan(x)

def sinh(x):
    return cmath.sinh(x) if isinstance(x, complex) else math.sinh(x)
def cosh(x):
    return cmath.cosh(x) if isinstance(x, complex) else math.cosh(x)
def tanh(x):
    return cmath.tanh(x) if isinstance(x, complex) else math.tanh(x)
def asinh(x):
    return cmath.asinh(x) if isinstance(x, complex) else math.asinh(x)
def acosh(x):
    if (isinstance(x, complex)
        or x < 1):
        return cmath.acosh(x)
    return math.acosh(x)
def atanh(x):
    if (isinstance(x, complex)
        or x <= -1
        or x >= 1):
        return cmath.atanh(x)
    return math.atanh(x)

def sqrt(x):
    if (isinstance(x, complex)
        or x < 0):
        return cmath.sqrt(x)
    return math.sqrt(x)
def log(x):
    if x == 0:
        raise Exception('ZeroLogError')
    if (isinstance(x, complex)
        or x < 0):
        return cmath.log(x)
    return math.log(x)
def log10(x):
    if x == 0:
        raise Exception('ZeroLogError')
    if (isinstance(x, complex)
        or x < 0):
        return cmath.log10(x)
    return math.log10(x)
