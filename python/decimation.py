import numpy as np
import math

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

def encrypt(plaintext, n):
    if not is_r_prime(n):
        print('Warning: n and 26 are not relatively prime')
    plaintext = plaintext.lower()
    plaintext = ''.join(i for i in plaintext if i in alph)
    ciphertext = ''
    for letter in plaintext:
        old_val = alph.index(letter)
        new_val = (old_val*n)%26
        new_letter = alph[new_val]
        ciphertext += new_letter.upper()
    print('Input: ' + plaintext)
    print('Output: ' + ciphertext)

def decrypt(ciphertext):
    ciphertext = ciphertext.lower()
    plaintext = ['']*25
    print('Ciphertext: ' + ciphertext.upper())
    for i in np.arange(1,25):
        if is_r_prime(i) == True:
            this_inverse = find_inverse(i)
            for letter in ciphertext:
                old_val = alph.index(letter)
                new_val = (old_val*this_inverse)%26
                new_letter = alph[new_val]
                plaintext[i] += new_letter
        if plaintext[i] != '':
            print('Key '+ str(i) + ': ' + plaintext[i])

this_plain_text = 'Hello world'
this_cipher_text = 'JUDDSGSHDP'
this_n = 5
#encrypt(this_plain_text, this_n)
decrypt(this_cipher_text)
