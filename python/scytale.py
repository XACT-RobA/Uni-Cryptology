import numpy as np

this_ciphertext = 'LGOABIAIRFRENPKEHSEGHEAIENIIMTSESNCAGTMACSNEOSDRUYNRTLYBOEYOYPTFRCHLTLTAAAAOEHLEVCGTESSEKRY'
this_plaintext = 'Like many of the great generals of history, Caesar seems to have been sadly lacking in cryptographic subtlety.'
rod_width = 7

def decrypt(ciphertext):
    width_range = np.arange(1,((len(ciphertext)/4)+1))
    print('Input: ' + ciphertext)
    for width in width_range:
        this_split_chars = [ciphertext[0+i:width+i] for i in range(0, len(ciphertext), width)]
        this_line_array = [[None]]*width
        for x in range(len(this_line_array)):
            this_line_array[x] = []
        these_lines = [None]*width
        for j in range(len(this_split_chars)):
            for k in range(width):
                try:
                    this_line_array[k].append(this_split_chars[j][k])
                except:
                    pass
        for k in range(width):
            these_lines[k] = ''.join(this_line_array[k])
        this_string = ''
        for k in range(width):
            this_string += str(these_lines[k]).lower()
        print('width ' + str(width) + ': ' + this_string)
            
def encrypt(plaintext, width):
    plaintext = plaintext.lower()
    plaintext = ''.join(i for i in plaintext if i in 'abcdefghijklmnopqrstuvwxyz')
    line_width = len(plaintext)/width
    this_split_chars = [plaintext[0+i:line_width+i] for i in range(0, len(plaintext), line_width)]
    ciphertext = ''
    for i in range(line_width):
        for j in range(width):
            try:
                ciphertext += this_split_chars[j][i]
            except:
                pass
    ciphertext = ciphertext.upper()
    print('Input: ' + plaintext)
    print('Output: ' + ciphertext)

#decrypt(this_ciphertext)
encrypt(this_plaintext, rod_width)