import random
import uuid
from LewdBokks.backend.database_connection import DatabaseConnection

number_of_items = 9000
# random.seed(1234) 

color_list = ["black", "blue", "brown", "green", "red", "pink", "purple", "yellow", "white"]
brand_list = ["Addidas", "Nike", "Puma", "Reebok", "Jack&Jones", "Boss", "Levis", "Lacoste", "Ralph Lauren", "Lee",
              "Zara"]
men_category = ["T-shirt", "jeans", "pants", "underpants", "shirt", "suits", "shoes", "hoodies"]
women_category = ["dress", "w_shirt", "jackets", "w_hoodies", "w_pants", "skirts", "w_shoes"]
children_category = ["size 50-74", "size 68-104", "size 92-140", "size 134-170"]
all_categories = {"men": men_category, "women": women_category, "children": children_category}
price = 2
style_list = ["casual", "sporty", "street", "business"]
rand = 1429

dbc = DatabaseConnection().get_instance()

alist = list()

for x in range(number_of_items):

    pid = str(uuid.uuid4())

    primary_category = random.choice(list(all_categories.keys()))
    sub_category = random.choice(all_categories[primary_category])
    brand = random.choice(brand_list)
    color = random.choice(color_list)
    price = random.randint(100, 2500)
    style = random.choice(style_list)

    alist.append((pid, primary_category, sub_category, brand, color, price, style))

query = """INSERT INTO products.items (uuid, primary_category, sub_category, brand, color, price, style) VALUES (%s, %s, %s, %s, %s, %s, %s);"""

dbc.insert_dummy_data(query, alist)

