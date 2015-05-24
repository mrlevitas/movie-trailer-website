import media
import fresh_tomatoes

# Below is the list of media.Movie class instances that populates 
# the html website

toy_story = media.Movie(
   "Toy Story", 
   "A story of a boy and his toys that come to life",
   "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
   "www.youtube.com/watch?v=KYz2wyBy3kc")


fear_and_loathing = media.Movie(
   "Fear and Loathing in Las Vegas" , 
   "An oddball journalist and his psychopathic lawyer travel to Las Vegas for\
   a series of psychedelic escapades.",
   "http://upload.wikimedia.org/wikipedia/en/6/6f/FandlinLV.jpg",
   "https://www.youtube.com/watch?v=_d0hEzXrWT4")

big_lebowski = media.Movie(
   "The Big Lebowski" , 
   "A dude whose rug was peed on.", 
   "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
   "https://www.youtube.com/watch?v=cd-go0oBF4Y")
					 
everything_is_illuminated = media.Movie(
   "Everything is Illuminated" , 
   "A man trying to discover his past in Ukraine.",
   "http://upload.wikimedia.org/wikipedia/en/2/27/Everything_Is_Illuminated_film.jpg",
   "https://www.youtube.com/watch?v=tSUOYY4oukc")

black_dynamite = media.Movie(
   "Black Dynamite" , 
   "An ex-CIA operative cleans up the streets from some jive turkeys and \
   finds revenge for his fallen brother.",
   "http://upload.wikimedia.org/wikipedia/en/8/84/Black_dynamite_poster.jpg",
   "https://www.youtube.com/watch?v=96Y24a0cyCE")

synecdoche_new_york = media.Movie(
   "Synecdoche, New York" , 
   "An elusive play within a play within a movie.",
   "http://upload.wikimedia.org/wikipedia/en/6/6a/Synecdoche%2C_New_York_poster.jpg",
   "https://www.youtube.com/watch?v=XIizh6nYnTU")

					 
					 
# Create an array of the movies above.					 
movies = [toy_story, fear_and_loathing, big_lebowski, 
   everything_is_illuminated, black_dynamite, synecdoche_new_york]

# Call the fresh tomatoes file/function to display movies on html page, pass 
# array of media.Movie class instances as argument
fresh_tomatoes.open_movies_page(movies)
