# Функції для кодування рядків в base64

def intTosixBits(value):
    binValue = "{0:b}".format(int(value))
    return (6 - len(binValue)) * '0' + binValue


def charTo16Bits(_char):
    binValue = "{0:b}".format(ord(_char))
    return (16 - len(binValue)) * '0' + binValue

def textToBits(string):
    bitsArray = ""
    for symbol in string:
        bitsArray += charTo16Bits(symbol)
    return bitsArray

def initialTable():
    global base64Table
    base64Table = []
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i in range(0, 64):
        base64Table.append({symbols[i]: intTosixBits(i)})

def base64(string):
    bitsArray = textToBits(string)
    initialTable()
    T = True
    base64String = ""
    while (T):
        base64buffer = ""
        if (len(bitsArray) == 0):
            break
        if (len(bitsArray) < 24):
            if (len(bitsArray) == 16):
                bitsArray += "00"
                for i in range(3):
                    bit = bitsArray[:6]
                    for dict in base64Table:
                        if (list(dict.values())[0] == bit):
                            base64buffer += list(dict.keys())[0]
                    bitsArray = bitsArray[6:]
                base64buffer += "="
                base64String += base64buffer
                break
            if (len(bitsArray) == 8):
                bitsArray += "0000"
                for i in range(2):
                    bit = bitsArray[:6]
                    for dict in base64Table:
                        if (list(dict.values())[0] == bit):
                            base64buffer += list(dict.keys())[0]
                    bitsArray = bitsArray[6:]
                base64buffer += "=="
                base64String += base64buffer
                break
        else:
            buffer = bitsArray[:24]
            for i in range(4):
                bit = buffer[:6]
                for dict in base64Table:
                    if (list(dict.values())[0] == bit):
                        base64buffer += list(dict.keys())[0]
                buffer = buffer[6:]
            bitsArray = bitsArray[24:]
        base64String += base64buffer
    return base64String