import sqlite3
import json
import random


class Database:

    def __init__(self):
        self.database = 'SQLite_Python.db'
        self.sqliteConnection = self.connectToOrCreateDatabase(self.database)
        self.cursor = self.createCursor()
        self.jsonFile = self.openJsonFile("/home/gb/Pobrane/movies.json")
        self.movies = self.loadJsonFile(self.jsonFile)
        self.columns = self.getColumnNames()  # to powinny być parametry wprowadzane dla danej instancji?

    def connectToOrCreateDatabase(self, database):
        try:
            sqliteConnection = sqlite3.connect(database)
            sqliteConnection.row_factory = sqlite3.Row  # teraz fetch zwraca obiekt z dostępem po kluczach(nazwy kolumn)
            return sqliteConnection
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)

    def createCursor(self):
        return self.sqliteConnection.cursor()  # tu musi być jakieś try?

    def closeConnection(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()
            print("Sqlite connection is closed.")  # czy to powinno być od razu w funkcjach jako finally?

    def dropTable(self, table):
        try:
            dropTableQuery = '''DROP TABLE (?);'''
            self.cursor.execute(table, dropTableQuery)
            self.sqliteConnection.commit()
            print("SQLite table dropped")
        except sqlite3.Error as error:
            print("Error while dropping the sqlite table", error)

    def executeSQLiteScript(self, scriptFilePath):
        try:
            with open(scriptFilePath, 'r') as sqlite_file:
                sql_script = sqlite_file.read()
                self.cursor.execute(sql_script)
            self.cursor.close()
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)

    def openJsonFile(self, filePath):
        return open(filePath, "r")

    def loadJsonFile(self, file):
        return json.load(file)

    def executeQuery(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.sqliteConnection.commit()
        except sqlite3.Error as error:
            print("Error while executing sqlite query", error)

    def executeMany(self, query, values):
        try:
            self.cursor.executemany(query, values)
            self.sqliteConnection.commit()
        except sqlite3.Error as error:
            print("Error while executing sqlite query", error)

    def getColumnNames(self):
        return list(self.movies[0].keys())
