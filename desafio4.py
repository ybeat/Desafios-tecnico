#calcular o percentual de representação que cada estado teve dentro do valor total

sp=67836.43
rj=36678.66
mg=29229.88
es=27165.48
outros=19849.53
total = sp + rj + mg + es + outros

def calc_porcent(estado):
    porcentagem = estado / total 
    porcentagem = porcentagem*100
    return round(porcentagem,2)

print(f'valor total é: R${total}\n')
print(f'o valor total de São Paulo é de R${sp} com um percentual de {calc_porcent(estado=sp)}%')
print(f'o valor total do Rio de janeiro é de R${rj} com um percentual de {calc_porcent(estado=rj)}%')
print(f'o valor total de Minas gerais é de R${mg} com um percentual de {calc_porcent(estado=mg)}%')
print(f'o valor total de Espírito Santo é de R${es} com um percentual de {calc_porcent(estado=es)}%')
print(f'o total dos outros estados é de R${outros} com um percentual de {calc_porcent(estado=outros)}%\n')
