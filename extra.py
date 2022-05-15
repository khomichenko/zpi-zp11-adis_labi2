import pandas
import matplotlib.pyplot as pyplot


class Lab2Extra:
    filename = ""
    frame = []

    def __init__(self, filename):
        self.filename = filename

    def task_1_load(self):
        print(f"1. Записати дані у data frame.")
        self.frame = pandas.read_csv(self.filename + '.csv', sep=';', encoding='windows-1251')
        print(f"Дані записані в data frame. \n {self.frame.to_csv()}")

    def task_2_show(self):
        self.frame.info()
        self.frame.describe()

    def task_3_fix(self):
        self.frame['GDP per capita'] = self.frame['GDP per capita'].str.replace(',', '.').astype(float)
        self.frame['GDP per capita'].fillna(self.frame['GDP per capita'].notna().mean(), inplace=True)

        tmp = self.frame[self.frame['GDP per capita'] < 0]
        tmp['GDP per capita'] *= -1
        self.frame[self.frame['GDP per capita'] < 0] = tmp

        self.frame['Populatiion'].fillna(self.frame['Populatiion'].notna().mean(), inplace=True)

        tmp = self.frame[self.frame['Populatiion'] < 0]
        tmp['Populatiion'] *= -1
        self.frame[self.frame['Populatiion'] < 0] = tmp

        self.frame['CO2 emission'] = self.frame['CO2 emission'].str.replace(',', '.').astype(float)
        self.frame['CO2 emission'].fillna(self.frame['CO2 emission'].notna().mean(), inplace=True)

        tmp = self.frame[self.frame['CO2 emission'] < 0]
        tmp['CO2 emission'] *= -1
        self.frame[self.frame['CO2 emission'] < 0] = tmp

        self.frame['Area'] = self.frame['Area'].str.replace(',', '.').astype(float)

        tmp = self.frame[self.frame['Area'] < 0]
        tmp['Area'] *= -1
        self.frame[self.frame['Area'] < 0] = tmp

        print(f"3. Виправити помилки в даних.\n "
              f"  Провірка пустих значень\n{self.frame.isna().any()}")
        print(f"  Дані записані в data frame після виправлення. \n {self.frame.to_csv()}")
        self.frame.to_csv(self.filename + "fixed.csv", index=False, sep=';')

    def task_5_add_popdensity(self):
        self.frame['Pop. density'] = self.frame['Populatiion'] / self.frame['Area']

    def task_4_boxplots(self):
        figure, axis = pyplot.subplots(1, 5, figsize=(16, 4))
        figure.suptitle('Діаграма розмаху', fontsize=18)
        axis[0].set_title('GDP per capita')
        axis[0].boxplot(self.frame['GDP per capita'])
        axis[1].set_title('Populatiion')
        axis[1].boxplot(self.frame['Populatiion'])
        axis[2].set_title('CO2 emission')
        axis[2].boxplot(self.frame['CO2 emission'])
        axis[3].set_title('Area')
        axis[3].boxplot(self.frame['Area'])
        axis[4].set_title('Pop. density')
        axis[4].boxplot(self.frame['Pop. density'])
        pyplot.show()

    def task_4_histograms(self):
        figure, axis = pyplot.subplots(1, 5, figsize=(16, 4))
        figure.suptitle('Гістограми', fontsize=18)
        axis[0].set_title('GDP per capita')
        axis[0].hist(self.frame['GDP per capita'])
        axis[1].set_title('Population')
        axis[1].hist(self.frame['Populatiion'])
        axis[2].set_title('CO2 emission')
        axis[2].hist(self.frame['CO2 emission'])
        axis[3].set_title('Area')
        axis[3].hist(self.frame['Area'])
        axis[4].set_title('Pop. density')
        axis[4].hist(self.frame['Pop. density'])
        pyplot.show()

    def task_6_questions(self):
        print(f"6. Країна з найбільшим ВВП : {self.frame.loc[self.frame['GDP per capita'].idxmax()]['Country Name']}")
        print(f"7. Країна з найменшою площею : {self.frame.loc[self.frame['Area'].idxmin()]['Country Name']}")
        print(f"8. Регіон з найбільшою середньою площею : {self.frame.groupby(['Region']).mean()['Area'].idxmax()}")
        print(f"9. Країни з найбільшим населенням в світі :\n{self.frame.loc[self.frame['Populatiion'].idxmax()][['Country Name','Populatiion']]}")
        print(
            f"10. Країни з найбільшим населенням в Эвропі :\n{self.frame.loc[self.frame[self.frame['Region'] == 'Europe & Central Asia']['Populatiion'].idxmax()][['Country Name', 'Populatiion']]}")
        print(f"11. Регіони, в яких співпадають середнє та медіана ВВП :\n{pandas.merge(self.frame.groupby(['Region']).mean()['GDP per capita'],self.frame.groupby(['Region']).median()['GDP per capita'],how='inner')}")
        print(f"12. Топ 5 країн по ВВП :\n{self.frame.sort_values(by='GDP per capita',ascending=False).head(5)}")
        print(f"13. Last 5 країн по ВВП :\n{self.frame.sort_values(by='GDP per capita', ascending=True).head(5)}")
        self.frame['CO2 emission per citizen'] = self.frame['CO2 emission'] / self.frame['Populatiion']
        print(f"14. Топ 5 країн по викидам вуглекисного газу за добу :\n{self.frame.sort_values(by='CO2 emission per citizen', ascending=False).head(5)}")
        print(
            f"15. Last 5 країн по викидам вуглекисного газу за добу :\n{self.frame.sort_values(by='CO2 emission per citizen', ascending=True).head(5)}")

if __name__ == '__main__':
    app = Lab2Extra('Data2')
    app.task_1_load()
    app.task_2_show()
    app.task_3_fix()
    app.task_5_add_popdensity()
    app.task_4_boxplots()
    app.task_4_histograms()
    app.task_6_questions()
