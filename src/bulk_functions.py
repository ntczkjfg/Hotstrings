import random
import re

def blackboard_bold(user_input = None):
    """Convert input into blackboard bold"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    extra_dict = {'Sigma': '⅀', 'Gamma': 'ℾ', 'gamma': 'ℽ', 'Pi': 'ℿ', 'pi': 'ℼ'}
    for key in extra_dict:
        while key in user_input:
            user_input = user_input.replace(key, extra_dict[key])
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def bold(user_input = None):
    """Convert input into bold"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def boldcursive(user_input = None):
    """Convert input into bold cursive"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def bolditalic(user_input = None):
    """Convert input into bold italic"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def braille(user_input = None):
    """Convert input into braille"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    translation_dict = { ',': '⠂', ';': '⠆', ':': '⠒', '.': '⠲', '!': '⠖', '(': '⠶', ')': '⠶', '?': '⠦', '"': '⠦', '<': '⠦', '>': '⠴', '/': '⠌', "'": '⠄', '-': '⠤', ' ': '⠀',
                         '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑', '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',
                         'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
                         'A': '⠠⠁', 'B': '⠠⠃', 'C': '⠠⠉', 'D': '⠠⠙', 'E': '⠠⠑', 'F': '⠠⠋', 'G': '⠠⠛', 'H': '⠠⠓', 'I': '⠠⠊', 'J': '⠠⠚', 'K': '⠠⠅', 'L': '⠠⠇', 'M': '⠠⠍', 'N': '⠠⠝', 'O': '⠠⠕', 'P': '⠠⠏', 'Q': '⠠⠟', 'R': '⠠⠗', 'S': '⠠⠎', 'T': '⠠⠞', 'U': '⠠⠥', 'V': '⠠⠧', 'W': '⠠⠺', 'X': '⠠⠭', 'Y': '⠠⠽', 'Z': '⠠⠵' }
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def colors_to_hex(user_input = None):
    """Convert 'r, g, b' triplet (0-255 each) into hex color code"""
    if not user_input:
        return {'max': 20,
                'time': 20}
    user_input = user_input.replace(',', ' ').replace('  ', ' ').split(' ')
    if len(user_input) != 3:
        return
    try:
        R = hex(int(user_input[0]))[2:]
        G = hex(int(user_input[1]))[2:]
        B = hex(int(user_input[2]))[2:]
    except (ValueError, TypeError):
        return
    if len(R) == 1:
        R = '0' + R
    if len(G) == 1:
        G = '0' + G
    if len(B) == 1:
        B = '0' + B
    output = f'#{R}{G}{B}'.upper()
    return output

def cursive(user_input = None):
    """Convert input into cursive"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''𝒶𝒷𝒸𝒹𝔢𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def delete_macro(hotstrings, user_input = None):
    """
    Delete the specified macro.
    Use 'macros' to see all macros.
    Specify by hotkey or number.
    """
    if not user_input:
        return {'max': 500,
                'time': 90}
    if user_input == 'all':
        hotstrings.user_macros = {}
        output = 'Deleted all macros'
    elif user_input in hotstrings.user_macros:
        index = list(hotstrings.user_macros.keys()).index(user_input) + 1
        del hotstrings.user_macros[user_input]
        output = f'Deleted macro {index}: {user_input}'
    elif user_input.isdigit() and 1 <= (user_int := int(user_input)) <= len(hotstrings.user_macros):
        macro_to_delete = list(hotstrings.user_macros.keys())[user_int - 1]
        del hotstrings.user_macros[macro_to_delete]
        output = f'Deleted macro {user_input}: {macro_to_delete}'
    else:
        return 'Invalid macro'
    hotstrings.save_settings()
    hotstrings.create_hooks()
    return output

def flip(user_input = None):
    """Flips the input text upside-down"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre =  r'''&><}{][)(_!?.',^0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`⅋<>{}[]()‾¡¿˙,'v0ƖᄅƐㄣϛ9ㄥ86ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z,'''
    post = r'''⅋<>{}[]()‾¡¿˙,'v0ƖᄅƐㄣϛ9ㄥ86ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z,&><}{][)(_!?.',^0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    translation_dict['"'] = ',,'
    user_input = user_input[::-1]
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def flip_case(user_input = None):
    """Swaps the case of each character in the input"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def hearts():
    """Returns all the colored heart emojis in a random order"""
    hearts = ['💚', '🤎', '💙', '🧡', '🤍', '🖤', '❤️', '💛', '💜', '🩷', '🩶', '🩵']
    random.shuffle(hearts)
    return ''.join(hearts)

