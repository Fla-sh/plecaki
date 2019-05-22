

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def __str__(self):
        return "Item(v:{}, w:{})".format(self.value, self.weight)


class Slot:
    def __init__(self, items, value):
        self.containing_items = items
        self.slot_value = value

    def get_items(self):
        return self.containing_items

    def get_slot_value(self):
        return self.slot_value

    def __str__(self):
        return "Items {}, value:{}".format(self.containing_items,
                                           self.slot_value)
