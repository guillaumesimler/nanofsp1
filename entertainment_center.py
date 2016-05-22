# *** Entertainment Center ***
#
# This acts as model and kicks the View in

import media
import fresh_tomatoes

# Model

apocalypse_now = media.Movie("Apocalypse Now",
                             "Let's kill a colonel, sorry terminate his commands",
                             "https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
                             "https://www.youtube.com/watch?v=bPXVGQnJm0w")

english_patient = media.Movie("The English Patient",
                             "A remembrance of a love story at the end of WWII",
                             "https://upload.wikimedia.org/wikipedia/en/b/bd/The_English_Patient_Poster.jpg",
                             "https://www.youtube.com/watch?v=WPKpU14Kqqw")


inception = media.Movie("Inception",
                        "Using the full power of subconsciousness and dreams and changing it",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

je_vais_bien = media.Movie("Je vais bien, ne t'en fais pas",
                           "Searching for the dead twin brother",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Je_vais_bien%2C_ne_t%27en_fais_pas_poster.jpg/220px-Je_vais_bien%2C_ne_t%27en_fais_pas_poster.jpg",
                           "https://www.youtube.com/watch?v=wJRh0PlWB6g")


oceans_11 = media.Movie("Ocean's 11",
                        "Let's win it all: the money, revenge and ... the girl",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
                        "https://www.youtube.com/watch?v=imm6OR605UI")

v_for_vendetta= media.Movie("V for Vendetta",
                            "It is more than a personal vendetta",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Vforvendettamov.jpg/220px-Vforvendettamov.jpg",
                            "https://www.youtube.com/watch?v=qxyUl9M_7vc")

# Array as main transfer data
movies = [apocalypse_now, english_patient, inception, je_vais_bien, oceans_11, v_for_vendetta]

# Starting the element
fresh_tomatoes.open_movies_page(movies)                     


