class Entity:
    def __init__(self):
        self.features = list()
        self.fishes = 0

        self.apples = 0
        self.fishes = 0
        self.tallow = 0
        self.needs = 1

    def __str__(self):
        # result = "Animal:\n"
        result = ""
        for feature in self.features:
            result += feature.name + '\n'
        return result

    def AddFeature(self, feature):
        self.features.append(feature)
        self.needs += feature.weight

    def RemoveFeature(self, feature):
        self.needs -= feature.weight
        self.features.remove(feature)

    def Attack(self, target) -> int:
        attack_result = 0
        for feature in target.features:
            if feature.on_attacked(target, self):
                attack_result += 1

        for feature in self.features:
            if feature.on_attack(self, target):
                attack_result += 1

        return attack_result

    def RefreshFood(self):
        self.fishes = 0
        self.apples = 0

    def AddFish(self, count=1):
        self.fishes += count

    def Fed(self) -> bool:
        return self.fishes + self.apples >= self.needs
