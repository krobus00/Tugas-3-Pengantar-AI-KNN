import math


class Distance:
    def __init__(self, df, test):
        self.df = df
        self.test = test

    def Euclidean(self):
        result = []
        for _, row in self.df.iterrows():
            rowResult = 0
            for col_name in list(self.df.columns)[1:]:
                rowResult += (row[col_name] - self.test[col_name]) ** 2
            result.append((math.sqrt(rowResult)))
        return result

    def Manhattan(self):
        result = []
        for _, row in self.df.iterrows():
            rowResult = 0
            for col_name in list(self.df.columns)[1:]:
                rowResult += abs(row[col_name] - self.test[col_name])
            result.append(rowResult)
        return result

    def Minkowski(self, p=2):
        result = []
        for _, row in self.df.iterrows():
            rowResult = 0
            for col_name in list(self.df.columns)[1:]:
                rowResult += (row[col_name] - self.test[col_name]) ** p
            result.append((rowResult ** 1/p))
        return result

    def Supremum(self):
        pass
