from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


db = SQLAlchemy()


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    last_modified = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    shows = db.relationship('Show', backref="artist",
                            lazy=True, cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Artist ID: {self.id}, name: {self.name}>"


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    last_modified = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    shows = db.relationship('Show', backref="venu",
                            lazy=True, cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Venue ID: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}>"


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artists.id'), nullable=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<Show id: {self.id}, artist_id: {self.artist_id},venue_id: {self.venue_id}, start_time: {self.start_time}>"
