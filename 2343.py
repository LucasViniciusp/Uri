def main():
    qtd_registros = int(input())
    registros = []
    
    n_linhas = 0
    n_colunas = 0
    
    for i in range(qtd_registros):
        x, y = map(int, input().split())
    
        if x > n_linhas:
            n_linhas = x 
        
        if y > n_colunas:
            n_colunas = y
    
        registros.append((x,y))
    
    rst = 0
    matriz = []
    for x in range(n_linhas + 1):
        matriz = matriz + [[0] * (n_colunas + 1)]
    
    for x in registros:
        matriz[x[0]][x[1]] += 1
        if matriz[x[0]][x[1]] > 1:
            rst = 1
            break
    
    print(rst)

if __name__ == '__main__':
    main()
