import random
from math import sqrt

просумувати = sum
довжина = len


class SampleGenerator:
    V = 8

    n = 350
    ax = V - 10
    ay = V + 5
    sigma_x = 3 + V / 10
    sigma_y = 5 + V / 5
    sum_limit = 12

    def generation_x(self):
        r = sum(random.uniform(0, 1) for _ in range(self.sum_limit))
        return (r - 6) * self.sigma_x + self.ax

    def generation_y(self):
        r = sum(random.uniform(0, 1) for _ in range(self.sum_limit))
        return (r - 6) * self.sigma_y + self.ay

    def generate(self):
        x = [self.generation_x() for _ in range(self.n)]
        y = [self.generation_y() for _ in range(self.n)]
        return {'x': x, 'y': y}


class АналізаторЧисел:
    @staticmethod
    def вибіркове_середнє(дані):
        return просумувати(дані) / довжина(дані)

    def sample_variance(я, дані):
        вибіркове_середнє = я.вибіркове_середнє(дані)
        сума = 0
        for число in дані:
            сума += pow((число - вибіркове_середнє), 2)
        return сума / довжина(дані)

    def sample_root_mean_square_deviation(self, data):
        return sqrt(self.sample_variance(data))

    def sample_correlation_coefficient(self, data_x, data_y):
        root_deviation_x = self.sample_root_mean_square_deviation(data_x)
        root_deviation_y = self.sample_root_mean_square_deviation(data_y)
        Xv = self.вибіркове_середнє(data_x)
        Yv = self.вибіркове_середнє(data_y)

        suma = 0
        for i in range(len(data_y)):
            suma += (data_x[i] - Xv) * (data_y[i] - Yv)
        return suma / (len(data_x) * root_deviation_x * root_deviation_y)


numbers_analyzer = АналізаторЧисел()
sample_generator = SampleGenerator()
