from calc import Calc
from convert import convert

def unit_test(func, args, out):
    """
    Runs the given function with the given arguments
    Returns nothing if the output matches the given output
    Returns an error message if it does not match
    """
    result = func(args)
    if result != out:
        return f'Fail: {func.__name__}({args}) returned "{result}", expected "{out}".'
    return ''

def unit_test_calc():
    """Runs unit tests on the Calc.calc function"""
    calc = Calc().calc
    output = []
    output.append(unit_test(calc, '3+4', '7'))
    output.append(unit_test(calc, '3+4', '7'))
    output.append(unit_test(calc, '5-2', '3'))
    output.append(unit_test(calc, '6*7', '42'))
    output.append(unit_test(calc, '8/2', '4'))
    output.append(unit_test(calc, '10//3', '3'))
    output.append(unit_test(calc, '9^2', '81'))
    output.append(unit_test(calc, '(3+4)*(5-2)', '21'))
    output.append(unit_test(calc, '6*(7-2)/2', '15'))
    output.append(unit_test(calc, '8/(2*(4-2))', '2'))
    output.append(unit_test(calc, '((1+2)*(3+4))/(5+6)', '1.909090909091'))
    output.append(unit_test(calc, '3+4*5', '23'))
    output.append(unit_test(calc, '2^3+6/2', '11'))
    output.append(unit_test(calc, '2*(3+4)^2', '98'))
    output.append(unit_test(calc, '(8+1)/(3-2)^2', '9'))
    output.append(unit_test(calc, 'abs(-5)', '5'))
    output.append(unit_test(calc, 'ceil(4.3)', '5'))
    output.append(unit_test(calc, 'exp(2)', '7.389056098931'))
    output.append(unit_test(calc, 'floor(4.8)', '4'))
    output.append(unit_test(calc, 'log(10)', '1'))
    output.append(unit_test(calc, 'ln(2.718)', '0.999896315729'))
    output.append(unit_test(calc, 'sqrt(16)', '4'))
    output.append(unit_test(calc, 'e^7-exp(7)', '0'))
    output.append(unit_test(calc, 'asin(0.5)', '0.523598775598'))
    output.append(unit_test(calc, 'acos(0.5)', '1.047197551197'))
    output.append(unit_test(calc, 'atan(1)', '0.785398163397'))
    output.append(unit_test(calc, 'sin(30)', '-0.988031624093'))
    output.append(unit_test(calc, 'cos(60)', '-0.952412980415'))
    output.append(unit_test(calc, 'tan(45)', '1.619775190544'))
    output.append(unit_test(calc, '----5', '5'))
    output.append(unit_test(calc, '---5', '-5'))
    output.append(unit_test(calc, '4--------3', '7'))
    output.append(unit_test(calc, '4-------3', '1'))
    output.append(unit_test(calc, '2^3*sqrt(25)-(8+1)/((3-2)^2)', '31'))
    output.append(unit_test(calc, '3*abs(-4+5)/cos(60)-exp(1)', '-5.868175899298'))
    output.append(unit_test(calc, '((2+3)*(4-1))^2/sqrt(16)', '56.25'))
    output.append(unit_test(calc, '1+2*(3+4*(5+6*(7+8*(9+10)))/9)/8', '108.305555555556'))
    output.append(unit_test(calc, '1+23+45+6', '75'))
    output.append(unit_test(calc, '3+4*5/(2+1)', '9.666666666667'))
    output.append(unit_test(calc, '(1+2)*(3+4)/(5+6)', '1.909090909091'))
    output.append(unit_test(calc, '2^3*(4-1)+sqrt(16)/ln(2)', '29.770780163556'))
    output.append(unit_test(calc, 'ceil(3.6)*floor(2.8)+exp(1)^2', '15.389056098931'))
    output.append(unit_test(calc, '(((2+3)*4)-(1+2))/(5-6)', '-17'))
    output.append(unit_test(calc, 'sqrt(sqrt(16))', '2'))
    output.append(unit_test(calc, 'floor(ceil(5.5))', '6'))
    output.append(unit_test(calc, '(1+2*(3+(4*(5+(6*(7+(8*9)))))))', '3839'))
    output.append(unit_test(calc, 'sin(30)+cos(60)', '-1.940444604508'))
    output.append(unit_test(calc, 'tan(45)-asin(0.5)', '1.096176414946'))
    output.append(unit_test(calc, 'acos(cos(0.5236))', '0.5236'))
    output.append(unit_test(calc, 'atan(1)+sin(0.5236)-cos(0.5236)', '0.419374432177'))
    output.append(unit_test(calc, '0.5+0.25', '0.75'))
    output.append(unit_test(calc, '1.5*2.0/3.333', '0.900090009001'))
    output.append(unit_test(calc, '0.1^2+0.01^2+0.001^2', '0.010101'))
    output.append(unit_test(calc, 'sqrt(4.0)/2.5', '0.8'))
    output.append(unit_test(calc, '3/4*5', '3.75'))
    output.append(unit_test(calc, '2^10*3^5/5^3', '1990.656'))
    output.append(unit_test(calc, '-2.e-2+3', '2.98'))
    output.append(unit_test(calc, '3+2e4', '20003'))
    output.append(unit_test(calc, '.23e6/4', '57500'))
    output.append(unit_test(calc, 'sqrt(2)^10', '32'))
    output.append(unit_test(calc, 'sqrt(2)^3*(sin(45)+cos(45))/2.5', '1.557021428693'))
    output.append(unit_test(calc, '(1+2*(3+4/2.0))^2', '121'))
    output.append(unit_test(calc, 'exp(1)^2*3.5-floor(sqrt(9.9))', '22.861696346257'))
    output.append(unit_test(calc, '2^0', '1'))
    output.append(unit_test(calc, '.9(8+3)', '9.9'))
    output.append(unit_test(calc, '0^5', '0'))
    output.append(unit_test(calc, '(-2)^3', '-8'))
    output.append(unit_test(calc, '4-3*-2', '10'))
    output.append(unit_test(calc, '10^-2', '0.01'))
    output.append(unit_test(calc, '1.5e2^2', '22500'))
    output.append(unit_test(calc, '1.5e+2^2', '22500'))
    output.append(unit_test(calc, 'exp(2*(1+sin(0.5236)))', '20.085579519137'))
    output.append(unit_test(calc, 'abs(-5)+ceil(-3.8)+floor(4.2)', '6'))
    output.append(unit_test(calc, '3--3', '6'))
    output.append(unit_test(calc, '3*-(4+8)', '-36'))
    output.append(unit_test(calc, 'abs(-1)+ceil(-1)+floor(-1)', '-1'))
    output.append(unit_test(calc, 'log(0.00001)', '-5'))
    output.append(unit_test(calc, '2^3+sqrt(16)*(sin(30)+cos(60))/abs(-5)', '6.447644316394'))
    output.append(unit_test(calc, '(1+2*(3+sqrt(16)))/(5-(exp(1)^2))', '-6.278630295335'))
    output.append(unit_test(calc, '1.2+(7.2-3)^9.2//17/7+ceil(4.3-exp(2.2))*abs(-8.2)-floor(-9.9)-log(8.443e*ln(sqrt(84)))+asin(.2)-acos(.4)+atan(.8)-sin(1.6)+cos(3.2)-tan(6.4)', '4527.723928415436'))
    output.append(unit_test(calc, '(4*3).9', '10.8'))
    output.append(unit_test(calc, 'sqrt(-8)', '2.828427124746i'))
    output.append(unit_test(calc, 'ln(-4)', '1.38629436112+3.14159265359i'))
    output.append(unit_test(calc, 'log(0)', 'Error: log of 0'))
    output.append(unit_test(calc, 'asin(17)', '1.570796326795+3.525494348078i'))
    output.append(unit_test(calc, 'arccos(-4)', '3.14159265359-2.063437068896i'))
    output.append(unit_test(calc, '0^-4.2', 'Error: Division by zero'))
    output.append(unit_test(calc, '(-4)^7.2', '-17489.99084486581-12707.222163219401i'))
    output.append(unit_test(calc, '-4^2', '-16'))
    output.append(unit_test(calc, '1/0', 'Error: Division by zero'))
    output.append(unit_test(calc, 'sqrt(((20-11)^2 + (3-11)^2 + (2-11)^2 + (10-11)^2 + (20-11)^2)/5)', '7.848566748139'))
    return output

