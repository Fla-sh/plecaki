import random
import time
from items import Item


class BBackpack:
    def __init__(self, amount=0, max_weight=0, from_file=False):
        self.amount = amount
        self.max_weight = max_weight
        self.permutations = list()
        self.items = self.load(from_file)
        print("Recursive: " + str(self.pack()))

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

            self.max_weight = int(lines[0].split(" ")[1])
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
        self.permutate(0, [])
        max_permutation = []
        max_value = 0

        for perm in self.permutations:
            value = 0
            weight = 0
            # print(perm)
            for i in range(self.amount):
                if perm[i] == 1:
                    value += self.items[i].get_value()
                    weight += self.items[i].get_weight()

            if weight <= self.max_weight and value > max_value:
                max_permutation = perm
                max_value = value

        t2 = time.time()

        return (t2 - t1) * 1000

    def permutate(self, item, permutation):
        if item == self.amount:
            self.permutations.append(permutation)
        else:
            self.permutate(item + 1,
                           permutation + [0])

            self.permutate(item + 1,
                           permutation + [1])
