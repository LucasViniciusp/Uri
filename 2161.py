x = 0
def main():
    repeticoes = int(input())
    
    def raiz_10(repeticoes):
        global x

        if repeticoes > 0:
            x += (1 / (6 + raiz_10(repeticoes - 1))) 
        return x

    a = raiz_10(repeticoes) + 3
    print('%.10f' %a)

if __name__ == '__main__':
    main()
