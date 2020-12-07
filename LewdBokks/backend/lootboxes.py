import db as db


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

    def generate_lootbox(self, uuid):
        """Method to generate a single lootbox of items based on a customers (UUID) preferences"""

        preferences = self.__get_preferences(uuid)
        collected_items = self.__collect(preferences)
        probability_assigned_items = self.__set_probabilities(collected_items)
        drawn_items = self.__draw_items(probability_assigned_items)

        return drawn_items

    def __get_preferences(self, uuid):
        """TODO: Needs to collect the users preferences from a database, based on their UUID"""
        return 0

    def __collect(self, preferences):
        """TODO: Needs to collect all (?) articles of clothing based on the preferences of the user prefs"""
        return 0

    def __set_probabilities(self, collected_items):
        """TODO: Once items has been collected, they need to have assigned random probabilities between their min &
        max """
        return 0

    def __draw_items(self, probabilitiy_assigned_items):
        """TODO: Should draw items based on probabilities"""
        return 0

