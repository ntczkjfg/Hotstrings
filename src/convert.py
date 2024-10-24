from calc import Calc

# Formats user input to make sure it's a number, remove leading and trailing
# whitespace, and remove leading 0s. Purposely uses string operations to
# avoid floating point precision errors messing up significant figures
def format_val(value):
    value = str(value).lower()
    try:
        float(value)
    except ValueError:
        value = Calc().evaluate(value)
        try:
            float(value)
        except ValueError:
            return 'NaN'
    # Remove leading and trailing whitespace
    value = value.strip()
    # Remove leading 0s, accounting for leading '-' in negatives
    if value[0] == '-':
        value = '-' + value[1:].lstrip('0')
    if value in ['', '-', '.', '-.']:
        value = '0'
    # Intentionally allows a trailing decimal ('4.') to indicate
    # significance of trailing 0s in an integer value
    return value

def determine_sig_figs(value):
    value = format_val(value)
    # Remove any scientific notation, not relevant here
    if 'e' in value:
        value = value.split('e')[0]
    # Negatives likewise not relevant
    if value[0] == '-':
        value = value[1:]
    # Number is an integer
    if '.' not in value:
        if value == '0':
            return 1
        value = value.rstrip('0')
        return len(value)
    # Number has a decimal point
    sig_figs = 0
    # Split into integer and decimal parts
    value = value.split('.')
    if len(value[0]) > 0 and int(value[0]) > 0:
        # If the integer part isn't 0, it's all significant
        sig_figs += len(value[0])
    if sig_figs > 0:
        # If the integer part isn't 0, then all of the decimal part is significant
        sig_figs += len(value[1])
    else:
        # If the integer part is 0, only parts of the decimal from the leftmost nonzero number are significant, unless it's all 0s
        trimmed_value = value[1].lstrip('0')
        if trimmed_value == '':
            sig_figs += len(value[1])
        else:
            sig_figs += len(trimmed_value)
    return sig_figs

# Formats value to have sig_figs significant figures
def format_sig_figs(value, sig_figs):
    value = str(value)
    current_sig_figs = determine_sig_figs(value)
    if current_sig_figs == sig_figs:
        # Done! That was easy
        return value
    # Handle scientific notation
    suffix = ''
    if 'e' in value:
        suffix = 'e' + value.split('e')[1]
        value = value.split('e')[0]
    if current_sig_figs < sig_figs:
        # Just add on 0s until it's good
        if '.' not in value:
            # Add a decimal if we don't already have one
            # Doing so may make previously insignificant 0s turn significant
            # Slight chance this give us too many sig figs, but without scientific notation,
            # it has to be a choice between too many and too few in this edge case
            current_sig_figs += len(value) - len(value.rstrip('0'))
            value += '.'
        value += '0' * (sig_figs - current_sig_figs)
        value += suffix
        return value
    # From here on we have too many sig figs, and must cut back
    if '.' not in value:
        # Just a bit easier logic-wise if every value has a decimal
        value += '.'
    # Find index of the digit we'll round on - so the (sig_figs)th sig fig
    sig_figs_seen = 0
    for i, char in enumerate(value):
        if char.isdigit() and (sig_figs_seen != 0 or char != '0'):
            sig_figs_seen += 1
            if sig_figs_seen == sig_figs:
                round_pos = i
                break
    if round_pos < (dot_index := value.index('.')):
        # Rounding left of the decimal
        round_pos = i - dot_index + 1
        value = str(round(float(value), round_pos))
        if '.' in value:
            value = value.split('.')[0]
        if round_pos == 0 and value[-1] == '0':
            # Rounded to the 1s place, and that last sig fig is a 0, so we need to include a decimal to show that
            # eg, '10.' has two sig figs but '10' only has one
            value += '.'
    else:
        round_pos = i - dot_index
        value = str(round(float(value), round_pos))
    value += suffix
    return value

# More of a 'less dumb round' - if rounding sends the value to 0 then it
# rounds it to the same number of digits in scientific notation instead
def smart_round(value, digits):
    rounded = round(value, digits)
    if rounded != 0:
        return rounded
    value = f'{value:e}'
    value = value.split('e')
    rounded = str(round(float(value[0]), digits)) + 'e' + value[1]
    if int(float(rounded)) == float(rounded):
        return int(float(rounded))
    return rounded

# Generic calculation function, alternates between multiplying and adding values to value
# If reverse is True then it performs the inverse calculation instead
# Main reason for this instead of just a multiplication is temperature conversions
def generic_convert(value, params, reverse = False):
    if reverse:
        mult = True
        for i in range(len(params)):
            if mult:
                params[i] = 1 / params[i]
                mult = False
            else:
                params[i] *= -1
                mult = True
        params = params[::-1]
    mult = True
    for param in params:
        if mult:
            value *= param
            mult = False
        else:
            value += param
            mult = True
    return value

