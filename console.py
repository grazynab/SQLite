from exceptions import NoDataFoundException
from movieRepository import MovieRepository
from consoleReader import ConsoleReader
from directorRepository import DirectorRepository
from database import Database
from movie import Movie


class Console:

    def __init__(self, database=Database()):
        self.consoleReader = ConsoleReader()
        self.movieRepository = MovieRepository(database)
        self.directorRepository = DirectorRepository(database)
        self.database = database

    def run(self):
        self.database.connectToOrCreateDatabase()
        self.database.createCursor()  # ???
        data = None
        text = self.consoleReader.readTextFromConsole()
        while True:
            if "<" in text:
                data = self.getDataFromString(text)
            if text == "add movie":
                movie = self.consoleReader.readMovieInput()
                self.movieRepository.add(movie)
            elif "find movies id" in text:
                try:
                    print(self.movieRepository.find(int(data)))
                except NoDataFoundException:
                    return False  # tu flaga
            elif "find movies name" in text:
                print(self.movieRepository.findByTitle(data))
            elif "find movies" in text and "director" in text:
                movie = self.movieRepository.find(data)
                print(movie.director)
            elif "add director" in text:
                director = self.consoleReader.readDirectorInput()
                self.directorRepository.add(director)
            elif "find directors id" in text:
                print(self.directorRepository.find(data))
            elif "find directors name" in text:
                print(self.directorRepository.findByName(data))
            elif "find directors" in text and "movies" in text:
                movieList = self.movieRepository.findMoviesByDirector(data)
                for movie in movieList:
                    print(movie)
            else:
                self.database.closeConnection()
                break

        #ma być petla


        # add movie ...
        # find movies
        # find movies id <id>
        # find movies name <name>
        # find movies <id> director
        #
        # find directors
        # find directors id <id>
        # find directors name <name>
        # find directors <id> movies
        # exec(text)

        # wyłapywanie wyjątków!!!

    def getDataFromString(self, string):
        left = string.find("<")
        right = string.find(">")
        data = string[left:right]
        data = data.replace('<', '')
        data = data.replace('>', '')
        return data

# console = Console()
# console.run()


#unit testy
#mockowanie

#to samo tylko w django

