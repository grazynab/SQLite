import director
import exceptions


class Movie:

    def __init__(self):  #było: director (obiekt) i wtedy self.director = director.id
        self.id = None
        self.title = None
        self.director = None
        self.distributor = None
        self.releaseDate = None
        self.runningTime = None
        self.productionBudget = None
        self.USDVDSales = None
        self.USGross = None
        self.worldwideGross = None
        self.IMDBRating = None
        self.IMDBVotes = None
        self.MPAARating = None
        self.rottenTomatoesRating = None
        self.creativeType = None
        self.source = None

    def __str__(self):
        return "Movie id: " + str(self.id) + " Title: " + self.title

    # def loadFromDict(self, movies, movieID):  #to potrzebne do wczytywania z .json
    #     movie = movies[movieID]
    #     self.title = movie['Title']
    #     self.director = None
    #     self.distributor = None
    #     self.releaseDate = movie['Release_Date']
    #     self.runningTime = movie['Running_Time_min']
    #     self.productionBudget = movie['Production_Budget']
    #     self.USDVDSales = movie['US_DVD_Sales']
    #     self.USGross = movie['US_Gross']
    #     self.worldwideGross = movie['Worldwide_Gross']
    #     self.IMDBRating = movie['IMDB_Rating']
    #     self.IBDBVotes = movie['IMDB_Votes']
    #     self.MPAARating = movie['MPAA_Rating']
    #     self.rottenTomatoesRating = movie['Rotten_Tomatoes_Rating']
    #     self.creativeType = movie['Creative_Type']
    #     self.source = movie['Source']

    def loadFromRow(self, rowObject):
        if rowObject == None:
            raise exceptions.EmptyRowObjectException
        self.id = rowObject['Id']
        self.title = rowObject['Title']
        self.director = rowObject['Director_Id']
        self.distributor = rowObject['Distributor_Id']
        self.releaseDate = rowObject['Release_Date']
        self.runningTime = rowObject['Running_Time']
        self.productionBudget = rowObject['Production_Budget']
        self.USDVDSales = rowObject['US_DVD_Sales']
        self.USGross = rowObject['US_Gross']
        self.worldwideGross = rowObject['Worldwide_Gross']
        self.IMDBRating = rowObject['IMDB_Rating']
        self.IMDBVotes = rowObject['IMDB_Votes']
        self.MPAARating = rowObject['MPAA_Rating']
        self.rottenTomatoesRating = rowObject['Rotten_Tomatoes_Rating']
        self.creativeType = rowObject['Creative_Type']
        self.source = rowObject['Source']
