input_string = 'LGOABIAIRFRENPKEHSEGHEAIENIIMTSESNCAGTMACSNEOSDRUYNRTLYBOEYOYPTFRCHLTLTAAAAOEHLEVCGTESSEKRY'
alph = list('abcdefghijklmnopqrstuvwxyz'.upper())

def get_percentages(this_string):
    letter_count = [0]*26
    for letter in input_string:
        letter_count[alph.index(letter)] += 1
    for letter in alph:
        print(letter + ': ' + str(letter_count[alph.index(letter)]/len(input_string)))
        
get_percentages(input_string)