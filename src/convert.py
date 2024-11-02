from calc import Calc

# Formats user input to make sure it's a number, remove leading and trailing
# whitespace, and remove leading 0s. Purposely uses string operations to
# avoid floating point precision errors messing up significant figures
def format_val(value):
    try:
        # See if it's already a number
        float(value)
    except ValueError:
        # If not, run it through the calculator, in case the user input an expression like 2*pi, for example
        value = Calc().evaluate(value)
        try:
            float(value)
        except ValueError:
            return 'NaN'
    # Remove leading and trailing whitespace
    value = value.strip()
    # Remove leading 0s, accounting for leading '-' in negatives
    if value.startswith('-'):
        value = '-' + value[1:].lstrip('0')
    # If the original string was '0', '-0', '0.', '-0.', etc...
    if value in ['', '-', '.', '-.']:
        value = '0'
    # Intentionally allows a trailing decimal ('4.') to indicate
    # significance of trailing 0s in an integer value
    return value

# Determines the number of significant figures in the input string
def determine_sig_figs(value):
    # Remove any scientific notation, not relevant here
    if 'e' in value:
        value = value.split('e')[0]
    # Negatives likewise not relevant
    if value.startswith('-'):
        value = value[1:]
    # Number is an integer
    if '.' not in value:
        if value == '0':
            # So we don't interpret something like '000' as having 3 sig figs
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
    # Set any scientific notation aside for now
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
        if char.isdigit() and (sig_figs_seen or char != '0'):
            sig_figs_seen += 1
            if sig_figs_seen == sig_figs:
                round_pos = i
                break
    if round_pos < (dot_index := value.index('.')):
        # Rounding left of the decimal
        round_pos = i - dot_index + 1
        value = str(round(float(value), round_pos))
        value = value.split('.')[0]
        if round_pos == 0 and value.endswith('0'):
            # Rounded to the 1s place, and that last sig fig is a 0, so we need to include a decimal to show that
            # eg, '10.' has two sig figs but '10' only has one
            value += '.'
    else:
        round_pos = i - dot_index
        value = str(round(float(value), round_pos))
    # If there was scientific notation earlier, put it back on
    value += suffix
    return value

# More of a 'less dumb round' - if rounding sends the value to 0 then it
# rounds it to the same number of digits in scientific notation instead
def smart_round(value, digits):
    rounded = round(value, digits)
    if rounded != 0:
        return rounded
    # Convert to scientific notation
    value = f'{value:e}'
    # Split into decimal and exponent parts
    value = value.split('e')
    # Round the decimal part, put the exponent part back on
    rounded = str(round(float(value[0]), digits)) + 'e' + value[1]
    # Basically if it's still 0, then just send 0
    if float(rounded) == 0:
        return 0
    return rounded

# Generic calculation function, alternates between multiplying and adding values to value
# If reverse is True then it performs the inverse calculation instead
# Main reason for this instead of just a multiplication is temperature conversions
def generic_convert(value, params, reverse = False):
    if reverse:
        # Must do the reversing step first, because params is here by reference, not value
        params = params[::-1]
        # If its length is even, it ends on an addition, and so now starts on an addition
        # We need it to start on a multiplication, so add a 1 to the beginning
        if len(params) % 2 == 0:
            params.insert(0, 1)
        mult = True
        for i in range(len(params)):
            # Take the reciprocal of multiplicative factors, the negative of additive ones
            params[i] = 1 / params[i] if mult else -1 * params[i]
            mult = not mult
    mult = True
    for param in params:
        value = value * param if mult else value + param
        mult = not mult
    return value

# Does some cleaning up of user input for convert below, to match unit alias lists
# Main point was to drastically reduce how many distinct aliases had to be listed
# Allows lots of variety in how the user types certain potentially complex inputs
def format_unit(unit):
    unit = unit.replace('^', '') # m^3 → m3
    unit = unit.replace(' ', '') # fluid ounce → fluidounce
    unit = unit.replace('_', '') # fluid_ounce → fluidounce
    unit = unit.replace('-', '') # fluid-ounce → fluidounce
    unit = unit.replace('.', '') # fl.ounce → flounce
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
    if unit.endswith('s') and len(unit) != 1:
        unit = unit[:-1] # meters → meter
    if ends_in_number:
        unit = unit + ending_num # meter → meter3
    return unit

