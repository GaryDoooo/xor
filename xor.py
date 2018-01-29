import hashlib
#mysha1 = hashlib.sha1()
#>>> mysha1.update("my_url")
#>>> print mysha1.hexdigest()


def xor(orig, key):
    key = key.encode('utf-8')
    keyhash = hashlib.sha1()
    keyhash.update(key)
    key = keyhash.hexdigest()
    # str(hex(abs(hash(heyhash.))))[2:]
    len_key = len(key)
    len_orig = len(orig)
    key = key * round(len_orig / len_key + 1)
    result = ''
    for i in range(len_orig):
        result = result + str(hex(int(key[i], 16) ^ int(orig[i], 16)))[2:]
    #  result = '0' * len_orig
    #  for i in range(round(len_orig / len_key)):
        #  seg = orig[i * len_key: (i + 1) * len_key]
        #  print(key, seg)
        #  for j in range(len_key):
        #  result = (result[:i * len_key + j] +
        #  str(hex(int(key[j], 16) ^ int(seg[j], 16)))[2:] +
        #  result[i * len_key + j + 1:])
    return result

#  def sxor(s1, s2):
    #  # convert strings to a list of character pair tuples
    #  # go through each tuple, converting them to ASCII code (ord)
    #  # perform exclusive or on the ASCII code
    #  # then convert the result back to ASCII (chr)
    #  # merge the resulting array of characters as a string
    #  return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
#


def main():
    orig = input("input the string want to convert: ")
    key = input("input the convert key: ")
    # print(sxor(orig, key))
    print("\n" + xor(orig, key) + "\n")


if __name__ == "__main__":
    main()
