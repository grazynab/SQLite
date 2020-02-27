import random
import exceptions

class Director:

    def __init__(self):
        self.id = None
        self.name = None
        self.birthYear = None
        self.deathYear = None
        self.nationality = None

        self.birthyears = [random.randint(1920, 1990) for x in range(1, 3201)]
        self.deathyears = [birthyear + random.randint(24, 89) for birthyear in self.birthyears]

    def __str__(self):
        return "Director id: " + str(self.id) + " Name: " + self.name

    def loadFromDict(self, movies, movieID):  # database.movie[x]
        movie = movies[movieID]
        self.id = None
        self.name = movie['Director']
        self.birthYear = self.birthyears[movieID-1]
        self.deathYear = self.deathyears[movieID-1]
        self.nationality = None

    def loadFromRow(self, rowObject):
        if rowObject == None:
            raise exceptions.EmptyRowObjectException
        self.id = rowObject['Id']
        self.name = rowObject['Name']  # było: 'Director' bo ładowałam z obiektu movie - może się przydać
        self.birthYear = rowObject['Birth_year']
        self.deathYear = rowObject['Death_year']
        self.nationality = rowObject['Nationality']









