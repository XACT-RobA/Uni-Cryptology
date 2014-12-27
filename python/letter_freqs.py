input_string = 'LGOABIAIRFRENPKEHSEGHEAIENIIMTSESNCAGTMACSNEOSDRUYNRTLYBOEYOYPTFRCHLTLTAAAAOEHLEVCGTESSEKRY'
input_string_2 = 'V TJXCS CVRD PJX MJ MDCC ND TKDY PJX LQD CDLIVYZ BJ MKLM V HLY HLCC L MLEV'

alph = list('abcdefghijklmnopqrstuvwxyz'.upper())

input_string_2 = ''.join(i for i in input_string_2 if i in alph)

def get_percentages(this_string):
    letter_count = [0.0]*26
    for letter in this_string:
        letter_count[alph.index(letter)] += 1
    for letter in alph:
        print(letter + ': ' + str("%.3f" % ((letter_count[alph.index(letter)]/len(this_string))*100)) + '%')
        
get_percentages(input_string_2)