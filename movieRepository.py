import database
import movie
import exceptions

class MovieRepository:

    def __init__(self):
        self.database = database.Database()

    def addFromObject(self, movieObject):
        insertQuery = """INSERT INTO 'movie'
                    ('Title', 'Director_Id', 'Distributor_Id', 'Release_Date', 'Running_Time', 'Production_Budget',
                    'US_DVD_Sales', 'US_Gross', 'Worldwide_Gross', 'IMDB_Rating REAL', 'IMDB_Votes', 'MPAA_Rating',
                    'Rotten_Tomatoes_Rating', 'Creative_type', 'Source')
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
        self.database.executeQuery(insertQuery, (movieObject.title, movieObject.director, movieObject.distributor,
                                                 movieObject.releaseDate, movieObject.runningTime,
                                                 movieObject.productionBudget, movieObject.USDVDSales,
                                                 movieObject.USGross, movieObject.worldwideGross, movieObject.IMDBRating,
                                                 movieObject.IMDBVotes, movieObject.MPAARating,
                                                 movieObject.rottenTomatoesRating, movieObject.creativeType,
                                                 movieObject.source))
        if movieObject.director == None:
            raise exceptions.NoDirectorException()



    def addFromTuple(self, movie):
        insertQuery = """INSERT INTO 'movie'
                    ('Title', 'Director_Id', 'Distributor_Id', 'Release_Date', 'Running_Time', 'Production_Budget',
                    'US_DVD_Sales', 'US_Gross', 'Worldwide_Gross', 'IMDB_Rating REAL', 'IMDB_Votes', 'MPAA_Rating',
                    'Rotten_Tomatoes_Rating', 'Creative_type', 'Source')
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
        self.database.executeQuery(insertQuery, movie)

    def find(self, Id):
        selectQuery = """SELECT * FROM 'movie'
                        WHERE Id = (?);"""
        self.database.executeQuery(selectQuery, (Id,))
        record = self.database.cursor.fetchone()
        movieObject = movie.Movie()
        movieObject.loadFromRow(record)
        return movieObject

    def findByName(self, name):
        selectQuery = """SELECT * FROM 'movie'
                    WHERE Name = (?);"""
        self.database.executeQuery(selectQuery, (name,))
        record = self.database.cursor.fetchone()
        object = movie.Movie()
        object.loadFromRow(record)
        return object

    def removeByName(self, name):
        deleteQuery = """DELETE FROM 'movie'
                    WHERE Name IS (?);"""
        self.database.executeQuery(deleteQuery, (name,))

    def update(self, movieObject):
        updateQuery = """UPDATE 'movie'
                    SET ('Title', 'Director_Id', 'Distributor_Id', 'Release_Date', 'Running_Time',
                    'Production_Budget', 'US_DVD_Sales', 'US_Gross', 'Worldwide_Gross', 'IMDB_Rating REAL', 'IMDB_Votes',
                    'MPAA_Rating', 'Rotten_Tomatoes_Rating', 'Creative_type', 'Source')
                    = (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    WHERE Id = (?)"""
        self.database.executeQuery(updateQuery, (movieObject.title, movieObject.director, movieObject.distributor,
                                                 movieObject.releaseDate, movieObject.runningTime,
                                                 movieObject.productionBudget, movieObject.USDVDSales,
                                                 movieObject.USGross, movieObject.worldwideGross,
                                                 movieObject.IMDBRating,
                                                 movieObject.IMDBVotes, movieObject.MPAARating,
                                                 movieObject.RottenTomatoesRating, movieObject.creativeType,
                                                 movieObject.source, movieObject.id))

    def updateName(self, name, newname):
        updateQuery = """UPDATE 'director'
                    SET Name = (?)
                    WHERE Name = (?);"""
        values = (newname, name)
        self.database.executeQuery(updateQuery, values)

