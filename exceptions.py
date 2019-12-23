class NoDirectorException(Exception):

    def __init__(self):
        super().__init__("There is no data about director for this movie.")
