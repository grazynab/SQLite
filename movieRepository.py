import movie
import exceptions
import console

class MovieRepository:

    def __init__(self, database):
        self.database = database

    def add(self, movie):  #tu trzeba będzie podawać
        insertQuery = """INSERT INTO 'movie'
                    ('Title', 'Director_Id', 'Distributor_Id', 'Release_Date', 'Running_Time', 'Production_Budget',
                    'US_DVD_Sales', 'US_Gross', 'Worldwide_Gross', 'IMDB_Rating REAL', 'IMDB_Votes', 'MPAA_Rating',
                    'Rotten_Tomatoes_Rating', 'Creative_type', 'Source')
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
        self.database.executeQuery(insertQuery, (movie.title, movie.director, movie.distributor,
                                                 movie.releaseDate, movie.runningTime,
                                                 movie.productionBudget, movie.USDVDSales,
                                                 movie.USGross, movie.worldwideGross, movie.IMDBRating,
                                                 movie.IMDBVotes, movie.MPAARating,
                                                 movie.rottenTomatoesRating, movie.creativeType,
                                                 movie.source))

    def find(self, Id):
        selectQuery = """SELECT * FROM 'movie'
                        WHERE Id = (?);"""
        self.database.executeQuery(selectQuery, (Id,))
        record = self.database.cursor.fetchone()
        foundMovie = movie.Movie()
        foundMovie.loadFromRow(record)
        if foundMovie is None:
            raise exceptions.NoDataFoundException()
        return foundMovie

    def findByTitle(self, title):
        selectQuery = """SELECT * FROM 'movie'
                    WHERE Title = (?);"""
        self.database.executeQuery(selectQuery, (title,))
        record = self.database.cursor.fetchone()
        foundMovie = movie.Movie()
        foundMovie.loadFromRow(record)
        return foundMovie

    def findMoviesByDirector(self, directorId):
        selectQuery = """SELECT * FROM 'movie'
                                            WHERE Director_Id = (?);"""
        self.database.executeQuery(selectQuery, (directorId,))
        records = self.database.cursor.fetchall()
        movieList = []
        for item in records:
            foundMovie = movie.Movie()
            foundMovie.loadFromRow(item)
            movieList.append(foundMovie)
        return movieList

    def removeByName(self, name):
        deleteQuery = """DELETE FROM 'movie'
                    WHERE Name IS (?);"""
        self.database.executeQuery(deleteQuery, (name,))

    def update(self, movie):
        updateQuery = """UPDATE 'movie'
                    SET ('Title', 'Director_Id', 'Distributor_Id', 'Release_Date', 'Running_Time',
                    'Production_Budget', 'US_DVD_Sales', 'US_Gross', 'Worldwide_Gross', 'IMDB_Rating REAL', 'IMDB_Votes',
                    'MPAA_Rating', 'Rotten_Tomatoes_Rating', 'Creative_type', 'Source')
                    = (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    WHERE Id = (?)"""
        self.database.executeQuery(updateQuery, (movie.title, movie.director, movie.distributor,
                                                 movie.releaseDate, movie.runningTime,
                                                 movie.productionBudget, movie.USDVDSales,
                                                 movie.USGross, movie.worldwideGross,
                                                 movie.IMDBRating,
                                                 movie.IMDBVotes, movie.MPAARating,
                                                 movie.RottenTomatoesRating, movie.creativeType,
                                                 movie.source, movie.id))

    def updateName(self, name, newname):
        updateQuery = """UPDATE 'director'
                    SET Name = (?)
                    WHERE Name = (?);"""
        values = (newname, name)
        self.database.executeQuery(updateQuery, values)


