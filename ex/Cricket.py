class Cricketer:
    def __init__(self, name, country, catches):
        self.name = name
        self.country = country
        self.catches = catches

class Bowler(Cricketer):
    def __init__(self, name, country, catches, wickets):
        Cricketer.__init__(self,name, country, catches)
        self.wickets = wickets

    def get_points(self):
        return self.wickets // 5;


class Batsman(Cricketer):
    def __init__(self, name, country, catches, runs):
        Cricketer.__init__(self,name, country, catches)
        self.runs = runs

    def get_points(self):
        return self.runs // 100;


class Allrounder(Batsman, Bowler):
    def __init__(self, name, country, catches, wickets, runs):
        Batsman.__init__(self, name, country, catches, runs)
        Bowler.__init__(self, name, country, catches, wickets)

    def print(self):
        print(self.name, self.country, self.catches, self.wickets, self.runs)

    def get_points(self):
        return Batsman.get_points(self) + Bowler.get_points(self)


ba = Batsman("Xyz", "India", 10, 1000)
bo = Bowler("Pqr", "Aus", 10, 250)
print(ba.get_points())
print(bo.get_points())
a = Allrounder("Abc", "India", 10, 50, 2000)
a.print()
print(a.get_points())