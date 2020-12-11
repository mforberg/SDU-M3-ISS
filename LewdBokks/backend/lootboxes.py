from .database_connection import DatabaseConnection
import random
import uuid

#dbc = DatabaseConnection().get_instance()


class LootBox:
    __instance = None

    @staticmethod
    def get_instance():
        if LootBox.__instance is None:
            LootBox()
        return LootBox.__instance

    def __init__(self):
        if LootBox.__instance is not None:
            raise Exception("Whoops")
        else:
            LootBox.__instance = self

    def generate_lootbox(self, uuid, dbc, lootbox_type):
        """Method to generate a single lootbox of items based on a customers (UUID) preferences"""
        preferences = self.__get_preferences(uuid, dbc)
        collected = self.__collect(preferences, dbc)
        probability_assigned_items = self.__set_probabilities(collected, dbc)
        #collected_items = self.__collect(probability_assigned_items, dbc)
        drawn_items = self.__draw_items(probability_assigned_items, lootbox_type)
        dbc.add_lootbox(uuid, drawn_items[1], drawn_items[0], drawn_items[2])
        return drawn_items

    def __get_preferences(self, uuid, dbc):
        """TODO: Needs to collect the users preferences from a database, based on their UUID"""
        result = dbc.get_preferences(uuid)
        return result

    def __collect(self, preferences, dbc):
        """TODO: Needs to collect all (?) articles of clothing based on the preferences of the user prefs"""
        result = []
        for preference in preferences:
            result.append(dbc.get_preferences_items(preference))
        return result

    def __set_probabilities(self, collected_items, dbc):
        """TODO: Once items has been collected, they need to have assigned random probabilities between their min &
        max """
        result = []
        for item in collected_items:
            if len(item) != 0:
                result.append((item[0][0], dbc.get_probability(item[0][0])))
        return result

    def __draw_items(self, probabilitiy_assigned_items, lootbox_type):
        """TODO: Should draw items based on probabilities"""

        
        item = random.choice(probabilitiy_assigned_items)
        discount = 0
        mini = item[1][0][0]
        maxi = item [1][0][1]
        val = random.randint(0, 100)
        loot = ""
        if lootbox_type == "Common":
            if val <= 80:
                loot = "Normal"
            else:
                loot = "Great"
        elif lootbox_type == "Uncommon":
            if val <= 70:
                loot = "Normal"
            else:
                loot = "Great"
        elif lootbox_type == "Rare":
            if val <= 60:
                loot = "Normal"
            else:
                loot = "Great"
        if loot == "Normal":
            half_point = round(maxi - ((maxi - mini) / 2))
            discount = random.randint(mini, half_point)
        elif loot == "Great":
            half_point = round(maxi - ((maxi - mini) / 2))
            discount = random.randint(half_point, maxi)  
        discount_code = str(uuid.uuid4())
        return discount, item[0], discount_code


#LootBox().__get_preferences(123)
