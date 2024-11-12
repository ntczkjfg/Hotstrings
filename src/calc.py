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
    
    def bisect(self, f, guess = 0.01):
        """Solves f(x) = 0 by bisecting"""
        # Make our first endpoint be the guess, calculate its value
        a = guess
        try:
            f_a = f(a)
        except:
            # The guess isn't in f's domain - try random values until we find one that is
            found_a = False
            for radius in [.01, .1, 1, 10, 100, 1000, 10000]:
                if found_a: break
                for _ in range(10):
                    a = random.choice([1, -1]) * random.random() * radius
                    try:
                        f_a = f(a)
                        found_a = True
                        break
                    except:
                        continue
            if not found_a:
                # We failed to find even a single value f was defined for. Bummer. 
                return None
        # Now we search until we find another endpoint with opposite sign
        # Going to search random points around our guess, in increasingly large radiuses
        found_b = False
        for radius in [.01, .1, 1, 10, 100, 1000, 10000]:
            if found_b: break
            for _ in range(10):
                b = random.choice([1, -1]) * random.random() * radius + a
                try:
                    f_b = f(b)
                except:
                    # We don't know f's domain ¯\_(ツ)_/¯
                    continue
                if f_a * f_b < 0:
                    found_b = True
                    break
        if not found_b:
            # We failed to find a point on f with opposite sign to f(a). Oh well. 
            return None
        # We found a b with opposite sign! Now to bisect
        tolerance = 1e-15
        while abs(f(a)) > tolerance:
            # Bisect
            c = (a+b)/2
            f_c = f(c)
            if f_a*f_c < 0:
                # If f_a and f_c have opposite sign, then this is our new b
                b = c
            else:
                # Otherwise it's our new a
                a = c
        return a
    
    def calc(self, user_input = None):
        """
        Parses user input in the context of the calculator

        Primary purpose is to take in mathematical expressions, and have them converted into a numerical result
        Can also define custom functions and variables, print defined functions and variables, and clear functions and variables
        """
        if user_input is None:
            return {'func': self.calc,
                    'max': 500,
                    'time': 90}
        user_input = user_input.replace(' ', '')
        if user_input == 'clear':
            # Clears all user functions and variables
            return self.clear()
        elif user_input == 'vars':
            # Prints built-in variables as well as any user-defined variables
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
            # Prints built-in functions as well as any user-defined functions
            output = 'Default functions: exp, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, sqrt, cbrt, ln, log, ceil, floor, factorial, gamma, comb, perm, radians, degrees, round (among others)'
            if self.user_funcs_raw:
                output += '\nUser functions: '
                for user_func in self.user_funcs_raw.values():
                    output += f'{user_func[0]}({user_func[1]}), '
                output = output[:-2]
            else:
                output += '\nNo user functions.'
            return output
        output = ''
        # Below regex substitute replaces 'ans' and '_' with the previous output of this calculator
        # Expression is complicated to avoid accidental uses
        # For example, 'x_1' is a valid variable name and should not have its _ replaced
        user_input = re.sub(r'([^a-z0-9_]|^)(_|ans)([^a-z0-9_]|$)', rf'\g<1>({self.last_output})\g<3>', user_input)
        # If user_input ends in =, write result as an equation
        if user_input.endswith('='):
            user_input = user_input[:-1]
            output += user_input + ' = '
        # If there's still an = in the input, check if they're trying to define a function or variable, or solve an equation
        if '=' in user_input:
            if match := re.match(r'^([a-z]+[a-z0-9]*)\(((?:[a-z]+[a-z0-9_]*,)*(?:[a-z]+[a-z0-9_]*))\)=(.+)$', user_input):
                return self.func(match)
            elif match := re.match(r'^([a-z]+[a-z0-9_]*)=(.+)$', user_input):
                return self.var(match)
            else:
                return self.solve(user_input)
        if user_input:
            result = self.evaluate(user_input)
        else:
            # ''
            return
        # Save the output for use with ans/_ variable in next calculation
        self.last_output = result
        output = output + self.last_output
        return output
    
    def calculator(self, user_input = None):
        """Persistent calculator, keeps doing calculations until its input is empty"""
        if user_input is None:
            return {'func': self.calculator,
                    'max': 500,
                    'time': 3600}
        if user_input == '':
            # Empty input, time to quit - that logic is handled in gather_input()
            return 'end_calculator'
        user_input = user_input.strip()
        # Ending with = formats the output as an equation, like "7+8 = 15"
        # In this mode we force this
        if not user_input.endswith('='):
            user_input += '='
        # Append a linebreak so calculations can continue easier
        return self.calc(user_input) + '\n'
    
    def clear(self):
        """Deletes all user variables and functions"""
        self.user_vars, self.user_funcs_raw = {}, {}
        self.update_user_funcs()
        self.hotstrings.save_settings()
        return
    
    def evaluate(self, expression):
        """Evaluates the given calculation and formats the result"""
        try:
            expression = self.format_expression(expression)
        except Exception as e:
            if e.args[0] == 'AbsBarError':
                return 'Error: Unmatched absolute value'
            raise e
        # Let expressions use phi as a built-in variable, like pi and e
        phi = 1.6180339887498948
        # Easier to do this than to detect and properly handle complex numbers in format_expression()
        i = 1j
        try:
            output = eval(expression, globals() | self.user_vars | self.user_funcs, locals())
        except ZeroDivisionError:
            return 'Error: Division by zero'
        except NameError as e:
            # Happens when a function or variable isn't defined
            for func in self.user_funcs_raw.values():
                # Checking if the user input something like g(x,y) where this is a valid user function and parameters
                # If they did, return the function's definition for them
                if expression == f'{func[0]}({func[1]})':
                    return f'{func[0]}({func[1]}) = {self.format_nicely(func[2])}'
            # Output like: 'invalid_function_name' is not defined
            return f'Error: {e.args[0][5:]}'
        except Exception as e:
            if e.args[0] == 'ZeroLogError':
                return 'Error: log of 0'
            raise e
        # If it's complex, check if it's actually complex - if it's not, make it real, then check if it's also an integer
        if isinstance(output, complex):
            if output.imag == 0:
                output = output.real
                if output == int(output):
                    output = int(output)
        # Output in binary, octal, or hex will be a string, so they're okay - anything else is a concern
        elif isinstance(output, str):
            if output[:2] in ['0b', '0o', '0x']:
                return output
            raise ValueError(f'Unexpected string output: {output}')
        # Turn results like 3.0 into 3
        elif output == int(output):
            output = int(output)
        # 12 seems to be enough to avoid most floating point nonsense like 1.00000000000003843
        real = round(output.real, 12)
        imag = round(output.imag, 12)
        # Some weird edge cases give -0.0 as results, like e^7 - exp(7)
        if real == 0: real = 0
        if imag == 0: imag = 0
        if imag != 0:
            output = real + imag*1j
        else:
            output = real
        # Convert j to i for complex numbers, remove parenthesis (which surround complex results otherwise)
        output = str(output).replace('j', 'i').replace('(', '').replace(')', '')
        # Remove any trailing 0s and decimals - but not from scientific notation!
        if '.' in output and 'e' not in output:
            output = output.rstrip('0')
        output = output.rstrip('.')
        return output
    
    def factorize(self, n):
        """
        Returns a list of the prime factors of n
        If n is negative, it also includes -1 as a factor
        Will only include 0 or 1 in the factors list if n is 0 or 1
        """
        if not isinstance(n, int):
            if not n:
                # Empty product
                return [1]
            try:
                if float(n) == int(n):
                    n = int(n)
                else:
                    raise Exception
            except:
                raise TypeError(f'Invalid non-integer value "{n}" provided')
        factors = []
        if n < 0:
            n *= -1
            factors.append(-1)
        done = False
        for _ in range(100):
            if done: break
            # If x has any factors, they must appear before sqrt(x)
            # Compute here so it's not re-computed every iteration of the for loop
            sqrt_n = n**0.5
            # Each iteration, start our search from the most recently found factor (if there is one)
            start_val = factors[-1] if (factors and factors[-1] > 1) else 2
            if start_val > sqrt_n:
                # This happens when n is 0, 1, 2, or 3, but also when sqrt_n is smaller than the previous
                # factor found. In all of those cases we would like to append n to our factors list and finish
                factors.append(n)
                done = True
                break
            for factor in range(start_val, n):
                if n % factor == 0:
                    # Once we find a factor, add it to the list, divide it out
                    # Then reduce n by it and check for more factors
                    factors.append(factor)
                    n = n // factor
                    break
                elif factor > sqrt_n:
                    if n > 1:
                        # n is prime
                        factors.append(n)
                    done = True
                    break
        return factors
    
    def format_expression(self, expression):
        """Processes raw user input, turning it into valid mathematical Python syntax"""
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
        # Number dot or close paren followed by a letter is implied multiplication: 3sin → 3*sin
        expression = re.sub(r'([\d.)])([a-df-zA-DF-Z]|e(?![-+]?\d+))', r'\1*\2', expression)
        # Letter followed by dot is implied multiplication: x.3 → x*.3
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
        # Turn the factorial of variables, like x! and x_2!, into gamma function calls: gamma(x+1), gamma(x_2+1)
        expression = re.sub(r'([a-z][a-z0-9_]*)!', r'gamma((\g<1>) + 1)', expression)
        # Add a leading 0 to decimals without them: .3 → 0.3
        expression = re.sub(r'([^\d])\.', r'\g<1>0.', expression)
        # Turn 3.3! into gamma(3.3 + 1)
        expression = re.sub(r'(\d+\.?\d*)!', r'gamma(\1+1)', expression)
        # Turn (3+4)! into gamma((3+4)+1), or sin(3+4)! into gamma(sin(3+4)+1)
        while ')!' in expression:
            right_index = expression.index(')!')
            unclosed_parens = 1
            # Iterate leftward from )! until we find the matching (
            for i in range(right_index - 1, -1, -1):
                if expression[i] == ')':
                    unclosed_parens += 1
                elif expression[i] == '(':
                    unclosed_parens -= 1
                if unclosed_parens == 0:
                    left_index = i
                    break
            # Once we find the matching (, keep looking left
            # If it's alpha characters, assume it's a function and include them in the gamma call
            while left_index > 0 and expression[left_index - 1].isalpha():
                left_index -= 1
            expression = expression[:left_index] + 'gamma(' + expression[left_index:right_index + 1] + '+1)' + expression[right_index + 2:]
        # Unmatched number of absolute value bars
        if expression.count('|') % 2 != 0:
            raise Exception('AbsBarError')
        # Turn |anything_at_all| into abs(anything_at_all)
        while '|' in expression:
            first_index = expression.index('|')
            expression = expression[:first_index] + 'abs(' + expression[first_index + 1:]
            second_index = expression.index('|')
            expression = expression[:second_index] + ')' + expression[second_index + 1:]
        # Earlier on we substituted out binary, octal, and hex values - substitute them back in now
        for key, value in bin_oct_hex.items():
            expression = expression.replace(key, value)
        return expression
    
    def format_nicely(self, expression):
        """Takes an expression formatted for Python, and reformats it to look nice to a human"""
        expression = expression.replace(' ', '')
        expression = expression.replace('**', '^') # 3**4 → 3^4
        expression = re.sub(r'(\d)\*([a-zA-Z])', r'\1\2', expression) # 3*x → 3x
        expression = expression.replace('+', ' + ') # 3+4 → 3 + 4
        expression = expression.replace('-', ' - ') # 3-4 → 3 - 4
        expression = expression.replace(' +  - ', ' + -') # 3 + - 4 → 3 + -4
        expression = expression.replace('log', 'ln') # log(3) → ln(3)
        expression = expression.replace('log10', 'log') # log10(3) → log(3)
        return expression
    
    def func(self, match):
        """Defines a user function"""
        # regex matching done in calc() function
        func_name = match.group(1)
        func_args = match.group(2)
        func_expr = self.format_expression(match.group(3))
        if self.format_expression(func_name) in globals():
            # User tried to define a function named something like sin or log
            return f'Error: Name \'{func_name}\' is reserved'
        self.user_funcs_raw[func_name] = [func_name, func_args, func_expr]
        # If this is already the name of a variable, delete that variable
        if func_name in self.user_vars:
            del self.user_vars[func_name]
        self.update_user_funcs()
        self.hotstrings.save_settings()
        return f'{func_name}({func_args}) = {func_expr}'
    
    def make_rational(self, x):
        """
        Takes in a float x, and outputs it as a reduced fraction if one is found
        Returns x if no appropriate fraction is found
        """
        x = str(x)
        if '.' not in x: return x
        decimal_index = x.index('.')
        # Convert to a string, and cut off after 10 decimal places
        # Rounding like 0.66666666667 would throw us off
        new_x = str(x[:decimal_index + 11])
        decimal_part = new_x[decimal_index + 1:]
        # Checks for a repeating decimal - wants at least 3 repeats
        if match := re.search(r'(.+?)\1\1', decimal_part):
            match_index = new_x.index(match.group(1), decimal_index)
            match_len = len(match.group(1))
            repeating_part = match.group(1)*3
            # Below code tries to ensure we've actually found the repeating part of the decimal
            if not new_x.endswith(repeating_part):
                # Could be like 0.43743743743743
                # Take off ending digits until it works
                end = ''
                temp_x = new_x
                for _ in range(match_len - 1):
                    end = temp_x[-1] + end
                    temp_x = temp_x[:-1]
                    if temp_x.endswith(repeating_part):
                        # We removed enough that it now ends in the repeating part
                        break
                else:
                    # It does not actually end in the repeating part, give up
                    return x
                if not repeating_part.startswith(end):
                    # The bit we removed doesn't repeat with the rest of the repeating part - give up
                    return x
            multiply_by = 10**(match_index - decimal_index - 1 + match_len)
            multiply_by_2 = 10**(match_index - decimal_index - 1)
            numerator = int(multiply_by * float(new_x)) - int(multiply_by_2 * float(new_x))
            denominator = multiply_by - multiply_by_2
        elif (decimal_len := len(new_x[decimal_index + 1:])) < 10:
            # The decimal is terminating
            int_part = int(new_x[:decimal_index])
            denominator = 10**decimal_len
            numerator = denominator*int_part + int(new_x[decimal_index + 1:])
        else:
            return x
        fraction = f'{numerator}/{denominator}'
        fraction_dec = eval(fraction)
        if round(fraction_dec - float(x), 10) == 0:
            return self.reduce(fraction)
        return x
    
    def newton(self, f, guess = 0.01):
        """Uses Newton's method to find a solution to f(x) = 0"""
        def df(x, h = 1e-10):
            return (f(x + h) - f(x)) / h
        x = guess
        tolerance = 1e-15
        # 100 is overkill, usually finishes in less than 10
        max_iterations = 100
        for _ in range(max_iterations):
            y = f(x)
            if isinstance(y, str): return y # Contains an error message
            dy = df(x)
            if dy == 0:
                # Derivative got too close to 0, the method isn't converging
                return None
            x = x - y/dy
            if abs(f(x)) < tolerance:
                # Solution found
                break
        else:
            # Reached max_iterations without converging, oh well
            return None
        return x
    
    def reduce(self, frac):
        """Takes in a fraction, and reduces it to lowest terms"""
        if not isinstance(frac, str):
            raise TypeError(f'Invalid non-string {frac} provided')
        if '/' not in frac:
            return frac
        # Split into numerator and denominator, factorize both
        numerator, denominator = frac.split('/')
        num_factors = self.factorize(int(numerator))
        den_factors = self.factorize(int(denominator))
        factors_to_delete = []
        # We will delete common factors to reduce. Iterate through all factors of the numerator
        # As we find matching factors, remove them from the denominator, and mark them for later
        # deletion from the numerator, so as to not mess up our iterating
        for index, factor in enumerate(num_factors):
            if factor in den_factors:
                del den_factors[den_factors.index(factor)]
                factors_to_delete.insert(0, index)
        for index in factors_to_delete:
            del num_factors[index]
        # Multiply all remaining factors to get reduced numerator and denominator
        numerator = math.prod(num_factors)
        denominator = math.prod(den_factors)
        if denominator == 1:
            # It's just an integer
            return str(numerator)
        if numerator == 0:
            # It's 0
            return str('0')
        return f'{numerator}/{denominator}'
    
    def solve(self, user_input = None):
        """Solves an equation for x"""
        if not user_input:
            return {'func': self.solve,
                    'max': 500,
                    'time': 90}
        if '=' not in user_input:
            # If they just provided an expression, not an equation, find its root
            user_input = user_input + '=0'
        # Turn left = right into left - (right) = 0
        equation = self.format_expression(user_input).split('=')
        equation = f'{equation[0]} - ({equation[1]})'
        # Uses Newton's method
        def f(x):
            try:
                return float(self.evaluate(equation.replace('x', f'({x})')))
            except ValueError:
                return 'Invalid equation, make sure x is the only unknown'
        answer = self.newton(f)
        if not answer:
            answer = self.bisect(f)
            if not answer:
                return 'No solution found'
        answer = str(round(answer, 12))
        rational_answer = self.make_rational(answer)
        if rational_answer != answer and float(self.evaluate(equation.replace('x', f'({rational_answer})'))) == 0:
            self.last_output = rational_answer
            return 'x = ' + self.last_output
        self.last_output = answer
        return 'x ≈ ' + self.last_output
    
    def update_user_funcs(self):
        """Builds lambda functions from custom user functions."""
        # Do it 2 times to allow earlier functions to reference later functions successfully
        for _ in range(2):
            for func in self.user_funcs_raw.values():
                func_name = func[0]
                func_args = func[1]
                func_expr = func[2]
                self.user_funcs[func_name] = eval(f'lambda {func_args}: {func_expr}', globals() | self.user_vars | self.user_funcs)
    
    def var(self, match):
        """Defines a user variable"""
        # regex matching done in calc() function
        var_name = match.group(1)
        var_expr = self.format_expression(match.group(2))
        if var_name in globals() or self.format_expression(var_name) in globals() or var_name == 'x':
            return f'Error: Name \'{var_name}\' is reserved'
        try:
            var_expr = self.evaluate(var_expr)
            var_expr = float(var_expr)
        except ValueError:
            # Assume it's a complex number and try again but with j
            if 'i' in var_expr:
                var_expr = var_expr.replace('i', 'j')
                try:
                    var_expr = complex(var_expr)
                except ValueError:
                    return 'Invalid expression'
            else:
                return 'Invalid expression'
        self.user_vars[var_name] = var_expr
        # If this was already the name of a user function, delete that function
        if var_name in self.user_funcs_raw:
            del self.user_funcs_raw[var_name]
        self.update_user_funcs()
        self.hotstrings.save_settings()
        return f'{var_name} = {var_expr}'

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
