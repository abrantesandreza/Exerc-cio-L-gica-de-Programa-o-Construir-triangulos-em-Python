print('Vamos representar um triângulo? ')
print('Obs: Nenhum valor pode ser 0, tá bom?')
lado1 = int(input('Escreva um valor para um lado do triângulo: '))
lado2 = int(input('Escreva um valor para um lado do triângulo: '))
lado3 = int(input('Escreva um valor para um lado do triângulo: '))
if (lado1 == lado2 == lado3):
    print('Acabamos de construir um Triângulo Equilátero!! Parabéns!!')
elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print('Acabamos de construir um Triângulo Isósceles!!Uhuuu!')
elif (lado1 != lado2 != lado3):
    print('Acabamos de construir um Triângulo Escaleno!! Uhuuu!')
else:
    print('Não conseguimos construir um triângulo por enquanto, vamos tentar novamente!!')

