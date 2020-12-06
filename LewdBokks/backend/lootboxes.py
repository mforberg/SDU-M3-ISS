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

    def print_hello(self, test):
        print("hello" + test)


LootBox.get_instance().print_hello("penis")