def hearts2():
    """Returns all of the heart emojis in a random order"""
    hearts = ['💚', '🤎', '💙', '🧡', '🤍', '🖤', '❤️', '💛', '💜', '💝', '💘', '💖', '💗', '💓', '💞', '💟', '❣', '💕', '🫀', '🩷', '🩶', '🩵']
    random.shuffle(hearts)
    return ''.join(hearts)

def hex_to_colors(user_input = None):
    """Converts a hex color code into an r, g, b triplet"""
    if not user_input:
        return {'max': 10,
                'time': 20}
    if len(user_input) != 6:
        return
    R = user_input[:2]
    G = user_input[2:4]
    B = user_input[4:]
    try:
        R = int(R, 16)
        G = int(G, 16)
        B = int(B, 16)
    except ValueError:
        return
    output = f'{R}, {G}, {B}'
    return output

def hide(user_input = None):
    """Converts input into hidden zero-width characters"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()~-_=+[{]}\|;:'",<.>/?'''
    post = r'''󠁡󠁢󠁣󠁤󠁥󠁦󠁧󠁨󠁩󠁪󠁫󠁬󠁭󠁮󠁯󠁰󠁱󠁲󠁳󠁴󠁵󠁶󠁷󠁸󠁹󠁺󠁁󠁂󠁃󠁄󠁅󠁆󠁇󠁈󠁉󠁊󠁋󠁌󠁍󠁎󠁏󠁐󠁑󠁒󠁓󠁔󠁕󠁖󠁗󠁘󠁙󠁚󠀰󠀱󠀲󠀳󠀴󠀵󠀶󠀷󠀸󠀹󠀡󠁀󠀣󠀤󠀥󠁞󠀦󠀪󠀨󠀩󠁾󠀭󠁟󠀽󠀫󠁛󠁻󠁝󠁽󠁜󠁼󠀻󠀺󠀧󠀢󠀬󠀼󠀮󠀾󠀯󠀿'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def italic(user_input = None):
    """Converts input into italic"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def lookalike(user_input = None):
    """Converts input into similar looking but different output"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyz:;<>=@!$%&()*+-ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''аᖯс𝖽е𝖿𝗀һіј𝗄ӏｍ𝗇ор𝗊𝗋ѕ𝗍𝗎ν𝗐хуꮓ։;˂˃᐀＠ǃ＄％＆❨❩*᛭˗ΑΒСᎠΕꓝᏀΗlЈΚᒪΜΝΟΡⵕꓣЅΤꓴᏙᎳΧΥΖ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def lower(user_input = None):
    """Converts input into lowercase"""
    # Because we all type a paragraph with caps on without noticing sometimes
    if not user_input:
        return {'max': 500,
                'time': 90}
    output = user_input.lower()
    return output

def lower2(user_input = None):
    """Converts input into lowercase, except first words in each sentence"""
    # Because we all type a paragraph with caps on without noticing sometimes
    if not user_input:
        return {'max': 500,
                'time': 90}
    output = user_input.lower()
    output = output[0].upper() + output[1:]
    output = re.sub(r'([.!?] *)([a-z])', lambda m: m.group(1) + m.group(2).upper(), output)
    output = output.replace(' i ', ' I ').replace(" i'", " I'")
    return output

def mock(user_input = None):
    """Randomizes the case of each character in the input"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    output = []
    for char in user_input:
        if random.random() < 0.5:
            output.append(char.upper())
        else:
            output.append(char.lower())
    output = ''.join(output)
    return output

