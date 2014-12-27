import numpy as np

alph = list('abcdefghijklmnopqrstuvwxyz')

def get_factors(n):
    factors = []
    i = 2.0
    while i <= n:
        if n%i == 0:
            factors.append(i)
        i += 1.0
    return factors

def is_r_prime(n):
    factors_n = get_factors(n)
    factors_26 = get_factors(26)
    rel_prime = True
    for factor in factors_n:
        if factor in factors_26:
            rel_prime = False
            break
    return rel_prime

def find_inverse(n):
    this_inverse = 0
    for i in range(26):
        if (n*i)%26 == 1:
            this_inverse = i
            break
    if this_inverse == 0:
        pass
    else:
        return this_inverse

def encrypt(plaintext, a, b):
    if not is_r_prime(a):
        print('Warning: a and 26 are not relatively prime')
    plaintext = plaintext.lower()
    plaintext = ''.join(i for i in plaintext if i in alph)
    ciphertext = ''
    for letter in plaintext:
        old_val = alph.index(letter)
        new_val = ((old_val*a)+b)%26
        new_letter = alph[new_val]
        ciphertext += new_letter.upper()
    print('Input: ' + plaintext)
    print('Output: ' + ciphertext)
    
def decrypt(ciphertext, a, b):
    a_inv = find_inverse(a)
    plaintext = ''
    print('Ciphertext: ' + ciphertext)
    ciphertext = ciphertext.lower()
    for letter in ciphertext:
        old_val = alph.index(letter)
        new_val = ((old_val-b)*this_inverse)%26
        new_letter = alph[new_val]
        plaintext += new_letter
    print('Input: ' + ciphertext)
    print('Output: ' + plaintext)
    
def decrypt_trial(ciphertext):
    print('Ciphertext: ' + ciphertext)
    ciphertext = ciphertext.lower()
    plaintext = [['']*26]*26
    for a in np.arange(1,26):
        if is_r_prime(a):
            this_inverse = find_inverse(a)
            for b in np.arange(1,27):
                this_plaintext = ''
                for letter in ciphertext:
                    old_val = alph.index(letter)
                    new_val = ((old_val-b)*this_inverse)%26
                    new_letter = alph[new_val]
                    this_plaintext += new_letter
                plaintext[a-1][b-1] = this_plaintext
                print('A '+ str(a) + ', B: ' + str(b) + ': ' + plaintext[a-1][b-1])

ciphertext = 'YJYN CDYN XDYO KYX XG UWFFBY EMDGGB EGUY MDWBFLYN LYUAWN QNEQLY CDYXDYL EANXA MBAQE YVWEXE'
this_ciphertext = ''.join(i for i in ciphertext.lower() if i in alph)
#print(this_ciphertext)

decrypt_trial(this_ciphertext)