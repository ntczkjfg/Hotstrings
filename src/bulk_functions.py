import random
import re
from PyQt6.QtWidgets import QFileDialog

def base64(user_input = None):
    """Converts input to base64"""
    if not user_input:
        return {'max': 5000,
                'time': 90}
    b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bits = ''.join(f"{ord(c):08b}" for c in user_input)
    while len(bits) % 6 != 0:
        bits += '0'
    output = ''
    for i in range(0, len(bits), 6):
        chunk = bits[i:i+6]
        output += b64[int(chunk, 2)]
    while len(output) % 4 != 0:
        output += '='
    return output

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
        hotstrings.user_macros = []
        output = 'Deleted all macros'
    elif user_input.isdigit() and 1 <= (user_int := int(user_input)) <= len(hotstrings.user_macros):
        output = f'Deleted macro {user_input}: {hotstrings.user_macros[user_int-1][0]}'
        del hotstrings.user_macros[user_int - 1]
    else:
        return 'Invalid macro'
    hotstrings.save_settings()
    hotstrings.create_hooks()
    return output

def dvorak(user_input = None):
    """Converts input between the Qwerty and Dvorak keyboard layouts"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre  = r"""1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?"""
    post = r"""1234567890[]',.pyfgcrl/=\aoeuidhtns-;qjkxbmwvz!@#$%^&*(){}"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ"""
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def emojify(user_input = None):
    """Converts input into emojis"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    user_input = user_input.replace('?!', '⁉️').replace('!!', '‼️').replace('10', '🔟')
    translation_dict = {
        'a': '​🇦', 'b': '​🇧', 'c': '​🇨', 'd': '​🇩', 'e': '​🇪', 'f': '​🇫',
        'g': '​🇬', 'h': '​🇭', 'i': '​🇮', 'j': '​🇯', 'k': '​🇰', 'l': '​🇱',
        'm': '​🇲', 'n': '​🇳', 'o': '​🇴', 'p': '​🇵', 'q': '​🇶', 'r': '​🇷',
        's': '​🇸', 't': '​🇹', 'u': '​🇺', 'v': '​🇻', 'w': '​🇼', 'x': '​🇽',
        'y': '​🇾', 'z': '​🇿',
        'A': '​🇦', 'B': '​🇧', 'C': '​🇨', 'D': '​🇩', 'E': '​🇪', 'F': '​🇫',
        'G': '​🇬', 'H': '​🇭', 'I': '​🇮', 'J': '​🇯', 'K': '​🇰', 'L': '​🇱',
        'M': '​🇲', 'N': '​🇳', 'O': '​🇴', 'P': '​🇵', 'Q': '​🇶', 'R': '​🇷',
        'S': '​🇸', 'T': '​🇹', 'U': '​🇺', 'V': '​🇻', 'W': '​🇼', 'X': '​🇽',
        'Y': '​🇾', 'Z': '​🇿',
        '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
        '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣',
        '!': '❗', '!!': '‼️', '?': '❓', '!?': '⁉️',
        '*': '*️⃣', '#': '#️⃣'}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def flip(user_input = None):
    """Flips the input text upside-down"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre  = r"/\&><}{][)(_!?.',^0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`⅋‾¡¿˙ƖᄅƐㄣϛㄥɐɔǝɟƃɥᴉɾʞɯɹʇʌʍʎ∀ꓭƆƎℲפſ˥Ԁ┴∩Λ⅄"
    post = r"/\⅋<>{}[]()‾¡¿˙,'v0ƖᄅƐㄣϛ9ㄥ86ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀ꓭƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z,&_!?.123457acefghijkmrtvwyABCEFGJLPTUVY"
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
    pre  = r'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
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

def program_hotstring_1(hotstrings, user_input = None):
    """
    Creates a macro to open a specified file
    """
    if not user_input:
        return {'max': 500,
                'time': 90}
    if (user_input in hotstrings.hotstrings
        or user_input in hotstrings.Hotstrings
        or user_input in hotstrings.callables
        or user_input in hotstrings.user_macros):
        return f'Name "{user_input}" already in use'
    hotstrings.program_hotstring_signal.emit(hotstrings, user_input)

def program_hotstring_2(hotstrings, user_input):
    file_name, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*)")
    if file_name:
        hotstrings.program_hotstrings[user_input] = file_name
        hotstrings.save_settings()
        hotstrings.write('Successfully created')
    else:
        hotstrings.write('Aborted')

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

def qwerty(user_input = None):
    """Converts input between the Dvorak and Qwerty keyboard layouts"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    pre  = r"""1234567890[]',.pyfgcrl/=\aoeuidhtns-;qjkxbmwvz!@#$%^&*(){}"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ"""
    post = r"""1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?"""
    translation_dict = {pre[i]: post[i] for i in range(len(pre))}
    output = ''.join(translation_dict.get(char, char) for char in user_input)
    return output

def random_heart():
    """Returns a randomly colored heart"""
    hearts = ['💚', '🤎', '💙', '🧡', '🤍', '🖤', '❤️', '💛', '💜', '🩷', '🩶', '🩵']
    return random.choice(hearts)

def roman(user_input = None):
    """Converts input to Roman Numerals"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    negative = False
    try:
        num = int(user_input)
        if num < 0:
            num *= -1
            negative = True
        if num == 0 or num >= 4000:
            return user_input
        num = str(num)
    except ValueError:
        return user_input
    ones = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV',
            '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
    tens = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL',
            '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
    hundreds = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD',
                '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
    thousands = {'1': 'M', '2': 'MM', '3': 'MMM'}
    dicts = [0, ones, tens, hundreds, thousands]
    i = 1
    output = ''
    while i <= len(num):
        output = dicts[i][num[-i]] + output
        i += 1
    if negative:
        output = '-' + output
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

def unbase64(user_input = None):
    """Converts input from base64"""
    if not user_input:
        return {'max': 5000,
                'time': 90}
    b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    user_input = user_input.rstrip('=')
    if not (set(user_input) <= set(b64)):
        return 'Invalid base64: Contains invalid characters'
    bits = ''.join(f'{b64.index(char):06b}' for char in user_input)
    output = ''
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        output += chr(int(byte, 2))
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

def unroman(user_input = None):
    """Converts from Roman Numeral to decimal"""
    if not user_input:
        return {'max': 500,
                'time': 90}
    negative = False
    if user_input.startswith('-'):
        user_input = user_input[1:]
        negative = True
    if not user_input:
        return 'Not a valid Roman Numeral'
    user_input = user_input.upper()
    if not (set(user_input) <= set('IVXLCDM')):
        return 'Not a valid Roman Numeral'
    thousands = {'MMM': 3000, 'MM': 2000, 'M': 1000}
    hundreds  = {'DCCC': 800, 'CCC': 300, 'DCC': 700, 'CC': 200, 'CD': 400, 'DC': 600, 'CM': 900, 'C': 100, 'D': 500}
    tens      = {'LXXX': 80, 'XXX': 30, 'LXX': 70, 'XX': 20, 'XL': 40, 'LX': 60, 'XC': 90, 'X': 10, 'L': 50}
    ones      = {'VIII': 8, 'III': 3, 'VII': 7, 'II': 2, 'IV': 4, 'VI': 6, 'IX': 9, 'I': 1, 'V': 5}
    dicts = [thousands, hundreds, tens, ones]
    output = 0
    for translation_dict in dicts:
        for key, value in translation_dict.items():
            if user_input.startswith(key):
                output += value
                user_input = user_input[len(key):]
                break
    if user_input:
        return 'Not a valid Roman Numeral'
    if negative:
        output *= -1
    return str(output)

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
