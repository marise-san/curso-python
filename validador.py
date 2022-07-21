continuar = 'S'

print('##### VALIDADOR DE CPF #####')
while continuar == 'S':
    cpf = input('Digite o seu CPF: \n')
    cpf_tratado = []

    for caractere in cpf:
        if caractere != '.' and caractere != '-':
            cpf_tratado.append(caractere)

    novo_cpf = cpf_tratado[:-2]

    contador = 10
    acumulador = 0
    for i in range(19):
        if i > 8:
            i -= 9

        acumulador += int(novo_cpf[i]) * contador
        contador -= 1

        if contador < 2:
            contador = 11
            digito = 11 - (acumulador % 11)
            if digito > 9:
                digito = 0
            novo_cpf.append(str(digito))
            acumulador = 0  # resetando o acumulador.

    cpf = ''.join(cpf_tratado)
    novo_cpf = ''.join(novo_cpf)

    if cpf == novo_cpf:
        print(f'O CPF {novo_cpf} é VÁLIDO.')
    else:
        print(f'O CPF {novo_cpf} é INVÁLIDO.')

    continuar = input('Validar outro CPF? S/N ').upper()
