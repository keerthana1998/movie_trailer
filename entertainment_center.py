import media
import fresh_tomatoes

Annabelle=media.Movie("Annabelle","A couple begins to experience terrifying supernatural occurences","https://i.ytimg.com/vi/Nby6KKEewas/maxresdefault.jpg","https://www.youtube.com/watch?v=jdUysoK6tdQ")

The_karate_kid=media.Movie("The karate kid","The Karate Kid is a 1984 American martial arts drama film produced by Jerry Weintraub","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmr0FscFFQ2jifUOciGrkEIxNIhGmNGatuAZl4k1d-YeeJWrZtHg","https://www.youtube.com/watch?v=XY8amUImEu0")


theri=media.Movie("theri","Indian Tamil-language action thriller film written and directed by Atlee and produced by Kalaipuli S. Thanu","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7Z34k7GrRfVfL05VTyjQDspFhtO7M1YPjhjF7qdYYJ3im9lYg","https://www.google.co.in/search?q=theri+movie+youtube+trailer&rlz=1C1NHXL_enIN760IN760&oq=theri+movie+youtube+trailer&aqs=chrome..69i57j0.14354j0j7&sourceid=chrome&ie=UTF-8")


#Annabelle.show_trailer()
movies=[Annabelle,The_karate_kid,theri]
fresh_tomatoes.open_movies_page(movies)
