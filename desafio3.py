from random import randint

faturamento_diario = []
semana = ['Segunda','Terça','Quarta','Quinta','Sexta']
for i in range(30):
    val = randint(40,100)
    faturamento_diario.append(val)
print(faturamento_diario)

def checar_menor_numero(faturamento_diario):
    menor_numero = faturamento_diario[0]
    for i in range(len(faturamento_diario)):
        if menor_numero > faturamento_diario[i]:
            menor_numero = faturamento_diario[i]
        else:
            pass
    return menor_numero

def checar_maior_numero(faturamento_diario):
    maior_numero = faturamento_diario[0]
    for i in range(len(faturamento_diario)):
        if maior_numero < faturamento_diario[i]:
            maior_numero = faturamento_diario[i]
        else:
            pass
    return maior_numero

def media(faturamento_diario):
    val_total = 0
    for i in range(len(faturamento_diario)):
        val_total = val_total + faturamento_diario[i]
        val_medio = val_total/len(faturamento_diario)
    return round(val_medio,2)

def checar_destaques(faturamento_diario,media):
    qtd_destaques = 0
    for i in range(len(faturamento_diario)):
        if faturamento_diario[i] > media(faturamento_diario):
            qtd_destaques +=1
    return qtd_destaques

print(media(faturamento_diario))
print(checar_maior_numero(faturamento_diario))
print(checar_menor_numero(faturamento_diario))
print(checar_destaques(faturamento_diario,media))

