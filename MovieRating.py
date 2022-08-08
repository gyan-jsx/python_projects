class MovieRating:
    def __init__(self, movie, story, actors, music):
        self.movie = movie

        self.story = story
        self.actors = actors
        self.music = music

        self.avg = int((self.story + self.music + self.actors) / 3)
        