# Each dimension has its own dict of supported units, with aliases and conversions for each unit
# Dimensional dicts' keys double as unit name and as the display unit text when sending output
# Dimensional dicts' values are dicts that contain acceptable aliases for each unit, and a list of
# parameters instructing on how to convert that unit to the base unit for its dimension (with generic_convert() function)
# Base unit for each dimension is first listed
dimensions = {
    'temperature': {
        '℃':  {
            'aliases': ['c', 'celsiu'],
            'conversion': [] },
        '℉':  {
            'aliases': ['f', 'fahrenheit'],
            'conversion': [1, -32, 5/9] },
        ' K': {
            'aliases': ['k', 'kelvin'],
            'conversion': [1, -273.15] },
        '°R': {
            'aliases': ['r', 'rankine'],
            'conversion': [5/9, -273.15] } },
    'length': {
        ' meters': {
            'aliases': ['m', 'me', 'meter', 'metre'],
            'conversion': [] },
        '"': {
            'aliases': ['in', 'inch', 'inche', '"'],
            'conversion': [.0254] },
        "'": {
            'aliases': ['ft', 'foot', 'feet', "'"],
            'conversion': [.3048] },
        ' yards': {
            'aliases': ['y', 'yd', 'yard'],
            'conversion': [.9144] },
        ' fathoms': {
            'aliases': ['fathom'],
            'conversion': [1.8288] },
        ' furlongs': {
            'aliases': ['furlong'],
            'conversion': [201.168] },
        ' miles': {
            'aliases': ['mi', 'mile'],
            'conversion': [1609.344] },
        ' nautical miles': {
            'aliases': ['nauticalmile'],
            'conversion': [1852] },
        ' astronomical units': {
            'aliases': ['au', 'astronomical units'],
            'conversion': [149597870700] },
        ' lightyears': {
            'aliases': ['ly', 'lightyear'],
            'conversion': [9460730472580800] },
        ' parsecs': {
            'aliases': ['ps', 'parsec'],
            'conversion': [149597870700*648000/3.14159265358979] } },
    'area': {
        ' meter²': {
            'aliases': ['m2', 'meter2', 'metre2'],
            'conversion': [] },
        ' in²': {
            'aliases': ['in2', 'inch2', 'inche2'],
            'conversion': [6.4516/10000] },
        ' ft²': {
            'aliases': ['ft2', 'foot2', 'feet2'],
            'conversion': [929.0304/10000] },
        ' yd²': {
            'aliases': ['y2', 'yd2', 'yard2'],
            'conversion': [0.83612736] },
        ' miles²': {
            'aliases': ['mi2', 'mile2'],
            'conversion': [2589988.110336] },
        ' acres': {
            'aliases': ['ac', 'acre'],
            'conversion': [4046.8564224] },
        ' hectares': {
            'aliases': ['ha', 'hectare'],
            'conversion': [10000] } },
    'volume': {
        ' liters': {
            'aliases': ['l', 'liter'],
            'conversion': [] },
        ' meter³': {
            'aliases': ['m3', 'meter3', 'metre3'],
            'conversion': [1000]},
        ' tsp': {
            'aliases': ['tsp', 'teaspoon'],
            'conversion': [4.92892159375/1000]},
        ' tbsp': {
            'aliases': ['tb', 'tbsp', 'tablespoon'],
            'conversion': [3*4.92892159375/1000] },
        ' fluid ounces': {
            'aliases': ['fl', 'fluidounce', 'flounce', 'floz', 'fluidoz', 'oz', 'ounce'],
            'conversion': [.0295735295625] },
        ' cups': {
            'aliases': ['c', 'cup'],
            'conversion': [236.5882365/1000] },
        ' pints': {
            'aliases': ['p', 'pint'],
            'conversion': [236.5882365/500] },
        ' quarts': {
            'aliases': ['q', 'quart'],
            'conversion': [236.5882365/250] },
        ' gallons': {
            'aliases': ['g', 'gal', 'gallon'],
            'conversion': [3.785411784] },
        ' in³': {
            'aliases': ['in3', 'inch3', 'inche3'],
            'conversion': [16.387064/1000] },
        ' ft³': {
            'aliases': ['ft3', 'foot3', 'feet3'],
            'conversion': [28.316846592] },
        ' yd³': {
            'aliases': ['y3', 'yd3', 'yard3'],
            'conversion': [764.554857984] },
        ' miles³': {
            'aliases': ['mi3', 'mile3'],
            'conversion': [5451776000*764.554857984] } },
    'mass': {
        ' grams': {
            'aliases': ['g', 'gram'],
            'conversion': [] },
        ' oz': {
            'aliases': ['oz', 'ounce'],
            'conversion': [28.349523125] },
        ' lbs': {
            'aliases': ['lb', 'pound'],
            'conversion': [453.59237] },
        ' stones': {
            'aliases': ['st', 'stone', 's'],
            'conversion': [6350.29318] },
        ' tons': {
            'aliases': ['ton'],
            'conversion': [907184.74] },
        ' metric tons': {
            'aliases': ['mt', 'metricton'],
            'conversion': [1000000] } },
    'time': {
        ' seconds': {
            'aliases': ['s', 'sec', 'second'],
            'conversion': [] },
        ' minutes': {
            'aliases': ['m', 'min', 'minute'],
            'conversion': [60] },
        ' hours': {
            'aliases': ['h', 'hour'],
            'conversion': [3600] },
        ' days': {
            'aliases': ['d', 'day'],
            'conversion': [86400] },
        ' weeks': {
            'aliases': ['w', 'week'],
            'conversion': [604800] },
        ' fortnights': {
            'aliases': ['fn', 'fortnight'],
            'conversion': [1209600] },
        ' years': {
            'aliases': ['y', 'year'],
            'conversion': [31557600] },
        ' decades': {
            'aliases': ['dec', 'decade'],
            'conversion': [315576000] },
        ' scores': {
            'aliases': ['sc', 'score'],
            'conversion': [631152000] },
        ' centuries': {
            'aliases': ['c', 'century', 'centurie'],
            'conversion': [3155760000] },
        ' millenniums': {
            'aliases': ['mil', 'mill', 'millennium', 'millennia'],
            'conversion': [31557600000] } },
    'angular measure': {
        '°': {
            'aliases': ['d', 'deg', 'degree'],
            'conversion': [] },
        ' radians': {
            'aliases': ['r', 'rad', 'radian'],
            'conversion': [180/3.14159265358979] },
        ' gradians': {
            'aliases': ['g', 'grad', 'gradian'],
            'conversion': [.9] },
        "'": {
            'aliases': ['am', "'", 'arcm', 'arcmin', 'arcminute'],
            'conversion': [1/60] },
        '"': {
            'aliases': ['as', '"', 'arcs', 'arcsec', 'arcsecond'],
            'conversion': [1/3600] } }
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

# Determines the units the user intended unit1 and unit2 to be
# Ensures they have the same dimension - for example, if they're 'd' and 'g', it
# won't match up 'degrees' and 'grams', it'll match up 'degrees' and 'gradians'
def determine_units(unit1, unit2):
    unit1_matches = []
    unit2_matches = []
    for dimension, units in dimensions.items():
        for unit, aliases in units.items():
            for alias in aliases['aliases']:
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
                    unit1_matches.append({'dim': dimension, 'unit': unit, 'prefix': prefix})
                # Just copies above logic, but appends to unit2_matches at the end instead
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
                    unit2_matches.append({'dim': dimension, 'unit': unit, 'prefix': prefix})
    # Check if no match was found for unit1 or unit2
    if not unit1_matches:
        return f'Unknown unit: {unit1}'
    elif not unit2_matches:
        return f'Unknown unit: {unit2}'
    # Return the first matching units that share dimensions
    for match1 in unit1_matches:
        for match2 in unit2_matches:
            if match1['dim'] == match2['dim']:
                # The matches are the same dimension - success
                return [match1, match2]
    return 'Dimensional mismatch'

def converter(value, unit1, unit2, sig_figs, no_suffix):
    if sig_figs:
        # Determine sig figs now, before value is changed
        sig_figs = determine_sig_figs(value)
    # Some parsing to simplify user input and fit the aliases allowed above
    unit1 = format_unit(unit1)
    unit2 = format_unit(unit2)
    # At this point user input will either be a valid match to a unit in the supported units dict, perhaps with an SI prefix, or it will be invalid
    units = determine_units(unit1, unit2)
    if isinstance(units, str):
        # Returned an error, no matching units found - return that error
        return units
    unit1, unit2 = units
    value = float(value)
    # If we have an SI prefix, use it to convert value to the prefix-free unit first - careful with area and volume units
    if prefix := unit1['prefix']:
        if unit1['unit'].endswith('²'):
            # 20 kilometer² = 20,000,000 meter²
            value *= metric_prefixes[prefix]**2
        elif unit1['unit'].endswith('³'):
            # 20 kilometer³ = 20,000,000,000 meter³
            value *= metric_prefixes[prefix]**3
        else:
            # 20 kilometer = 20,000 meter
            value *= metric_prefixes[prefix]
    # Convert value to the base unit for its dimension
    value = generic_convert(value, dimensions[unit1['dim']][unit1['unit']]['conversion'])
    # Now convert it from the base unit to the destination unit
    value = generic_convert(value, dimensions[unit2['dim']][unit2['unit']]['conversion'], True)
    # If the destination unit also has an SI prefix, then convert from the prefix-free unit to it
    # Same logic as above just with division
    if si_prefix := unit2['prefix']:
        if unit2['unit'].endswith('²'):
            value /= metric_prefixes[si_prefix]**2
        elif unit2['unit'].endswith('³'):
            value /= metric_prefixes[si_prefix]**3
        else:
            value /= metric_prefixes[si_prefix]
    if sig_figs:
        value = format_sig_figs(value, sig_figs)
    else:
        value = smart_round(value, 2)
        value = str(value)
    # Change answers like 2.0 to 2, as long as the .0 isn't intentionally there for sig-fig reasons
    if value.endswith('.0') and not sig_figs:
        value = value[:-2]
    if not no_suffix:
        # Suffix is the ending unit, ie, the ' kilometers' in '3 kilometers'
        if si_prefix:
            if si_prefix in metric_symbols:
                # 'k' → 'kilo'
                si_prefix = metric_symbols[si_prefix]
            suffix = ' ' + si_prefix + unit2['unit'][1:] if unit2['unit'].startswith(' ') else si_prefix + unit2['unit']
        else:
            suffix = unit2['unit']
        if value == '1' and suffix.endswith('s'):
            # '1 meters' → '1 meter'
            suffix = suffix[:-1]
            if suffix.endswith('ie'):
                # 'centurie' (this is the only unit with this issue)
                suffix = suffix[:-2] + 'y'
    else:
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
    # All valid input has at least 3 parts: value, unit1, and unit2
    # Can be broken by commas or spaces
    if ',' in user_input:
        user_input = user_input.split(',')
    else:
        user_input = user_input.split(' ')
    if len(user_input) < 3:
        return 'Incorrect format'
    value = user_input[0].strip().lower()
    unit1 = user_input[1].strip().lower()
    unit2 = user_input[2].strip().lower()
    sig_figs = False
    no_suffix = False
    output = ''
    while len(user_input) > 3:
        # If more than 3 parameters given, user may have indicated the output should be
        # given as an equation, have significant figures respected, or have its units omitted
        # These are the valid ways to do so - if they do anything else, return an error
        if user_input[-1].lower() in ['=', 'equal', 'equals', 'equation']:
            output = f'{value} {unit1} = '
            del user_input[-1]
        elif user_input[-1].lower() in ['sig', 'sigfigs', 'significant', 'significantfigures']:
            sig_figs = True
            del user_input[-1]
        elif user_input[-1].lower() in ['nounit', 'nounits', 'no', '!']:
            no_suffix = True
            del user_input[-1]
        else:
            return f"Incorrect format, unknown parameter '{user_input[-1]}'"
    # Ensure value is a valid, nicely formatted number
    value = format_val(value)
    if value == 'NaN':
        return 'NaN'
    output += converter(value, unit1, unit2, sig_figs, no_suffix)
    return output
