from encodings import utf_8, utf_8_sig
import os
way = os.getcwd()
full_way = os.path.join(way, 'recipes.txt')
cook_book = {}
with open (full_way, 'r') as f:
    fr = f.read()
    list_ing = fr.split('\n\n')
    num = 0
    num_1 = 2
    list_ingrediense = []
    for i in list_ing:
        list_ingrediense += [i.split('\n')]
        ing_list = []
        while num_1 - 2 <= int(list_ingrediense[num][1]):
            if num_1 <= int(list_ingrediense[num][1]) + 1:
                ing_list += [{
                    'ingredient_name': list_ingrediense[num][num_1].split('|')[0], 
                    'quantity': int(list_ingrediense[num][num_1].split('|')[1]), 
                    'measure': list_ingrediense[num][num_1].split('|')[2]
                    }]
                num_1 += 1
            else:
                num_1 = 2
                break
        cook_book[list_ingrediense[num][0]] = ing_list
        num += 1

print (cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    for every_in_list in dishes:
        comp = cook_book.get(every_in_list)
        new_dict = {}
        for every in comp:
            every['quantity'] = every['quantity'] * person_count
            new_dict[every.pop('ingredient_name')] = every
    print (new_dict)

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 4)