# Does some cleaning up of user input for convert below, to match unit alias lists
# Main point was to drastically reduce how many distinct aliases had to be listed
def format_unit(unit):
    unit = unit.replace('^', '') # m^3 → m3
    unit = unit.replace(' ', '') # fluid ounce → fluidounce
    unit = unit.replace('uared', '') # metersquared → metersq
    unit = unit.replace('uare', '') # squaremeter → sqmeter
    unit = unit.replace('sq', '2') # sqmeter → 2meter
    unit = unit.replace('bic', '') # cubicmeter → cumuter
    unit = unit.replace('bed', '') # metercubed → metercu
    unit = unit.replace('be', '') # cubemeter → cumeter
    unit = unit.replace('cu', '3') # cumeter → 3meter
    if unit[0].isdigit():
        unit = unit[1:] + unit[0] # 3meter → meter3
        if unit == 'p3' or unit == 'ps3': # cup(s) → 3p(s) → p(s)3 → cup
            unit = 'cup'
    if (ends_in_number := (ending_num := unit[-1]).isdigit()):
        unit = unit[:-1] # meters3 → meters
    if unit[-1] == 's' and len(unit) != 1:
        unit = unit[:-1] # meters → meter
    if ends_in_number:
        unit = unit + ending_num # meter → meter3
    return unit

