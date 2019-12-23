import database
import director


class DirectorRepository:

    def __init__(self):
        self.database = database.Database()

    def addFromObject(self, directorObject):
        insertQuery = """INSERT INTO 'director'
                    ('Name', 'Birth_year', 'Death_year', 'Nationality')
                    VALUES (?,?,?,?);"""
        self.database.executeQuery(insertQuery, (directorObject.name, directorObject.birthYear,
                                                 directorObject.deathYear, directorObject.nationality))

    def addFromTuple(self, director):  # director = (name, birthYear, deathYear, nationality)
        insertQuery = """INSERT INTO 'director'
                    ('Name', 'Birth_year', 'Death_year', 'Nationality')
                    VALUES (?,?,?,?);"""
        self.database.executeQuery(insertQuery, director)

    def addManyFromTuples(self, directors):  # list of tuples including name, birthYear, deathYear, nationality
        insertManyQuery = """INSERT INTO 'director'
                        ('Name', 'Birth_year', 'Death_year', 'Nationality')
                        VALUES (?, ?, ?, ?);"""
        self.database.executeMany(insertManyQuery, directors)

    def find(self, Id):
        selectQuery = """SELECT * FROM 'director'
                    WHERE Id = (?);"""
        self.database.executeQuery(selectQuery, (Id,))
        record = self.database.cursor.fetchone()
        directorObject = director.Director()
        directorObject.loadFromRow(record)
        return directorObject

    def findByName(self, name):
        selectQuery = """SELECT * FROM 'director'
                    WHERE Name = (?);"""
        self.database.executeQuery(selectQuery, (name,))
        record = self.database.cursor.fetchone()
        object = director.Director()
        object.loadFromRow(record)
        return object

    def removeByName(self, name):
        deleteQuery = """DELETE FROM 'director'
                    WHERE Name IS (?);"""
        self.database.executeQuery(deleteQuery, (name,))

    def update(self, directorObject):
        updateQuery = """UPDATE 'director'
                    ('Name', 'Birth_year', 'Death_year', 'Nationality')
                    = (?, ?, ?, ?)
                    WHERE Id = (?)"""
        self.database.executeQuery(updateQuery, (directorObject.name, directorObject.birthYear, directorObject.deathYear,
                                                 directorObject.nationality, directorObject.id))

    def updateName(self, name, newname):
        updateQuery = """UPDATE 'director'
                    SET Name = (?)
                    WHERE Name = (?);"""
        values = (newname, name)
        self.database.executeQuery(updateQuery, values)
