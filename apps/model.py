from apps import db

class Movies(db.Model):
    __tablename__ = 'Movies'
    movieId = db.Column(db.Integer, nullable=True,primary_key=True)
    title = db.Column(db.String(250))
    genres = db.Column(db.String(180))

class Tags(db.Model):
    __tablename__ = 'Tags'
    userId = db.Column(db.Integer, nullable=True,primary_key=True)
    movieId = db.Column(db.Integer, nullable=True,primary_key=True)
    tag = db.Column(db.String(250))
    timestamp = db.Column(db.Integer, nullable=True)

class Ratings(db.Model):
    __tablename__ = 'Ratings'
    userId = db.Column(db.Integer, nullable=True,primary_key=True)
    movieId = db.Column(db.Integer, nullable=True,primary_key=True)
    rating = db.Column(db.Float)
    timestamp = db.Column(db.Integer, nullable=True)

class Links(db.Model):
    __tablename__ = 'Links'
    movieId = db.Column(db.Integer, nullable=True,primary_key=True)
    imdbId = db.Column(db.Integer, nullable=True,primary_key=True)
    tmdbId = db.Column(db.Integer)

class Genome_scores(db.Model):
    __tablename__ = 'Genome_scores'
    movieId = db.Column(db.Integer, nullable=True,primary_key=True)
    tagId = db.Column(db.Integer, nullable=True,primary_key=True)
    relevance = db.Column(db.String(30))

class Genome_tags(db.Model):
    __tablename__ = 'Genome_tags'
    tagId = db.Column(db.Integer, nullable=True,primary_key=True)
    tag = db.Column(db.String(100))

class MissionC(db.Model):
    __tablename__ = 'MissionC'
    id = db.Column(db.Integer, primary_key=True)
    Action = db.Column(db.TEXT)
    Adventure = db.Column(db.TEXT)
    Animation = db.Column(db.TEXT)
    Chidren = db.Column(db.TEXT)
    Comedy = db.Column(db.TEXT)
    Crime = db.Column(db.TEXT)
    Documentary = db.Column(db.TEXT)
    Drama = db.Column(db.TEXT)
    Fantasy = db.Column(db.TEXT)
    FilmNoir = db.Column(db.TEXT)
    Horro = db.Column(db.TEXT)
    IMAX = db.Column(db.TEXT)
    Musical = db.Column(db.TEXT)
    Mystery = db.Column(db.TEXT)
    Romance = db.Column(db.TEXT)
    SciFi = db.Column(db.TEXT)
    Thriller = db.Column(db.TEXT)
    War = db.Column(db.TEXT)
    Western = db.Column(db.TEXT)




