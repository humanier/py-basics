input_lst = [45345, 342, 13421, 22, 45345, 12, 12, 56]
dct = {}

for el in input_lst:
    dct_el = dct.get(el)
    if dct_el == None:
        dct_el = 0
    
    dct_el += 1
    dct[el] = dct_el

print(dct)