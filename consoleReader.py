from movie import Movie
from director import Director


class ConsoleReader:

    def __init__(self):
        pass

    def readTextFromConsole(self):
        return input("You may now type in what you wish to do. Available commands: \n add movie \n find movies \n "
                     "find movies id <id> \n find movies name <name> \n find movies <id> director \n add director \n"
                     "find directors id <id> \n find directors name <name> \n find directors <id> movies \n")

    def readMovieInput(self):
        movie = Movie()
        movie.title = input("Please input movie title: ")
        movie.director = input("Please input movie director id: ")
        movie.distributor = input("Please input movie distributor: ")
        movie.releaseDate = input("Please input movie release date (YYYY-MM-DD): ")
        movie.runningTime = input("Please input movie running time (minutes): ")
        movie.productionBudget = input("Please input movie production budget: ")
        movie.USDVDSales = input("Please input movie US DVD sales: ")
        movie.USGross = input("Please input movie US gross: ")
        movie.worldwideGross = input("Please input movie worldwide gross: ")
        movie.IMDBRating = input("Please input movie IMDB rating: ")
        movie.IMDBVotes = input("Please input movie IMDB votes: ")
        movie.MPAARating = input("Please input movie MPAA rating: ")
        movie.rottenTomatoesRating = input("Please input movie Rotten Tomatoes rating: ")
        movie.creativeType = input("Please input movie creative type: ")
        movie.source = input("Please input movie source: ")
        return movie

    def readDirectorInput(self):
        director = Director()
        director.name = input("Please input the name of the director: ")
        director.birthYear = input("Please input birth year of the director (YYYY-MM-DD): ")
        director.deathYear = input("Please input death year of the director, if applicable (YYYY-MM-DD): ")
        director.nationality = input("Please input nationality of the director: ")
        return director



