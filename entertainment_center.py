import fresh_tomatoes
import media

'''Movie - class in media module, accepts 4 parameters
(Name of movie,Description,Poster,Trailer)'''

fast1 = '''https://upload.wikimedia.org/wikipedia/en/2/2d/'''
justice1 = '''https://upload.wikimedia.org/wikipedia/en/3/31/'''
superhero1 = '''https://upload.wikimedia.org/wikipedia/en/2/20/'''
captain1 = '''https://upload.wikimedia.org/wikipedia/en/5/53/'''

anabelle1 = '''https://upload.wikimedia.org/wikipedia/en/0/08/'''
avengers1 = '''https://upload.wikimedia.org/wikipedia/en/9/90/'''
doctor1 = '''https://upload.wikimedia.org/wikipedia/en/c/c7/'''

'''Instance of class Movie'''
fast = media.Movie(
    '''The Fate Of The Furious''',
    '''The Fate of the Furious is a 2017 American action film directed by
    F. Gary Gray and written by Chris Morgan.''',
    fast1+'''The_Fate_of_The_Furious_Theatrical_Poster.jpg''',
    '''https://www.youtube.com/watch?v=uisBaTkQAEs''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
cars = media.Movie(
    '''Cars3''',
    '''Cars 3 is a 2017 American 3D computer-animated sports comedy-drama film
    produced by Pixar and released by Walt Disney Pictures.''',
    '''https://upload.wikimedia.org/wikipedia/en/9/94/Cars_3_poster.jpg''',
    '''https://www.youtube.com/watch?v=2LeOH9AGJQM''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
justice = media.Movie(
    '''Justice League''',
    '''Justice League is a 2017 American superhero film based on the DC Comics
    superhero team of the same name, distributed by Warner Bros. Pictures ''',
    justice1+'''Justice_League_film_poster.jpg''',
    '''https://www.youtube.com/watch?v=3cxixDgHUYw''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
anabelle = media.Movie(
    '''Anabelle : Creation''',
    '''Annabelle: Creation is a 2017 American supernatural horror film directed
    by David F. Sandberg and written by Gary Dauberman.''',
    anabelle1+'''Annabelle_Creation.jpg''',
    '''https://www.youtube.com/watch?v=KisPhy7T__Q''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
avengers = media.Movie(
    '''Avengers: Infinity War''',
    '''Avengers: Infinity War is an upcoming American superhero film based on the
    Marvel Comics superhero team the Avengers, produced by Marvel Studios.''',
    avengers1+'''Avengers_Infinity_War.jpg''',
    '''https://www.youtube.com/watch?v=6ZfuNTqbHE8''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
superhero = media.Movie(
    '''Batman v Superman''',
    '''Batman v Superman: Dawn of Justice is a 2016 American superhero film
    featuring the DC Comics characters Batman and Superman.''',
    superhero1+'''Batman_v_Superman_poster.jpg''',
    '''https://www.youtube.com/watch?v=0WWzgGyAH6Y''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
captain = media.Movie(
    '''Captain America: Civil War''',
    '''Captain America: Civil War is a 2016 American superhero film based on the
    Marvel Comics character Captain America, produced by Marvel Studios''',
    captain1+'''Captain_America_Civil_War_poster.jpg''',
    '''https://www.youtube.com/watch?v=dKrVegVI0Us''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
doctor = media.Movie(
    '''Doctor Strange''',
    '''Doctor Strange is a 2016 American superhero film based on the Marvel
    Comics character of the same name, produced by Marvel Studios''',
    doctor1+'''Doctor_Strange_poster.jpg''',
    '''https://www.youtube.com/watch?v=HSzx-zryEgM''')
'''-------------------------------------------------------------------------'''

'''Instance of class Movie'''
deadpool = media.Movie(
    '''DeadPool2''', '''The Untitled Deadpool Sequel, also known as Deadpool 2,
    an upcoming American superhero film based on the Marvel
    Comics character Deadpool.''',
    '''https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg''',
    '''https://www.youtube.com/watch?v=I4tFNfROlqk''')
'''-------------------------------------------------------------------------'''

'''Instances of class are listed in python data structure'''

movies = [fast, cars, justice, anabelle, avengers,
          superhero, captain, doctor, deadpool]
'''Calling open_movies_page function'''
fresh_tomatoes.open_movies_page(movies)
