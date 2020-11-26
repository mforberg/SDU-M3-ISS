import random
import os
import string

number_of_items = 2000

uuid = 1
uuid_list = list()
color_list = ["black", "blue", "brown", "green", "red", "pink", "purple", "yellow", "white"]
brand_list = ["Addidas", "Nike", "Puma", "Reebok", "Jack&Jones", "Boss", "Levi's", "Lacoste", "Ralph Lauren", "Lee", "Zara"]
men_category = ["T-shirt", "jeans", "pants", "underpants", "shirt", "suits", "shoes", "hoodies"]
women_category = ["dress", "shirts", "jackets", "hoodies", "pants", "skirts", "shoes"]
children_catgory = ["size 50-74", "size 68-104", "size 92-140", "size 134-170"]
all_categories = [men_category, women_category, children_catgory]
price = 2
style = ["casual", "sporty"]
rand = 1429


def lcg(x):
    a = 18
    c = 11
    m = 10007
    x = (a * x + c) % m
    return x


for x in range(number_of_items):

    while len(uuid_list) < x:
        rand = lcg(1429)
        if rand not in uuid_list:
            uuid_list.append
    
    uuid = random.randint(1, 9999)
    

