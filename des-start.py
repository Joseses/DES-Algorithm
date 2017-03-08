import binascii

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

ROTATION_TABLE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

for itemList in PC_1:
    print(itemList)


def keytobinary(key):
    """Converts a hexadecimal key to its binary representation"""
    binary_array = []
    counter = 0
    binary_string = ""
    for letter in key:
        counter += 1
        binary_string += bin(int(letter, 16))[2:].zfill(4)
        if counter == 2:
            binary_array.append(binary_string)
            counter = 0
            binary_string = ""
    return binary_array


def permutation56bit(key):
    """"Performs a 56-bit permutation"""
    permutedkey = ""
    return permutedkey


print(keytobinary("133457799BBCDFF1"))
