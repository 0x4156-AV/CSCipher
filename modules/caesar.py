import collections
from string import ascii_lowercase

def find_key():
    number = len(string)
    array = []

    dict = collections.defaultdict(int)
    for character in string:
        dict[character] += 1

    for character in ascii_lowercase:
    	array.append((dict[character]/float(number)))

    num = array.index(max(array))
    key = (((num - 5) % 26) + 1)
    return key

def decrypt(n, ciphertext):
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

def caesar(string):
	key = str(find_key())
	decrypted = str(decrypt(key, string.lower()))
	print "Used key: " + key + "\n" + decrypted
	
caesar()
