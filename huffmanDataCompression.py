
def frequency(text):
    freqs = {}
    for ch in text:
        freqs[ch] = freqs.get(ch,0)+1
    return freqs

text ='aaabccdeeeeeffg' 
freq_dict = frequency(text)

def sortFreq(freq):
    letters = freq.keys()
    tuple_list = []
    for letter in letters:
        tuple_list.append((freq[letter],letter))
    tuple_list.sort()
    return tuple_list

tuple_list = sortFreq(freq_dict)

def buildTree(tuple_list):
    while len(tuple_list) >1:
        leastTwo_tuple = tuple(tuple_list[:2])                      # get the 2 to combine
        theRest_list = tuple_list[2:]                               # all the others
        combFreq = leastTwo_tuple[0][0] + leastTwo_tuple[1][0]
        tuple_list = theRest_list + [(combFreq,leastTwo_tuple)]
        tuple_list.sort(key=lambda t: t[0])
    return tuple_list[0]

tree = buildTree(tuple_list)
print(tree)

def trimTree (tree):
    # Trim the freq counters off, leaving just the letters
    p = tree[1]                                     # ignore freq count in [0]
    if type(p) ==type(""):                          # if just a leaf, return it
        return p
    else:
        return (trimTree(p[0]), trimTree(p[1]))     # trim left and right and recombine

trim = trimTree(tree)
print(trim)


codes = {}
def assignCodes(node, pat=''):
    global codes
    if type(node) == type(""):
        codes[node] = pat               # A leaf. set its code
    else:
        assignCodes(node[0], pat+'0')   # Branch point, Do the left branch
        assignCodes(node[1], pat+'1')   # then do the right branch.

#print(trim)
assignCodes(trim)
#print(codes)

def encode(text):
    global codes
    output = ''
    for word in text:
        output += codes[word]
    return output

encoded_text = encode(text)

print(text)
print(encoded_text)

def decode(tree, bitcode):
    output = ''
    p = tree
    for bit in bitcode:
        if bit =='0':
            p = p[0]                # Head up ht left branch
        else:
            p = p[1]                # or up the right branch
        if type(p) == type(''): 
            output +=p              # found a character. Add to output
            p = trim                # and restart for next character
    return output

def decode_with_codeDict(bitcode, code_dict):
    decode_dict = {}
    for key, value in code_dict.items():
        decode_dict[value]= key 
    output = ''
    byte=''
    for bit in bitcode:
        byte += bit
        if byte in decode_dict:
            output += decode_dict[byte]
            byte=''
    return output

print(decode(trim,encoded_text))
print('---')
print(decode_with_codeDict(encoded_text, codes))