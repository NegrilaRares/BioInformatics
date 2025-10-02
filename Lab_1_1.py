seq ="ATTGCCCCGAAT"
alph = []

for i in seq:
   if i  not in alph:
       alph.append(i)
       
print(alph)