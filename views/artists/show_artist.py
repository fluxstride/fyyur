from flask import render_template
from models import Artist, Show, Venue
from datetime import datetime


def show_artist(artist_id):
    # shows the artist page with the given artist_id
    # TODO: replace with real artist data from the artist table, using artist_id

    artist = Artist.query.get(artist_id)
    now = datetime.now()

    data = {
        "id": artist.id,
        "name": artist.name,
        "genres": artist.genres.split(','),
        "city": artist.city,
        "state": artist.state,
        "phone": artist.phone,
        "website": artist.website_link,
        "facebook_link": artist.facebook_link,
        "seeking_venue": artist.seeking_venue,
        "seeking_description": artist.seeking_description,
        "image_link": artist.image_link,
        "past_shows": [],
        "upcoming_shows": [],
        "past_shows_count": Show.query.join(Artist).filter(Show.artist_id == artist_id).filter(Show.start_time < now).count(),
        "upcoming_shows_count": Show.query.join(Artist).filter(Show.artist_id == artist_id).filter(Show.start_time > now).count(),
    }

    past_shows = Show.query.join(Artist).filter(
        Show.artist_id == artist_id).filter(Show.start_time < now).all()
    upcoming_shows = Show.query.join(Artist).filter(
        Show.artist_id == artist_id).filter(Show.start_time > now).all()

    for past_show in past_shows:
        id = past_show.venue_id
        show = {
            "venue_id": id,
            "venue_name": Venue.query.get(id).name,
            "venue_image_link": Venue.query.get(id).image_link,
            "start_time": str(past_show.start_time)
        }
        data["past_shows"].append(show)

    for upcoming_show in upcoming_shows:
        id = upcoming_show.venue_id
        show = {
            "venue_id": id,
            "venue_name": Venue.query.get(id).name,
            "venue_image_link": Venue.query.get(id).image_link,
            "start_time": str(upcoming_show.start_time)
        }
        data["upcoming_shows"].append(show)

    return render_template('pages/show_artist.html', artist=data)