def converter(user_input):
    value = user_input[0].strip()
    unit1 = user_input[1].strip()
    unit2 = user_input[2].strip()
    honor_sig_figs, no_suffix = False, False
    # Precede value with ! to maintain significant figure count
    if value[0] == '!':
        honor_sig_figs = True
        value = value[1:]
    # Postcede value with ! to skip writing the unit after the result
    if value[-1] == '!':
        no_suffix = True
        value = value[:-1]
    value = format_val(value)
    user_input[0] = value
    if value == 'NaN':
        return 'NaN'
    # Each dimension has its own dict of supported units, with aliases and conversions for each unit
    # Dimensional dicts' keys double as unit name and as the display unit text when sending results
    # Dimensional dicts' values are list of lists.  First list is acceptable aliases for that unit (after input parsing)
    # Second list is parameters instructing on how to convert that unit to the base unit for its dimension
    # Base unit for each dimension is first listed
    dimensions = {
        'temperature': {
            '℃':  [['c', 'celsiu'], []],
            '℉':  [['f', 'fahrenheit'], [1, -32, 5/9]],
            ' K': [['k', 'kelvin'], [1, -273.15]],
            '°R': [['r', 'rankine'], [5/9, -273.15]] },
        'length': {
            ' meters': [['m', 'me', 'meter', 'metre'], []],
            '"': [['in', 'inch', 'inche', '"'], [.0254]],
            "'": [['ft', 'foot', 'feet', "'"], [.3048]],
            ' yards': [['y', 'yd', 'yard'], [.9144]],
            ' fathoms': [['fathom'], [1.8288]],
            ' furlongs': [['furlong'], [201.168]],
            ' miles': [['mi', 'mile'], [1609.344]],
            ' nautical miles': [['nauticalmile'], [1852]],
            ' astronomical units': [['au', 'astronomical units'], [149597870700]],
            ' lightyears': [['ly', 'lightyear'], [9460730472580800]],
            ' parsecs': [['ps', 'parsec'], [149597870700*648000/3.14159265358979]] },
        'area': {
            ' m²': [['m2', 'meter2', 'metre2'], []],
            ' in²': [['in2', 'inch2', 'inche2'], [6.4516/10000]],
            ' ft²': [['ft2', 'foot2', 'feet2'], [929.0304/10000]],
            ' yd²': [['y2', 'yd2', 'yard2'], [0.83612736]],
            ' miles²': [['mi2', 'mile2'], [2589988.110336]],
            ' acres': [['ac', 'acre'], [4046.8564224]],
            ' hectares': [['ha', 'hectare'], [10000]] },
        'volume': {
            ' liters': [['l', 'liter'], []],
            ' m³': [['m3', 'meter3', 'metre3'], [1000]],
            ' tsp': [['tsp', 'teaspoon'], [4.92892159375/1000]],
            ' tbsp': [['tb', 'tbsp', 'tablespoon'], [3*4.92892159375/1000]],
            ' fluid ounces': [['fl', 'fluidounce', 'flounce', 'fl.ounce', 'floz', 'fl.oz', 'fluidoz', 'oz', 'ounce'], [.0295735295625]],
            ' cups': [['c', 'cup'], [236.5882365/1000]],
            ' pints': [['p', 'pint'], [236.5882365/500]],
            ' quarts': [['q', 'quart'], [236.5882365/250]],
            ' gallons': [['g', 'gal', 'gallon'], [3.785411784]],
            ' in³': [['in3', 'inch3', 'inche3'], [16.387064/1000]],
            ' ft³': [['ft3', 'foot3', 'feet3'], [28.316846592]],
            ' yd³': [['y3', 'yd3', 'yard3'], [764.554857984]],
            ' miles³': [['mi3', 'mile3'], [5451776000*764.554857984]] },
        'mass': {
            ' grams': [['g', 'gram'], []],
            ' oz': [['oz', 'ounce'], [28.349523125]],
            ' lbs': [['lb', 'pound'], [453.59237]],
            ' stones': [['st', 'stone', 's'], [6350.29318]],
            ' tons': [['ton'], [907184.74]],
            ' metric tons': [['mt', 'metricton'], [1000000]] },
        'time': {
            ' seconds': [['s', 'sec', 'second'], []],
            ' minutes': [['m', 'min', 'minute'], [60]],
            ' hours': [['h', 'hour'], [3600]],
            ' days': [['d', 'day'], [86400]],
            ' weeks': [['w', 'week'], [604800]],
            ' fortnights': [['fn', 'fortnight'], [1209600]],
            ' years': [['y', 'year'], [31557600]],
            ' decades': [['dec', 'decade'], [315576000]],
            ' scores': [['sc', 'score'], [631152000]],
            ' centuries': [['c', 'century', 'centurie'], [3155760000]],
            ' millenniums': [['mil', 'mill', 'millennium', 'millennia'], [31557600000]] },
        'angular measure': {
            '°': [['d', 'deg', 'degree'], []],
            ' radians': [['r', 'rad', 'radian'], [180/3.14159265358979]],
            ' gradians': [['grad', 'gradian'], [.9]],
            "'": [['am', 'arcm', 'arcmin', 'arcminute'], [1/60]],
            '"': [['as', 'arcs', 'arcsec', 'arcsecond'], [1/3600]] }
    }
    # SI prefixes and their associated factors
    metric_prefixes = {"quetta": 1e30, "ronna": 1e27, "yotta": 1e24, "zetta": 1e21, "exa": 1e18,
                       "peta": 1e15, "tera": 1e12, "giga": 1e9, "mega": 1e6, "kilo": 1e3,
                       "hecto": 1e2, "deca": 10, "deci": 1e-1, "centi": 1e-2, "milli": 1e-3,
                       "micro": 1e-6, "nano": 1e-9, "pico": 1e-12, "femto": 1e-15, "atto": 1e-18,
                       "zepto": 1e-21, "yocto": 1e-24, "ronto": 1e-27, "quecto": 1e-30,
                       "Q": 1e30, "R": 1e27, "Y": 1e24, "Z": 1e21, "E": 1e18, "P": 1e15, "T": 1e12,
                       "G": 1e9, "M": 1e6, "k": 1e3, "h": 1e2, "da": 10, "d": 1e-1, "c": 1e-2,
                       "m": 1e-3, "mu": 1e-6, "μ": 1e-6, "n": 1e-9, "p": 1e-12, "f": 1e-15, "a": 1e-18,
                       "z": 1e-21, "y": 1e-24, "r": 1e-27, "q": 1e-30}
    # SI symbols and the full prefix names they shorten - results always display the long name
    metric_symbols = {"Q": "quetta", "R": "ronna", "Y": "yotta", "Z": "zetta", "E": "exa",
                      "P": "peta", "T": "tera", "G": "giga", "M": "mega", "k": "kilo",
                      "h": "hecto", "da": "deca", "d": "deci", "c": "centi", "m": "milli",
                      "mu": "micro", "μ": "micro", "n": "nano", "p": "pico", "f": "femto",
                      "a": "atto", "z": "zepto", "y": "yocto", "r": "ronto", "q": "quecto"}
    # Some parsing to simplify user input and fit the formats allowed above
    unit1 = format_unit(unit1)
    unit2 = format_unit(unit2)
    # At this point user input will either be a valid match to a unit in the supported units list, perhaps with an SI prefix, or it will be invalid
    unit1_matches = []
    unit2_matches = []
    for dimension, units in dimensions.items():
        for unit, aliases in units.items():
            for alias in aliases[0]: # aliases[1] contains conversion factors
                if unit1.endswith(alias):
                    # unit1 ends in a valid unit alias - if that's the full input, or if an SI prefix completes the full input, accept it as a match
                    prefix = ''
                    if len(unit1) > len(alias):
                        prefix = unit1[:-len(alias)]
                        # Some prefixe symbols are case-sensitive so be careful.  First see if there's an exact case match, use that if there is
                        # Then see if there's a lowercase match - will allow user to type for example "Kilo" for "kilo"
                        # Lastly check for an uppercase match - for example if they typed gm instead of Gm for Gigameter
                        if prefix not in metric_prefixes:
                            if prefix.lower() in metric_prefixes:
                                prefix = prefix.lower()
                            elif prefix.upper() in metric_prefixes:
                                prefix = prefix.upper()
                            else:
                                continue
                    unit1_matches.append([dimension, unit, prefix])
                if unit2.endswith(alias):
                    prefix = ''
                    if len(unit2) > len(alias):
                        prefix = unit2[:-len(alias)]
                        if prefix not in metric_prefixes:
                            if prefix.lower() in metric_prefixes:
                                prefix = prefix.lower()
                            elif prefix.upper() in metric_prefixes:
                                prefix = prefix.upper()
                            else:
                                continue
                    unit2_matches.append([dimension, unit, prefix])
    # Check if no match was found for unit1 or unit2
    if not unit1_matches:
        return f'Unknown unit: {unit1}'
    elif not unit2_matches:
        return f'Unknown unit: {unit2}'
    match_found = False
    for match1 in unit1_matches:
        for match2 in unit2_matches:
            if match1[0] == match2[0]:
                # The matches are the same dimension - success
                unit1 = match1
                unit2 = match2
                match_found = True
                break
        if match_found:
            break
    if not match_found:
        return 'Dimensional mismatch'
    value = float(value)
    # If we have an SI prefix, use it to convert value to the prefix-free unit first - careful with area and volume units
    if (prefix := unit1[2]) != '':
        if unit[1][-1] == '²':
            value *= metric_prefixes[prefix]**2
        elif unit[1][-1] == '³':
            value *= metric_prefixes[prefix]**3
        else:
            value *= metric_prefixes[prefix]
    # Convert value to the base unit for its dimension
    value = generic_convert(value, dimensions[unit1[0]][unit1[1]][1])
    # Now convert it from the base unit to the destination unit
    value = generic_convert(value, dimensions[unit2[0]][unit2[1]][1], True)
    # If the destination unit also has an SI prefix, then convert from the prefix-free unit to it
    if (prefix := unit2[2]) != '':
        if unit2[1][-1] == '²':
            value /= metric_prefixes[prefix]**2
        elif unit2[1][-1] == '³':
            value /= metric_prefixes[prefix]**3
        else:
            value /= metric_prefixes[prefix]
    if honor_sig_figs:
        sig_figs = determine_sig_figs(user_input[0])
        value = format_sig_figs(value, sig_figs)
    else:
        value = smart_round(value, 2)
        value = str(value)
    if prefix != '':
        if prefix in metric_symbols:
            prefix = metric_symbols[prefix]
        if unit2[1][0] == ' ':
            suffix = ' ' + prefix + unit2[1][1:]
        else:
            suffix = prefix + unit2[1]
    else:
        suffix = unit2[1]
    if no_suffix:
        suffix = ''
    output = value + suffix
    return output

