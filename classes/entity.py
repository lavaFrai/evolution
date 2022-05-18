class Entity:
    def __init__(self):
        self.features = list()

    def AddFeature(self, feature):
        self.features.append(feature)

    def Attack(self, target) -> int:
        attack_result = 0
        for feature in target.features:
            if feature.on_attacked(target, self):
                attack_result += 1
        return attack_result
