class NoDirectorException(Exception):

    def __init__(self):
        super().__init__("There is no data about director for this movie.")


class EmptyRowObjectException(Exception):  # inaczej nazwać i powstawiać wszędzie, wyłapać

    def __init__(self):
        super().__init__("There is no data!")


class NoDataFoundException(Exception):

    def __init__(self, entity):
        super().__init__(f"There is no {entity} you are looking for in this database.")  #