# Converts between units.  Format:  `convert\valueToConvert, startingUnit, destinationUnit\
# Temperature: celsius, fahrenheit, kelvin, rankine
# Length: meter, inch, foot, yard, fathom, furlong, mile, nautical mile, astronomical unit, lightyear, parsec
# Area: meter², inch², foot², yard², mile², acre, hectare
# Volume: liter, meter³, teaspoon, tablespoon, fluid ounce, cup, pint, quart, gallon, inch³, foot³, yard³, mile³
# Mass: gram, ounce, pound, stone, ton, metric ton
# Time: second, minute, hour, day, week, fortnight, year, decade, score, century, millennium
# Angular measure: degree, radian, gradian, arcminute, arcsecond
def convert(user_input = None):
    if not user_input:
        return {'func': convert,
                'max': 500,
                'time': 90}
    # All valid input has 3 parts: value, unit1, and unit2
    # Can be broken by commas or spaces
    if ',' in user_input:
        user_input = user_input.split(',')
    else:
        user_input = user_input.split(' ')
    if len(user_input) != 3:
        return 'Incorrect format'
    if user_input[2][-1] == '=':
        output = user_input[0] + ' ' + user_input[1] + ' = '
        user_input[2] = user_input[2][:-1]
    else:
        output = ''
    output += converter(user_input)
    return output
