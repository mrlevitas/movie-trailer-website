5/21/2015
code written by: Roman Levitas & Udacity team
contact: mrlevitas@yahoo.com

***************************Summary**********************************
This zip contains 3 files which combine to display an HTML static webstie that loads posters of 
movies and upon click, plays their trailer.


***************************General Usage****************************
Download and install Python 2.7.
To launch movie trailer website, run 'entertainment_center.py' in IDLE (after downloading python).



modules/files:
 
media
####################################################################
Contains media.Movie class, which is the primary class utilized by the fresh_tomatoes.py & entertainment_center.py files.
media.Movie stores all the information pertaining to an instance of a movie such as Title, Synopsis, Poster, and Trailer url 
which it takes as arguments.

primary file run as executable: 
entartainment_center.py
####################################################################
import media (to use media.Movie class)
import fresh_tomatoes (to pass array of movies for loading in a webpage)
This is the file used to call fresh_tomatoes.py and is the primary executing file.
It contains 6 instances of media.Movie class. These 6 instances are placed in an array and passed to fresh_tomatoes 
to be loaded as a webpage.

configuration, styles, and scripting to load media.Movie class instances into HTML renderable webpage:
fresh_tomatoes.py
###################################################################
Contains css formatting and html template necessary to display the instances of media.Movie classes.
Takes array of movie.Media class instances as argument.


