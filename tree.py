# ((((1) + 1) + 1) + 1) + 1
def list_lenght(lista):
    if lista == []:
        return 0
    if lista[0] % 2 == 0:
        return 1 + list_lenght(lista[1:])
    return list_lenght(lista[1:])

#print(list_lenght([1,2,4,7,8]))

def list_sum(lista):
    if lista == []:
        return 0
    return lista[0] + list_sum(lista[1:])

#print(list_sum([1,2,4,7,8]))

def list_dif(lista):
    if lista == []:
        return 0
    if lista[0] % 2 == 0:
        return list_dif(lista[1:]) + lista[0] 
    return list_dif(lista[1:]) - lista[0] 
    
#print(list_dif([1,2,4,7,8]))

#funcio garjesus
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibonacci(n - 2) + fibonacci(n - 1))
   

#print(len([0, 1]))

def fibonaccii(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibonacci_list = [0, 1]
    counter = 0
    while counter < n - 1:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
        counter += 1
    return fibonacci_list[-1]
     
#print(fibonaccii(0)) # 0
#print(fibonaccii(1)) # 1
#print(fibonaccii(2)) # 1
#print(fibonaccii(3)) # 2
#print(fibonaccii(4)) # 3
#print(fibonaccii(5)) # 5
#print(fibonaccii(6)) # 8
#print(fibonaccii(7)) # 13



print(fibonaccii(5))

#print(fibonaccii(10))


test = "Garjesus"
print(test[1])