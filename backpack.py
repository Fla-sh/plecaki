import random
import numpy as np
import copy
from items import Item
from items import Slot
import time

class Backpack:
    def __init__(self, amount=0, max_weight=0, from_file=False):
        self.amount = amount
        self.max_weight = max_weight
        self.items = self.load(from_file)
        print("Dynamic: " + str(self.pack()))

    def load(self, from_file):
        if from_file:
            return self.read_file()
        else:
            return self.shuffle()

    def read_file(self):
        with open("back.pack", "r") as backpack:
            data = backpack.read()
            lines = data.splitlines()
            items = list()

            for line in lines[1:]:
                words = line.split(" ")
                items.append(Item(int(words[0]),
                                  int(words[1])
                                  ))

            self.max_weight = int(lines[0].split(" ")[1]) + 1
            self.amount = len(items)
            return items

    def shuffle(self):
        items = list()
        for i in range(self.amount):
            items.append(Item(random.randint(0, self.max_weight),
                              random.randint(0, self.max_weight)
            ))

            return items

    def pack(self):
        t1 = time.time()
        backpack = list()
        for row in range(self.amount):
            line = list()
            for element in range(self.max_weight):
                line.append([[], 0])
            backpack.append(line)

        for weight in range(1, self.max_weight):
            for capacity in range(1, self.amount):
                best_item = None
                best_slot_value = None
                for k in range(len(self.items)):
                    if self.items[k].get_weight() <= weight:
                        if k not in backpack[capacity - 1][weight - self.items[k].get_weight()][0]:
                            best_item = k
                            best_slot_value = backpack[capacity - 1][weight - self.items[k].get_weight()][1] + self.items[k].get_value()
                            break
                if best_item is not None:
                    for item in range(len(self.items)):
                        if self.items[item].get_weight() <= weight:
                            actual_value = backpack[capacity - 1][weight - self.items[item].get_weight()][1] + self.items[item].get_value()
                            if actual_value > best_slot_value:
                                if item not in backpack[capacity - 1][weight - self.items[item].get_weight()][0]:
                                    best_item = item
                                    best_slot_value = backpack[capacity - 1][weight - self.items[item].get_weight()][1] + self.items[item].get_value()

                    if best_slot_value > backpack[capacity - 1][weight][1]:
                        backpack[capacity][weight] = copy.deepcopy(backpack[capacity - 1][weight - self.items[best_item].get_weight()])
                        backpack[capacity][weight][0].append(best_item)
                        backpack[capacity][weight][1] = best_slot_value
                    else:
                        backpack[capacity][weight] = copy.deepcopy(backpack[capacity - 1][weight])
                else:
                    backpack[capacity][weight] = copy.deepcopy(backpack[capacity - 1][weight])

        t2 = time.time()

        return (t2 - t1) * 1000



