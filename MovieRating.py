class MovieRating:
    def __init__(self, movie, story, actors, music):
        self.movie = movie

        self.story = story
        self.actors = actors
        self.music = music

        self.avg = int((self.story + self.music + self.actors) / 3)

        self.myRating = {
            "Movie Name": self.movie,
            "Story Rating": self.story,
            "Actor Rating": self.actors,
            "Music Rating": self.music,
            "Avg Rating": self.avg
        }
        
    moviereviews = []

    def _append_data(self, movie_list):
        movie_list.append(self.myRating)

    def get_avg_star(self, movie_list):
        for movie in movie_list:
            if(movie["Avg Rating"] == 1):
                print("Thanks for your repsonse")
                print("You rated the movie with     *")
                print(movie)

            elif(movie["Avg Rating"] == 2):
                print("Thanks for your repsonse")
                print("You rated the movie with    **")
                print(movie)

            elif(movie["Avg Rating"] == 3):
                print("Thanks for your repsonse")
                print("You rated the movie with   ***")
                print(movie)

            elif(movie["Avg Rating"] == 4):
                print("Thanks for your repsonse")
                print("You rated the movie with   ****")
                print(movie)

            elif(movie["Avg Rating"] == 5):
                print("Thanks for your repsonse")
                print("You rated the movie with  *****")
                print(movie)

            else:
                print(movie)

review2 = MovieRating("Pursuit of Happines", 5, 3, 5)
review2._append_data(moviereviews)
review2.get_avg_star(moviereviews)


