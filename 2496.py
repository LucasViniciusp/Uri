def main():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    qtd_testes = int(input())

    while qtd_testes > 0:
        qtd_letras = int(input())
        letras = input()
        letras_inesperadas = 0

        for index_letra in range(qtd_letras):
            if letras[index_letra] != alfabeto[index_letra]:
                letras_inesperadas += 1

        qtd_testes -= 1
        if letras_inesperadas > 2:
            print("There aren't the chance.")
        else:
            print("There are the chance.")

if __name__ == '__main__':
    main()
