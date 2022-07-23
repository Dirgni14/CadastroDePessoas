"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos."""

print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)

total18 = TotalH = TotalM20 =  0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M]: ')).strip().upper()[0]
    if idade > 18:
        total18 += 1
    if sexo == 'M':
        TotalH += 1
    if sexo == 'F' and idade < 20:
        TotalM20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}.')
print(f'Ao todo temos {TotalH} homens cadastrados e {TotalM20} mulheres com menos de 20 anos.')
print('ACABOU')


