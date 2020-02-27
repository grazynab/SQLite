import database
import director
from exceptions import NoDataFoundException
import console

class DirectorRepository:

    def __init__(self, database):
        self.database = database

    def add(self, director):
        insertQuery = """INSERT INTO 'director'
                    ('Name', 'Birth_year', 'Death_year', 'Nationality')
                    VALUES (?,?,?,?);"""
        self.database.executeQuery(insertQuery, (director.name, director.birthYear,
                                                 director.deathYear, director.nationality))

    def find(self, Id):
        selectQuery = """SELECT * FROM 'director'
                        WHERE Id = (?);"""
        self.database.executeQuery(selectQuery, (Id,))
        record = self.database.cursor.fetchone()
        foundDirector = director.Director()
        foundDirector.loadFromRow(record)
        if foundDirector is None:
            raise NoDataFoundException()
        return foundDirector  # tu wyjątek jeśli nie ma wyników?

    def findByName(self, name):
        selectQuery = """SELECT * FROM 'director'
                    WHERE Name = (?);"""
        self.database.executeQuery(selectQuery, (name,))
        record = self.database.cursor.fetchone()
        foundDirector = director.Director()
        foundDirector.loadFromRow(record)
        return foundDirector

    def removeByName(self, name):
        deleteQuery = """DELETE FROM 'director'
                    WHERE Name IS (?);"""
        self.database.executeQuery(deleteQuery, (name,))

    def update(self, director):
        updateQuery = """UPDATE 'director'
                    ('Name', 'Birth_year', 'Death_year', 'Nationality')
                    = (?, ?, ?, ?)
                    WHERE Id = (?)"""
        self.database.executeQuery(updateQuery, (director.name, director.birthYear, director.deathYear,
                                                 director.nationality, director.id))

    # def updateName(self, name, newname):
    #     updateQuery = """UPDATE 'director'
    #                 SET Name = (?)
    #                 WHERE Name = (?);"""
    #     values = (newname, name)
    #     self.database.executeQuery(updateQuery, values)


