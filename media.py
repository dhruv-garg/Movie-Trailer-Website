class Movie():
    """Clas describing attributes of movie related information
    Args:
        movie_title (str): Title of the movie
        movie_storyline(str): Short description of the movie
        poster_image(str): Link to the respective movie
        trailer_youtube(str): Link to movie's youtube trailer
    Attributes:
        movie_title (str): Title of the movie
        movie_storyline(str): Short description of the movie
        poster_image_url(str): Link to the respective movie
        trailer_youtube_url(str): Link to movie's youtube trailer
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    '''Constructor of class Movie - initialized instance variables'''
