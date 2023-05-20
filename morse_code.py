
code = {'a':'.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                'i': '..', 'j': '.---','k': '-.-', 'l': '.-..',
                'm': '--', 'n': '-.', 'o': '---', 'p': '--.-',
                'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
                'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                'y': '-.--', 'z': '--..', ' ': '\\',
                '0': '-----', '1': '.----', '2': '..---', 
                '3': '...--', '4': '...-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..',
                '9': '----.'}


def encode(msg: str) -> str:
    
    msg = msg.lower()
    encoded_msg = []

    for char in msg:
        encoded_msg.append(code[char])

    return " ".join(encoded_msg)


def decode(msg: str) -> str:
    
    msg = msg.split(" ")
    decoded_msg = []

    for code in msg:
        decoded_msg.append(get_key_from_value(code))

    try:
        return "".join(decoded_msg).title()
    except:
        return "Enter a valid code"
        

def get_key_from_value(value: str) -> str:
    
    for key, val in code.items():
        if val == value:
            return key  
    return None


while True:
    msg = input("Enter the message: ")
    if msg[0].isalpha() or msg[0].isnumeric:
        encoded_msg = encode(msg)
        print(encoded_msg)
    else:
        decoded_msg = decode(msg)
        print(decoded_msg)