def mock2(user_input = None):
    """Alternates the case of each character in the input, starting with lower"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    output = []
    UPPER = False
    for char in user_input:
        if UPPER:
            output.append(char.upper())
            UPPER = False
        else:
            output.append(char.lower())
            UPPER = True
    output = ''.join(output)
    return output

def mono(user_input = None):
    """Converts input into a monowidth character set"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!|"#$%&'()*+,-./:;<=>?@[\]^_`{}~'''
    post = r'''ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ　ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ０１２３４５６７８９！｜＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｝～'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def morse(user_input = None):
    """Converts input into morse code using proper morse unicode symbols"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    translation_dict = { '.': '•−•−•− ', ',':'−−••−− ', '?': '••−−•• ', "'": '•−−−−• ', '/': '−••−• ', '(': '−•−−• ', ')': '−•−−•− ', '&': '•−••• ', ':': '−−−••• ', '=': '−•••− ', '+': '•−•−• ', '-': '−••••− ', '"': '•−••−• ', '@': '•−−•−• ', '$': '•••−••− ', '_': '••−−•− ', ';': '−•−•−• ', '!': '−•−•−− ', ' ': '  ',
                         'A': '•− ', 'B': '−••• ', 'C': '−•−• ', 'D': '−•• ', 'E': '• ', 'F': '••−• ', 'G': '−−• ', 'H': '•••• ', 'I': '•• ', 'J': '•−−− ', 'K': '−•− ', 'L': '•−•• ', 'M': '−− ', 'N': '−• ', 'O': '−−− ', 'P': '•−−• ', 'Q': '−−•− ', 'R': '•−• ', 'S': '••• ', 'T': '− ', 'U': '••− ', 'V': '•••− ', 'W': '•−− ', 'X': '−••− ', 'Y': '−•−− ', 'Z': '−−•• ',
                         '1': '•−−−− ', '2': '••−−− ', '3': '•••−− ', '4': '••••− ', '5': '••••• ', '6': '−•••• ', '7': '−−••• ', '8': '−−−•• ', '9': '−−−−• ', '0': '−−−−− ' }
    output = ''.join(translation_dict.get(char.upper(), char) for char in user_input)
    return output

def morse2(user_input = None):
    """Converts input into morse code using periods and hyphens"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    translation_dict = { '.': '.-.-.- ', ',':'--..-- ', '?': '..--.. ', "'": '.----. ', '/': '-..-. ', '(': '-.--. ', ')': '-.--.- ', '&': '.-... ', ':': '---... ', '=': '-...- ', '+': '.-.-. ', '-': '-....- ', '"': '.-..-. ', '@': '.--.-. ', '$': '...-..- ', '_': '..--.- ', ';': '-.-.-. ', '!': '-.-.-- ', ' ': '/ ',
                         'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
                         '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ' }
    output = ''.join(translation_dict.get(char.upper(), char) for char in user_input)
    return output

def python(user_input = None):
    """Runs input as a Python program, intercepts any print statements and returns them"""
    if not user_input:
        return {'max': 2000,
                'time': 180}
    # Intentional mutable default!
    def custom_print(text, output = [], outputting = False):
        if outputting:
            return '\n'.join(output)
        output.append(str(text))
    try:
        exec(user_input, {'print': custom_print}, {})
    except Exception as e:
        output = f'Encountered error while executing: {repr(e)}'
    else:
        output = custom_print('', outputting = True)
    return output

def rot13(user_input = None):
    """Applies the rot13 shift cypher to input"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def rune(user_input = None):
    """Converts input into futhark runes"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''fuarkgwhnijæpzstbemlodv'''
    post = r'''ᚠᚢᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛟᛞᚠ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char.lower(), char) for char in user_input)
    return output

def rune2(user_input = None):
    """Converts input into elder futhark runes"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''fuvwyoøærkghnieastdbpml'''
    post = r'''ᚠᚢᚢᚢᚢᚢᚢᚬᚱᚴᚴᚼᚾᛁᛅᛅᛋᛏᛏᛒᛒᛘᛚ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char.lower(), char) for char in user_input)
    return output

def smallcaps(user_input = None):
    """Converts input into smallcaps"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char.upper(), char) for char in user_input)
    return output

def smallcaps2(user_input = None):
    """Converts input so the first letter of each word is regular caps, and all the other letters are smallcaps"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    post = r'''ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    words = user_input.split(' ')
    for i in range(len(words)):
        if len(words[i]) > 0:
            words[i] = words[i][0].upper() + ''.join(translation_dict.get(char.upper(), char) for char in words[i][1:])
    output = ' '.join(words)
    return output

