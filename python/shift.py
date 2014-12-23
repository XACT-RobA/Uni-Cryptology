alph = list('abcdefghijklmnopqrstuvwxyz')

def encrypt(plaintext, shift_size):
    plaintext = plaintext.lower()
    plaintext = ''.join(i for i in plaintext if i in alph)
    ciphertext = ''
    for letter in plaintext:
        old_val = alph.index(letter)
        new_val = (old_val+shift_size)%26
        ciphertext += alph[new_val]
    ciphertext = ciphertext.upper()
    print('Input: ' + plaintext)
    print('Output: ' + ciphertext)
    
def decrypt(ciphertext):
    ciphertext = ciphertext.lower()
    for shift_size in range(26):
        plaintext = ''
        for letter in ciphertext:
            old_val = alph.index(letter)
            new_val = (old_val-shift_size)%26
            plaintext += alph[new_val]
        print('Shift size ' + str(shift_size) + ': ' + plaintext)
    
encrypt('The rain in spain falls mainly on the plane', 3)
#decrypt('WKHUDLQLQVSDLQIDOOVPDLQOBRQWKHSODQH')