def sales(lista):
    L = len(lista[0])
    income = [[], [0, 0, 0]]  # types #sizes
    for i in range(L):
        income[0].append(0)
    typee = input("Ti eidos pizza? 1-3: ")
    while typee != -1:
        size = raw_input("Ti megethos? K M G?: ")
        if size == "K":
            size = 0
        elif size == "M":
            size = 1
        else:
            size = 2
        price = pizza[1][typee - 1][size]
        income[0][typee - 1] = income[0][typee - 1] + price
        income[1][size] = income[1][size] + price
        typee = input("Ti eidos pizza? 1-10: ")
    return income

def megisto(lista):
    maxi = -1
    L = len(lista[0])
    for i in range(L):
        if lista[0][i] > maxi:
            maxi = lista[0][i]
            pos = [i]
        elif lista[0][i] == maxi:
            pos.append(i)
    return pos , maxi

def elaxisto(lista):
    mini = 1000000000000
    L = len(lista[0])
    for i in range(L):
        if lista[0][i] < mini:
            mini = lista[0][i]
            pos2 = [i]
        elif lista[0][i] == mini:
            pos2.append(i)
    return pos2,mini


def elaxisto2(lista):
    mini = 100000000000
    L = len(lista[1])
    for i in range(L):
        if lista[1][i] < mini:
            mini = lista[1][i]
            pos3 = i
    return pos3



pizza = [[], []] #names, price


for i in range(3):
    pizzaname = raw_input("Ti eidos pizza?: ")
    pizza[0].append(pizzaname)
    temp = []
    for j in range(3):
        price =  input("dose timh gia K / M / G : ")
        temp.append(price)
    pizza[1].append(temp)


elapameligo = sales(pizza)
print "Income for every type of pizza: ,Income for every pizza size: "
print elapameligo
megionoma,megitimh = megisto(elapameligo)
elaxonoma,elaxtimh = elaxisto(elapameligo)
elax = elaxisto2(elapameligo)
if elax == 0:
    elax = "Kanonikh"
elif elax == 1:
    elax = "Megalh"
else:
    elax = "Gigas"

print "Pizza type with the highest income: "
for i in megionoma:
    print pizza[0][i]
print "With an income of:", megitimh
print "====================================="
print "Pizza type with the lowest income: "
for i in elaxonoma:
    print pizza[0][i]
print "With an income of:", elaxtimh
print "====================================="
print "Pizza size with the lowest income: "
print elax





print "TELOS LEITOURGEI"

