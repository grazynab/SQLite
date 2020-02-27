from unittest.mock import MagicMock
from unittest.mock import patch
from console import Console
from movie import Movie
import pytest


class Test_Console:

    @pytest.fixture(scope="module")
    def console(self):
        console = Console()
        console.consoleReader = MagicMock()
        console.database = MagicMock()
        console.movieRepository = MagicMock()
        return console

    def test_ifDataFromStringIsCorrect(self, console):
        string = "String containing <data>"
        assert console.getDataFromString(string) == "data"

    def test_ifMovieIsAddedWhenInputAddMovie(self, console):
        console.consoleReader.readTextFromConsole.return_value = "add movie"
        console.run()
        assert console.movieRepository.add.assert_called_once is True
