def main():
  while True:
      try:
          quantidade_ninjas = int(input())
          quantidade_jutsu_kagebunshin = 0
          
          while quantidade_ninjas > 1:
              quantidade_ninjas /= 2
              quantidade_jutsu_kagebunshin += 1

          print(quantidade_jutsu_kagebunshin)
      except EOFError:
          break

if __name__ == '__main__':
  main()
