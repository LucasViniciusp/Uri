def contar_acertos_tiros(altura_tiros, kiloman_posicao):
    acertos = 0
    for i in range(len(altura_tiros)):
        altura = altura_tiros[i]
        kiloman = kiloman_posicao[i]

        if altura <= 2 and kiloman == 'S':
            acertos += 1

        elif altura > 2 and kiloman == 'J':
            acertos += 1
    return acertos

def main():
    qtd_testes = int(input())

    while qtd_testes > 0:
        tiros = int(input())
        alturas = list(map(int, input().split()))
        kiloman = input()
    
        acertos = contar_acertos_tiros(alturas, kiloman)

        print(acertos)
        qtd_testes -= 1

if __name__ == '__main__':
  main()
