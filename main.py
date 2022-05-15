import numpy as np
import statistics as s
from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr
import scipy.stats as stats
import matplotlib.pyplot as plt


class Lab2:
    sample = list

    def __init__(self, count):
        self.sample = np.random.random_sample(count)

    def show(self):
        print(f" Масив: {self.sample} ")
        print(f" Кількість елементів в масиві: {len(self.sample)} ")
        print(f" Середнє значення: {np.mean(self.sample)} ")
        print(f" Вибіркова дисперсія: {np.var(self.sample, ddof=1)} ")
        print(f" Виправлена вибіркова дисперсія: {np.var(self.sample)} ")
        print(f" Стандартне відхилення: {np.std(self.sample, ddof=1)} ")
        print(f" Медіана: {sorted(self.sample)[len(self.sample) // 2]} ")
        print(f" Медіана (бібліотекою statistics): {s.median(self.sample)} ")
        print(f" Середньоквадратичне відхилення: {np.sqrt(np.var(self.sample))} ")

        print(f" "
              f"1. Визначення точкових оцінок параметрів розподілу методом моментів: \n"
              f"   {importr('fitdistrplus').fitdist(FloatVector(self.sample), 'norm', 'mme')}")

        print(f""
              f"2. Визначення точкових оцінок параметрів розподілу методом найбільшої подібності: \n"
              f"   {importr('fitdistrplus').fitdist(FloatVector(self.sample), 'norm', 'mle')}")

        print(f"*** При порівнянні значень точкових оцінок параметрів розподілу, \n отриманих двома способами 1) і 2)"
              f"  ми бачимо, що математичне сподівання та стандартне відхилення однакові. ")

    def show_graph(self, count1, count2, count3, count4):
        figure, axis = plt.subplots(2, 2)
        h1 = sorted(self.sample)[:count1]
        axis[0, 0].plot(h1, stats.norm.pdf(h1, np.mean(h1), np.std(h1)))
        axis[0, 0].hist(h1, density=True)
        axis[0, 0].set_title(f"Кількість:{count1},середнє: {np.mean(h1)}")
        h2 = sorted(self.sample)[:count2]
        axis[0, 1].plot(h2, stats.norm.pdf(h2, np.mean(h2), np.std(h2)))
        axis[0, 1].hist(h2, density=True)
        axis[0, 1].set_title(f"Кількість:{count2},середнє: {np.mean(h2)}")
        h3 = sorted(self.sample)[:count3]
        axis[1, 0].plot(h3, stats.norm.pdf(h3, np.mean(h3), np.std(h3)))
        axis[1, 0].hist(h3, density=True)
        axis[1, 0].set_title(f"Кількість:{count3},середнє: {np.mean(h3)}")
        h4 = sorted(self.sample)[:count4]
        axis[1, 1].plot(h4, stats.norm.pdf(h4, np.mean(h4), np.std(h4)))
        axis[1, 1].hist(h4, density=True)
        axis[1, 1].set_title(f"Кількість:{count4},середнє: {np.mean(h4)}")
        print(f"*** На графіках зображено 4 гістограми для 25%, 50%, 75% і 100% даних.\n"
              f"Математичні сподівання для них {np.mean(h1)}, {np.mean(h2)}, {np.mean(h3)}, {np.mean(h4)} відповідно \n"
              f"Ці математичні сподівання є зростаюча числова послідовність, яка прямуює до середнього арифметичного "
              f"всієї вибірки {np.mean(h4)}"
              f"")
        plt.show()


if __name__ == '__main__':
    count = 40
    app = Lab2(count)
    app.show()
    app.show_graph(count // 8, count // 4, count // 2, count // 1)
