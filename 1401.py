from itertools import permutations

def main():
    casos_testes = int(input())
    while casos_testes > 0:
        permutacoes = list(permutations(input()))
        permutacoes.sort()

        for index in range(len(permutacoes)):
            if permutacoes[index] != permutacoes[index - 1] or index == 0:
                print(''.join(permutacoes[index]))
        print()

        casos_testes -= 1

if __name__ == '__main__':
    main()
