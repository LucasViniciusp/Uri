def main():
    qtd_registros = int(input())
    registros = []

    n_linhas = 0
    n_colunas = 0

    for index_registro in range(qtd_registros):
        cood_x, cood_y = map(int, input().split())
    
        if cood_x > n_linhas:
            n_linhas = cood_x

        if cood_y > n_colunas:
            n_colunas = cood_y

        registros.append((cood_x, cood_y))

    matriz = cria_matriz(n_linhas + 1, n_colunas + 1)
    rst = 0

    for cood in registros:
        cood_x, cood_y = cood
        matriz[cood_x][cood_y] += 1
        if matriz[cood_x][cood_y] > 1:
            rst = 1
            break

    print(rst)

def cria_matriz(n_linhas, n_colunas):
    matriz = []
    for x in range(n_linhas):        
        matriz += [[0] * (n_colunas)]
    return matriz

if __name__ == '__main__':
    main()
