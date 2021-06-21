import math


class Distance:
    def __init__(self, df, test):
        self.df = df
        self.test = test.iloc[0]
        # drop non numeric data
        self.df = df._get_numeric_data()

    def Euclidean(self):
        result = []
        for _, row in self.df.iterrows():
            rowResult = sum((row - self.test) ** 2)
            result.append((math.sqrt(rowResult)))
        return result

    def Manhattan(self):
        result = []
        for _, row in self.df.iterrows():
            rowResult = sum(abs(row - self.test))
            result.append(rowResult)
        return result

    def Minkowski(self, p=1.5):
        result = []
        for _, row in self.df.iterrows():
            rowResult = sum(abs(row - self.test) ** p)
            result.append((rowResult ** (1/p)))
        return result

    def Supremum(self):
        result = []
        for _, row in self.df.iterrows():
            rowResult = max(abs(row - self.test))
            result.append((rowResult))
        return result

    def getAllDistance(self):
        return {
            'Euclidean': self.Euclidean(),
            'Manhattan': self.Manhattan(),
            'Minkowski': self.Minkowski(),
            'Supremum': self.Supremum()
        }
