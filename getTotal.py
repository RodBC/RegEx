from treatItens import lista
import re
# for x in lista:
#     preco = re.findall("$.*", x)
#     precos.append(preco)
data = re.search(r"\$.\d.*$", 'R$ 48,41')
# print(data.span())
x, y = data.span()
# print(x, y)
value = data.string[x+2:y]
data = re.sub(",", ".", value)
precos = []

for x in lista:
    #data: 30/03, compra: UBER UBER TRIP HELP UBER, preco: R$ 20,66
    data = re.search(r"\$.\d.*$", x)
    x, y = data.span()
    value = data.string[x+2:y]
    data = re.sub(",", ".", value)
    precos.append(float(data))
total = 0
for x in precos:
    total += x
print(total)