def unit_test_convert():
    """Runs unit tests on the convert function"""
    output = []
    output.append(unit_test(convert, '212 f c', '100℃'))
    output.append(unit_test(convert, '32 f c', '0℃'))
    output.append(unit_test(convert, '-40 f c', '-40℃'))
    output.append(unit_test(convert, '32 fahrenheit celsius', '0℃'))
    output.append(unit_test(convert, '100 celsius fahrenheit', '212℉'))
    output.append(unit_test(convert, '273.15 kelvin celsius', '0℃'))
    output.append(unit_test(convert, '212 fahrenheit kelvin', '373.15 K'))
    output.append(unit_test(convert, '0 celsius kelvin', '273.15 K'))
    output.append(unit_test(convert, '77 fahrenheit celsius', '25℃'))
    output.append(unit_test(convert, '25 celsius fahrenheit', '77℉'))
    output.append(unit_test(convert, '500 kelvin fahrenheit', '440.33℉'))
    output.append(unit_test(convert, '273 kelvin celsius', '-0.15℃'))
    output.append(unit_test(convert, '-40 celsius fahrenheit', '-40℉'))
    output.append(unit_test(convert, '1 meter kilometer', '1.0e-03 kilometers'))
    output.append(unit_test(convert, '1000 millimeter meter', '1 meter'))
    output.append(unit_test(convert, '5 mile kilometer', '8.05 kilometers'))
    output.append(unit_test(convert, '5280 foot mile', '1 mile'))
    output.append(unit_test(convert, '100 centimeter meter', '1 meter'))
    output.append(unit_test(convert, '0.5 kilometer mile', '0.31 miles'))
    output.append(unit_test(convert, '10000 meter kilometer', '10 kilometers'))
    output.append(unit_test(convert, '1 inch centimeter', '2.54 centimeters'))
    output.append(unit_test(convert, '2000 yard mile', '1.14 miles'))
    output.append(unit_test(convert, '3.28084 meter foot', "10.76'"))
    output.append(unit_test(convert, '1 meter2 kilometer2', '1.0e-06 kilometer²'))
    output.append(unit_test(convert, '10000 meter2 hectare', '1 hectare'))
    output.append(unit_test(convert, '100 acre meter2', '404685.64 meter²'))
    output.append(unit_test(convert, '2 hectare meter2', '20000 meter²'))
    output.append(unit_test(convert, '100 foot2 meter2', '9.29 meter²'))
    output.append(unit_test(convert, '1 mile2 kilometer2', '2.59 kilometer²'))
    output.append(unit_test(convert, '0.4047 hectare acre', '1 acre'))
    output.append(unit_test(convert, '1 kilometer2 acre', '247.11 acres'))
    output.append(unit_test(convert, '43560 feet2 acre', '1 acre'))
    output.append(unit_test(convert, '1000000 meter2 kilometer2', '1 kilometer²'))
    output.append(unit_test(convert, '1 liter milliliter', '1000 milliliters'))
    output.append(unit_test(convert, '1000 centimeter3 liter', '1 liter'))
    output.append(unit_test(convert, '1 gallon liter', '3.79 liters'))
    output.append(unit_test(convert, '3.78541 liter gallon', '1 gallon'))
    output.append(unit_test(convert, '0.5 quart pint', '1 pint'))
    output.append(unit_test(convert, '1 meter3 liter', '1000 liters'))
    output.append(unit_test(convert, '250 milliliter cup', '1.06 cups'))
    output.append(unit_test(convert, '1 foot3 liter', '28.32 liters'))
    output.append(unit_test(convert, '500 liter meter3', '0.5 meter³'))
    output.append(unit_test(convert, '1000 milliliter liter', '1 liter'))
    output.append(unit_test(convert, '1 hour minute', '60 minutes'))
    output.append(unit_test(convert, '60 second minute', '1 minute'))
    output.append(unit_test(convert, '86400 second day', '1 day'))
    output.append(unit_test(convert, '2 day hour', '48 hours'))
    output.append(unit_test(convert, '1000000 millisecond second', '1000 seconds'))
    output.append(unit_test(convert, '1 week day', '7 days'))
    output.append(unit_test(convert, '24 hour day', '1 day'))
    output.append(unit_test(convert, '60 minute hour', '1 hour'))
    output.append(unit_test(convert, '1 year day', '365.25 days'))
    output.append(unit_test(convert, '1000 microsecond millisecond', '1 millisecond'))
    output.append(unit_test(convert, '1 kilogram gram', '1000 grams'))
    output.append(unit_test(convert, '1000 gram kilogram', '1 kilogram'))
    output.append(unit_test(convert, '1 ton kilogram', '907.18 kilograms'))
    output.append(unit_test(convert, '2 pound kilogram', '0.91 kilograms'))
    output.append(unit_test(convert, '1 ounce gram', '28.35 grams'))
    output.append(unit_test(convert, '0.5 kilogram pound', '1.1 lbs'))
    output.append(unit_test(convert, '453.592 gram pound', '1 lb'))
    output.append(unit_test(convert, '100 kilogram ton', '0.11 tons'))
    output.append(unit_test(convert, '10000 milligram gram', '10 grams'))
    output.append(unit_test(convert, '2 metric_ton kilogram', '2000 kilograms'))
    output.append(unit_test(convert, '360 degree radian', '6.28 radians'))
    output.append(unit_test(convert, '1 radian degree', '57.3°'))
    output.append(unit_test(convert, '180 degree radians', '3.14 radians'))
    output.append(unit_test(convert, '90 degree radian', '1.57 radians'))
    output.append(unit_test(convert, '2 radians degree', '114.59°'))
    output.append(unit_test(convert, '2*pi radians degree', '360°'))
    output.append(unit_test(convert, '0.5 radian degree', '28.65°'))
    output.append(unit_test(convert, '6.28318 radian degree', '360°'))
    output.append(unit_test(convert, '45 degree radian', '0.79 radians'))
    output.append(unit_test(convert, '0.707 radian degree', '40.51°'))
    return output

def unit_test_solve():
    """Runs unit tests on the Calc.solve function"""
    solve = Calc().solve
    output = []
    output.append(unit_test(solve, 'sin(x) = 0', 'x = 0'))
    output.append(unit_test(solve, 'ln(x+1)/ln(2)-ln(x)/ln(2) = 4', 'x = 1/15'))
    output.append(unit_test(solve, 'pi*x = 3', 'x ≈ 0.954929658551'))
    return output

def unit_tests():
    """Runs all the unit tests, and returns their outputs"""
    output = []
    output += unit_test_calc()
    output += unit_test_convert()
    output += unit_test_solve()
    output.append('Done!')
    # Remove empty strings
    output = [i for i in output if i]
    return '\n'.join(output)
