seq ="ATTGCCCCGAAT"
freq = []
alph = []

for i in seq:
    if i not in alph:
        alph.append(i)
        freq.append(1)
    elif i in alph:
        freq[alph.index(i)] = freq[alph.index(i)] + 1
        
print(alph)

for j in freq:
    print(j/len(seq))