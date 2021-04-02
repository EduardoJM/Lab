GENRE_MALE = 'MALE'
GENRE_FEMALE = 'FEMALE'
GENRE_UNKNOWN = 'UNKNOWN'

class People:
    def __init__(self, genre):
        """Creates a new People.
        Arguments:
            genre {str} -- The genre of the people.
        """
        self.genre = genre