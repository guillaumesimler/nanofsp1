# ***** Media.py ***** 
# 
# This python files, maanges the classes which will be used later


import webbrowser

class Movie():

	""" This stores the main info about a movie which are its title, its storyline, its poster, íts trailer in Youtube """


	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)    