def subscript(user_input = None):
    """Converts input into subscripts"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''+-=()0123456789aehijklmnoprstuvx'''
    post = r'''₊₋₌₍₍₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def superscript(user_input = None):
    """Converts input into superscripts"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''+-=()0123456789abcdefghijklmnoprstuvwxyzABDEGHIJKLMNOPRTUVW'''
    post = r'''⁺⁻⁼⁽⁾⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂ'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def unbraille(user_input = None):
    """Converts input from braille to plain text"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    translation_dict = {'⠂': ',', '⠆': ';', '⠒': ':', '⠲': '.', '⠖': '!', '⠶': ')', '⠦': '<', '⠴': '>', '⠌': '/', '⠄': "'", '⠤': '-', '⠀': ' ',
                        '⠁': 'a', '⠃': 'b', '⠉': 'c', '⠙': 'd', '⠑': 'e', '⠋': 'f', '⠛': 'g', '⠓': 'h', '⠊': 'i', '⠚': 'j', '⠅': 'k', '⠇': 'l', '⠍': 'm', '⠝': 'n', '⠕': 'o', '⠏': 'p', '⠟': 'q', '⠗': 'r', '⠎': 's', '⠞': 't', '⠥': 'u', '⠧': 'v', '⠺': 'w', '⠭': 'x', '⠽': 'y', '⠵': 'z'}
    numbers_dict = { '⠼⠁': '1', '⠼⠃': '2', '⠼⠉': '3', '⠼⠙': '4', '⠼⠑': '5', '⠼⠋': '6', '⠼⠛': '7', '⠼⠓': '8', '⠼⠊': '9', '⠼⠚': '0' }
    for key in numbers_dict:
        while key in user_input:
            user_input = user_input.replace(key, numbers_dict[key])
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    while '⠠' in output:
        index = output.index('⠠')
        output = output[:index] + output[index + 1].upper() + output[index + 2:]
    return output

def underline(user_input = None):
    """Underlines the input"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    output = ''.join(['͟'] + [char + '͟' for char in user_input])
    return output

def unhide(user_input = None):
    """Undoes hide(), converts hidden message back to plain text"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''󠁡󠁢󠁣󠁤󠁥󠁦󠁧󠁨󠁩󠁪󠁫󠁬󠁭󠁮󠁯󠁰󠁱󠁲󠁳󠁴󠁵󠁶󠁷󠁸󠁹󠁺󠁁󠁂󠁃󠁄󠁅󠁆󠁇󠁈󠁉󠁊󠁋󠁌󠁍󠁎󠁏󠁐󠁑󠁒󠁓󠁔󠁕󠁖󠁗󠁘󠁙󠁚󠀰󠀱󠀲󠀳󠀴󠀵󠀶󠀷󠀸󠀹󠀡󠁀󠀣󠀤󠀥󠁞󠀦󠀪󠀨󠀩󠁾󠀭󠁟󠀽󠀫󠁛󠁻󠁝󠁽󠁜󠁼󠀻󠀺󠀧󠀢󠀬󠀼󠀮󠀾󠀯󠀿'''
    post = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()~-_=+[{]}\|;:'",<.>/?'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def unicode(user_input = None):
    """Prints the unicode character matching the provided codepoint"""
    if not user_input:
        return {'max': 10,
                'time': 20}
    try:
        codepoint = int(user_input, 16)
        output = chr(codepoint)
    except ValueError:
        return
    return output

def unmorse(user_input = None):
    """Converts input from morse code to plain text"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    # Dict is ordered by length of keys, from longest to shortest
    # Has some bookkeeping items at the start and end to fit the different ways morse can be typed to the rest of the dict
    translation_dict = { '.': '•', '-': '−', '_': '−', '  ': '{space}', ' ': ' ', '/': ' ',
                         '•••−••− ': '$', '•−•−•− ': '.', '−−••−− ': ',', '••−−•• ': '?', '•−−−−• ': "'", '−•−−•− ': ')', '−−−••• ': ':', '−••••− ': '-', '•−••−• ': '"', '•−−•−• ': '@', '••−−•− ': '_', '−•−•−• ': ';', '−•−•−− ': '!', '−••−• ': '/', '−•−−• ': '(', '•−••• ': '&', '−•••− ': '=', '•−•−• ': '+', '•−−−− ': '1', '••−−− ': '2', '•••−− ': '3', '••••− ': '4', '••••• ': '5', '−•••• ': '6', '−−••• ': '7', '−−−•• ': '8', '−−−−• ': '9', '−−−−− ': '0', '−••• ': 'b', '−•−• ': 'c', '••−• ': 'f', '•••• ': 'h', '•−−− ': 'j', '•−•• ': 'l', '•−−• ': 'p', '−−•− ': 'q', '•••− ': 'v', '−••− ': 'x', '−•−− ': 'y', '−−•• ': 'z', '−•• ': 'd', '−−• ': 'g', '−•− ': 'k', '−−− ': 'o', '•−• ': 'r', '••• ': 's', '••− ': 'u', '•−− ': 'w', '•− ': 'a', '•• ': 'i', '−− ': 'm', '−• ': 'n', '  ': ' ', '• ': 'e', '− ': 't',
                         ' ': ' ', '{space}': ' ' }
    output = user_input
    if output[-1] != ' ' and output[-1] != ' ':
        output = output + ' '
    for key in translation_dict:
        output = output.replace(key, translation_dict[key].upper())
    return output

def unrune(user_input = None):
    """Converts input from futhark runes to plain text"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''ᚠᚢᛞᛉᛒᛃᚨᚹᚷæᚱᚲᚺᚾᛁᛖᛊᛏᛈᛗᛚᛟ'''
    post = r'''fudzbjawgᛇrkhniestpmlo'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def unrune2(user_input = None):
    """Converts input from elder futhark runes to plain text"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre = r'''ᚠᚢᚬᚱᚴᚼᚾᛁᛅᛋᛏᛒᛘᛚ'''
    post = r'''foærkhniestpml'''
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output
