def main():
  qtd_testes = int(input())

  while n > 0:
      tiros = int(input())
      acertos = 0
      height = input().split()
      kiloman = input()

      for i in range(len(height)):
          if int(height[i]) <= 2 and kiloman[i] == 'S':
              acertos += 1

          elif int(height[i]) > 2 and kiloman[i] == 'J':
              acertos += 1

      print(acertos)
      qtd_testes -= 1

if __name__ == '__main__':
  main()
