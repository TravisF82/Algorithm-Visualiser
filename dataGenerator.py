import random

class DataGenerator:
    @staticmethod
    def GenerateDataSet(minimum=10, maximum=10000):
        return [random.randint(minimum, maximum) for _ in range(maximum - minimum + 1)]