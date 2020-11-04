def main():
    qtd_registros = int(input())
    registros = []
    
    n_linhas = 0
    n_colunas = 0
    
    for i in range(qtd_registros):
        #coordenadas x,y em que cairam um raio
        x, y = map(int, input().split())
    
        if x > n_linhas:
            n_linhas = x 
        
        if y > n_colunas:
            n_colunas = y
        #salva as coordenadas do raio nos registros
        registros.append((x,y))
    #rst é o resultado. 1 se cair algum raio no mesmo lugar e 0 se não
    rst = 0
    matriz = []
    #criação da matriz com os valores de n_colunas e n_linhas para determinar o tamanho da matriz 
    for x in range(n_linhas + 1):
        matriz = matriz + [[0] * (n_colunas + 1)]
    #preenchimento da matriz com os valores salvos nos registros
    for x in registros:
        matriz[x[0]][x[1]] += 1
        if matriz[x[0]][x[1]] > 1:
            rst = 1
            break
    
    print(rst)

if __name__ == '__main__':
    main()
