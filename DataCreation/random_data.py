import random
import os
import string

number_of_items = 2000

uuid = 1
color_list = ["black", "blue", "brown", "green", "red", "pink", "purple", "yellow", "white"]
brand_list = ["Addidas", "Nike", "Puma", "Reebok", "Jack&Jones", "Boss", "Levi's", "Lacoste", "Ralph Lauren", "Lee", "Zara"]
men_category = ["T-shirt", "jeans", "pants", "underpants", "shirt", "suits", "shoes", "hoodies"]
women_category = ["dress", "shirts", "jackets", "hoodies", "pants", "skirts", "shoes"]
children_catgory = ["size 50-74", "size 68-104", "size 92-140", "size 134-170"]
all_categories = [men_category, women_category, children_catgory]
price = 1
style = ["casual", "sporty"]

def lcg(x):
    a = 18
    c = 11
    m = 17
    rand = (a * x + c) % m
    return rand


for x in range(number_of_items):
    uuid = random.randint(1, 9999)

