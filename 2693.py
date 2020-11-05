def main():
    #L N O S
    while True:
        try:
            alunos_presentes = int(input()) 
            alunos = []
            while alunos_presentes > 0:
                nome, regiao, distancia = input().split()
                distancia = int(distancia)

                alunos.append([nome, regiao, distancia])
                alunos_presentes -= 1

            alunos.sort(key=lambda x: (x[2], x[1], x[0]))        

            for aluno in alunos:
                print(aluno[0])

        except EOFError:
            break
if __name__ == '__main__':
    main()
