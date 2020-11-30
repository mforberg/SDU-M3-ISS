import random
import os
import string
import requests

number_of_items = 10
random.seed(1234)

uuid = 1
uuid_list = list()
color_list = ["black", "blue", "brown", "green", "red", "pink", "purple", "yellow", "white"]
brand_list = ["Addidas", "Nike", "Puma", "Reebok", "Jack&Jones", "Boss", "Levi's", "Lacoste", "Ralph Lauren", "Lee", "Zara"]
men_category = ["T-shirt", "jeans", "pants", "underpants", "shirt", "suits", "shoes", "hoodies"]
women_category = ["dress", "w_shirt", "jackets", "w_hoodies", "w_pants", "skirts", "w_shoes"]
children_catgory = ["size 50-74", "size 68-104", "size 92-140", "size 134-170"]
all_categories = [men_category, women_category, children_catgory]
price = 2
style = ["casual", "sporty", "street", "business"]
rand = 1429
store_items = {}






for x in range(number_of_items):
    items_dict = {}
    while len(uuid_list) < x:
       # print(uuid)
        uuid = random.randint(1, 9999)
        if uuid not in uuid_list:
            uuid_list.append(uuid)

    items_dict['uuid'] = uuid    
    category = random.choice(all_categories)
    items_dict['category'] = category
    items_dict['clothes_category'] = random.choice(category)
    items_dict['brand'] = random.choice(brand_list)
    items_dict['color'] = random.choice(color_list)
    items_dict['price'] = random.randint(100, 2500)
    items_dict['style'] = random.choice(style)
    requests.post("http://localhost:5000/insert", data=items_dict )
    #print(items_dict)

    
    #store_items[uuid] = [clothes_category, brand, color, price]
#for key in store_items:
    #requests.post("http://localhost5000/insert", data={key, store_items[key]} )
    #print(key, store_items[key])
#print(store_items)