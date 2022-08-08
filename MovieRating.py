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
            "Music Rating": self.music
        }

   


