alph = list('abcdefghijklmnopqrstuvwxyz')

def plain(plaintext):
    plaintext = plaintext.lower()
    plaintext = ''.join(i for i in plaintext if i in alph)
    return plaintext

def encrypt(plaintext, keyword):
    plaintext = plain(plaintext)
    cipherbet = []
    for keyletter in keyword:
        if keyletter not in cipherbet:
            cipherbet.append(keyletter)
    for letter in alph:
        if letter not in cipherbet:
            cipherbet.append(letter)
    ciphertext = ''
    for letter in plaintext:
        old_val = alph.index(letter)
        new_letter = cipherbet[old_val]
        ciphertext += new_letter
    print('Input: ' + plaintext)
    print('Output: ' + ciphertext.upper())
    
def encrypt_transposed(plaintext, keyword):
    plaintext = plain(plaintext)
    keyword_no_repeat = ''
    for letter in keyword:
        if letter not in keyword_no_repeat:
            keyword_no_repeat += letter
    keyword = keyword_no_repeat
    width = len(keyword)
    height = (26/width)+1
    cipherbet = []
    for keyletter in keyword:
        if keyletter not in cipherbet:
            cipherbet.append(keyletter)
    for letter in alph:
        if letter not in cipherbet:
            cipherbet.append(letter)
    cipherbet_array = [cipherbet[0+i:width+i] for i in range(0, len(cipherbet), width)]
    cipher_chunk_array = ['']*width
    for cipherbet_chunk in cipherbet_array:
        j = 0
        for i in range(len(cipherbet_chunk)):
            cipher_chunk_array[i] += cipherbet_chunk[i]
        j += 1
    cipherbet = ''
    for i in range(len(cipher_chunk_array)):
        cipherbet += cipher_chunk_array[i]
    cipherbet_string = cipherbet
    cipherbet = list(cipherbet)
    print('Alphabet: ' + cipherbet_string)
    ciphertext = ''
    for letter in plaintext:
        old_val = alph.index(letter)
        new_letter = cipherbet[old_val]
        ciphertext += new_letter
    print('Input: ' + plaintext)
    print('Output: ' + ciphertext.upper())

this_plaintext = 'Mary had a little lamb and she also had a bear.'
keyword = 'nursery'
#encrypt(this_plaintext, keyword)
encrypt_transposed(this_plaintext, keyword)