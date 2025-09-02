import random, string, sys

def validateInput(argv):
    if len(argv) != 2:
        print("Usage: ./solver.py {encodedText}")
        sys.exit(1)

def toXor(text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % key_length]))
    return encrypted_text

def hexXorEncoder(text, key):
    return toXor(text, key).encode().hex()

def hexXorDecoder(textEncoded, key):
    return toXor(bytes.fromhex(textEncoded).decode(), key)

def findLastDigit(textEncoded, key):
    allDigits = string.ascii_letters + string.digits
    try:
        i = 0
        while(True):
            newKey = key + allDigits[i]
            print(f"\nTRYING KEY: {newKey}")
            print(f"FLAG: {hexXorDecoder(textEncoded, newKey)}")

            i+=1
    except:
        return print("\nFinished all digits")

def findKey(textEncoded):
    cont = True
    while(cont):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        result = hexXorDecoder(textEncoded, key)
        if(result[0] == "T" and result[1] == "H" and result[2] == "M" and result[3] == "{"):
            print(f"FIRST 4 DIGITS KEY: {key}")
            print(f"FLAG: {result}")
            print("\n\nSTARTING TO GUESS THE OTHERS DIGITS")
            findLastDigit(textEncoded, key)
            cont = False
            break



validateInput(sys.argv)
encoded = sys.argv[1]
findKey(encoded)


