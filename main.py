import re

class Planet:
    def __init__(self, name, open_date, radius):
        self.name = name
        self.open_date = open_date
        self.radius = radius

    def __str__(self):
        return f"{self.name} {self.open_date} {self.radius}"

class PlanetList:
    def __init__(self, List=[], path_to_txt=None):
        self.List = List
        self.read(path_to_txt)

    def __read_name(self, line):
        name = ""
        try:
            name = re.findall('"(.+?)"', line)[0]
        except:
            print("Reading name error")
        return name

    def __read_date(self, line):
        date = ""
        try:
            date = re.findall(r"\d{2}\.\d{2}\.\d{4}", line)[0]
        except:
            print("Reading date error")
        return date

    def __read_radius(self, line):
        radius = 0
        try:
            splitted = line.split(" ")
            for text in splitted:
                try:
                    float(text)
                    radius = float(text)
                except ValueError:
                    pass
        except:
            print("Reading radius error")
        return radius

    def read(self, path_to_txt):
        try:
            with open(path_to_txt, "r") as file:
                lines = file.readlines()
                for line in lines:
                    name = self.__read_name(line)
                    date = self.__read_date(line)
                    radius = self.__read_radius(line)
                    self.List.append(Planet(name, date, radius))
        except:
            print("File open error")

    def sort_by_date(self):
        self.List = [planet for planet in self.List if planet.open_date]
        try:
            self.List.sort(key=lambda x: tuple(map(int, x.open_date.split("."))))
        except ValueError:
            print("Error during sorting: invalid date format")

    def filter_by_radius(self, min_radius, max_radius):
        return [planet for planet in self.List if min_radius <= planet.radius <= max_radius]

    def show(self, planets=None):
        if planets is None:
            planets = self.List
        for planet in planets:
            print(str(planet))

planets = PlanetList(path_to_txt="data.txt")
planets.sort_by_date()
print("Список планет после сортировки по дате открытия:")
planets.show()

try:
    min_radius = float(input("Введите минимальный радиус: "))
    max_radius = float(input("Введите максимальный радиус: "))
    filtered_planets = planets.filter_by_radius(min_radius, max_radius)
    print(f"\nСписок планет с радиусом от {min_radius} до {max_radius}:")
    planets.show(filtered_planets)
except ValueError:
    print("Некорректный ввод. Убедитесь, что вы вводите числа.")