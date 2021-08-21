import hashlib

resultado = hashlib.md5(b'Python Security')

print("O hash da string é:", resultado.hexdigest())

texto2 = input("Digite o texto a ser gerado a hash:")

resultado2 = hashlib.md5(texto2.encode('utf-8'))

print("O hash da string é:", resultado2.hexdigest())