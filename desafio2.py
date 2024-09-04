#VERIFICAR SE UM NÚMERO FAZ PARTE DA SEQUÊNCIA DE FIBONACCI
val =  2583
fibonacci=[0,1]

def checar_val():
    if val in fibonacci:
        print(f'{val} faz parte da sequência de fibonacci.')
        print(fibonacci)
    else:
        print(f'{val} NÃO faz parte da sequência de fibonacci.')
        print(fibonacci)

for i in fibonacci:
    novo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novo_numero)
    if fibonacci[-1] >= val:
        checar_val()
        break