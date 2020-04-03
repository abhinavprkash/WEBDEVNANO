import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of boys and his toys that came to life","https: // upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=tN1A2mVnrOM")

avatar = media.Movie("Avatar", "A marine on an Alien Planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATING)