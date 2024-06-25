def amounts (item2, store):
    if store in megadict and item2 in megadict[store]:
        return megadict[store][item2]
    else:
        return 0
import re

megadict = {'': {'': 0}}
#shop_name = {''}
#future_dict = {''}
item_list = {''}
shoplist = {''}
final_amount = {'':0}
try:
    f = open('input.txt', 'r')
    s = f.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
shoplists = s.split('}')

for shop in shoplists:
    shop = re.sub(r'[^a-zA-Z0-9:\n]', '', shop)
    if shop == '' or shop == "\n":
        continue
    shop_name = (shop.split(':')[0])
    shop_name = re.sub(r'[^\w\s]', '', shop_name)
    shoplist.add(shop_name)
    future_dict = (shop.split(':', 1)[1])
    lines = future_dict.split('\n')
    dictionary = {'': 0}
    for line in lines:
        line = re.sub(r'[^a-zA-Z0-9:]', '', line)
        if line != '':
            items = line.split(':')[0]
            amount = line.split(':')[1]
            items_new = re.sub(r'[^\w\s]', '', items)
            item_list.add(items_new)
            amount_new = int(re.sub(r'[^\w\s]', '', amount))
            dictionary.update({str(items_new): int(amount_new)})
    megadict.update({shop_name: dictionary})
for item in item_list:
    res = 0
    for shop in shoplist:
        res += amounts(item, shop)
    final_amount.update({item: res})
try:
    with open(r"output.txt", "w") as file:
        for key in final_amount.keys():
            if key != '':
                file.write(f"{key}:{final_amount[key]}\n")

except IOError as e:
    print(f"Error: Unable to write to file")


