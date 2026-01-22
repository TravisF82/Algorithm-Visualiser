import random

class DataGenerator:
    @staticmethod
    def GenerateDataSet(maximum=10000):
        return [random.randint(1, maximum + 1) for _ in range(maximum+ 1)]