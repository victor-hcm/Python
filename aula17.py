num = [2, 5, 9, 1] #listas uso [] tuplas (), listas são mutáveis e tuplas não.
num [2] = 3 #troca o 9 pelo 3, começa com índice 0
num.append(7) #adiciona o número 7 ao final da lista.
num.sort(reverse=True)
num.insert(2, 0) #Depois do segundo indice ele adiciona o 0.
num.pop() #exclui o último elemento
print(num)
print(f'Essa lista tem {len(num)} elementos.') #conta a quantidade de elementos.