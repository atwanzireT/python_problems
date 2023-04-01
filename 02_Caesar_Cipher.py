# Caesar Cipher
import string


# l = "abcdef"
# n = 4
# print(str.maketrans(l, l[n:] + l[:n]))
def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase

    # shifting the characters
    mask = letters[shift_num:] + letters[:shift_num]

    # mapping characters to the cipher
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


print(caesar("ifmmp"))
