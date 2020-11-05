qtd_medidas = int(input())
medidas = input().split()
for i in range(len(medidas)):
    medidas[i] = int(medidas[i])
    
if int(medidas[0]) > int(medidas[1]):
    starts_with_pico = True
else:
    starts_with_pico = False

default = 1
for index_medida in range(len(medidas)):
    try:
        if index_medida % 2 != starts_with_pico:
           if medidas[index_medida] <= medidas[index_medida + 1]:
                default = 0
        else:
           if medidas[index_medida] >= medidas[index_medida + 1]:
                default = 0
                
    except:
        continue

print(default)
