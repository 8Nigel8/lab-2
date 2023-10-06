import math
from scipy.stats import t
import numpy as np

from utils import sample_generator, numbers_analyzer
import matplotlib.pyplot as plt

# знайти вибірки для заданих випадкових величин X і Y
sample = sample_generator.generate()
for i in range(len(sample['x'])):
    print(f"[{round(sample['x'][i], 3)};{round(sample['y'][i], 3)}]")

# побудувати кореляційне поле в координатах (X ,Y)
x_coords = sample['x']
y_coords = sample['y']

# емпірична лінія(лінія регресії)
slope, intercept = np.polyfit(x_coords, y_coords, 1)
regression_line_y = np.array(x_coords) * slope + intercept
plt.scatter(x_coords, y_coords)
plt.plot(x_coords, regression_line_y, color='red')

plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Scatter Plot with Regression Line')

plt.show()

# знайти вибіркові оцінки характеристик розподілів;
print(
    f"sample mean x: {numbers_analyzer.вибіркове_середнє(sample['x'])}\nsample mean y: {numbers_analyzer.вибіркове_середнє(sample['y'])}\nsample variance x: {numbers_analyzer.sample_variance(sample['x'])}\nsample variance y: {numbers_analyzer.sample_variance(sample['y'])}\nsample root mean square deviation x: {numbers_analyzer.sample_root_mean_square_deviation(sample['x'])}\nsample root mean square deviation y: {numbers_analyzer.sample_root_mean_square_deviation(sample['y'])}\nsample correlation coefficient x and y: {numbers_analyzer.sample_correlation_coefficient(data_y=sample['y'],data_x=sample['x'])}")


r = numbers_analyzer.sample_correlation_coefficient(data_y=sample['y'],data_x=sample['x'])
T = (r * math.sqrt(350 - 2)) / math.sqrt(1 - r ** 2)
tkp = t.ppf(1 - 0.05 / 2, 350 - 2)

if np.abs(T) < tkp:
    print("Нема підстав відкидати нульову гіпотезу")
else:
    print("Нульову гіпотезу відкидаєм")