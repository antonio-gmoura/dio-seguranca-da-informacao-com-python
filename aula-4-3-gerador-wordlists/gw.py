import itertools

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))
print(type(resultado))

for i in resultado:
    print(''.join(i))