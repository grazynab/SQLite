import random


class Director:

    def __init__(self):
        self.id = None
        self.name = None
        self.birthYear = None
        self.deathYear = None
        self.nationality = None

        self.birthyears = [random.randint(1920, 1990) for x in range(1, 3201)]
        self.deathyears = [birthyear + random.randint(24, 89) for birthyear in self.birthyears]

    def loadFromDict(self, movies, movieID):  # database.movie[x]
        movie = movies[movieID]
        self.id = None
        self.name = movie['Director']
        self.birthYear = self.birthyears[movieID-1]
        self.deathYear = self.deathyears[movieID-1]
        self.nationality = None

    def loadFromRow(self, rowObject):
        self.id = None
        self.name = rowObject['Director']
        self.birthYear = None
        self.deathYear = None
        self.nationality = None





