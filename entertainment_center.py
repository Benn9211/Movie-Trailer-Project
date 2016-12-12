import fresh_tomatoes
#I have a sprete file name fresh_tomatomes. Which is helping import all the data. 
import media
#I have a sprete file name media. Which is helping import all the data.

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

'''In this section of python coding.
   I am using Toy Story Movie Trailer that is using sytext of media.py to genrate that infornation on this movie.'''
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


# In this section of python coding. I am using Avatar Movie Trailer that is using sytext of media.py to genrate that infornation on this movie.
xXx_return_of_xander_cage = media.Movie("xXx: Return of Xander Cage",
                        "This will also mark the first film produced",
                        "https://upload.wikimedia.org/wikipedia/en/7/73/XXx_Return_of_Xander_Cage_offcial_logo_poster.jpg",
                        "https://www.youtube.com/watch?v=MQEFmHsseaU")

'''In this section of python coding. 
    I am using xXx: Return of Xander Cage Movie Trailer that is using sytext of media.py to genrate that infornation on this movie.'''
bad_moms = media.Movie("Bad Moms",
                     "Three lady try to become a good moms",
                     "https://upload.wikimedia.org/wikipedia/en/7/70/Bad_Moms_poster.jpg",
                     "https://www.youtube.com/watch?v=iKCw-kqo3cs")
# In this section of python coding. I am using Bad Moms Movie Trailer that is using sytext of media.py to genrate that infornation on this movie.
bang_bang = media.Movie("Bang Bang",
                        "A thief that stole the kuhinoor",
                        "https://upload.wikimedia.org/wikipedia/en/9/90/Bang_Bang_%282014_Film%29.jpg",
                        "https://www.youtube.com/watch?v=LRARHtMzZQE")
# In this section of python coding. I am using Bang Bang Movie Trailer that is using sytext of media.py to genrate that infornation on this movie.
doctor_strange = media.Movie("Doctor Strange",
                        "A doctor that leans how to fix  his broken hands",
                        "https://upload.wikimedia.org/wikipedia/en/4/4f/Doctor_Strange_Vol_4_2_Ross_Variant_Textless.jpg",
                        "https://www.youtube.com/watch?v=HSzx-zryEgM")
# In this section of python coding. I am using Doctor Strang Movie Trailer that is using sytext of media.py to genrate that infornation on this movie.
movies = [toy_story, avatar, xXx_return_of_xander_cage, bad_moms, bang_bang,doctor_strange]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
