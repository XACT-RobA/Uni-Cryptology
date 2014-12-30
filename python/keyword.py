alph = list('abcdefghijklmnopqrstuvwxyz')

def encrypt(plaintext, keyword):
    plaintext = plaintext.lower()
    plaintext = ''.join(i for i in plaintext if i in alph)
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
    
this_plaintext = 'Mary had a little lamb and she also had a bear.'
encrypt(this_plaintext, 'test')