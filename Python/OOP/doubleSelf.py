class Bag:
    def __init__(self):
        self.data = []
        self.value = 0

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
        self.a

bag = Bag()
bag.addtwice(2)

print(bag.data)