def main():
    while True:
        try:
            #Transforma cada letra da str word em um indice na lista
            #Cria uma variavel para controlar o espaçamento a esquerda 
            
            word = list(input())
            blank_spaces = 0 
            while len(''.join(word)) > 0:
                print(blank_spaces * ' ' +  ' '.join(word))
                word.pop()
                blank_spaces += 1
        except EOFError:
            break
        print()

if __name__ == '__main__':
    main()
