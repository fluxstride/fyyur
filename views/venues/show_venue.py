from datetime import datetime
from flask import render_template

from models import Artist, Venue, Show, db


def show_venue(venue_id):
    # shows the venue page with the given venue_id
    # TODO: replace with real venue data from the venues table, using venue_id
    now = datetime.now()

    venue = db.session.query(Venue).get(venue_id)
    data = {
        "id": venue.id,
        "name": venue.name,
        "genres": venue.genres.split(','),
        "address": venue.address,
        "city": venue.city,
        "state": venue.state,
        "phone": venue.phone,
        "website": venue.website_link,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,

        "past_shows": [],
        "upcoming_shows": [],
        "past_shows_count": Show.query.join(Venue).filter(Show.venue_id == venue_id).filter(Show.start_time < now).count(),
        "upcoming_shows_count": Show.query.join(Venue).filter(Show.venue_id == venue_id).filter(Show.start_time > now).count(),
    }
    upcoming_shows = db.session.query(Show).join(
        Venue).filter(Show.venue_id == venue_id).filter(Show.start_time > now).all()
    past_shows = db.session.query(Show).join(
        Venue).filter(Show.venue_id == venue_id).filter(Show.start_time < now).all()

    for upcoming_show in upcoming_shows:
        show = {
            "artist_id": upcoming_show.artist_id,
            "artist_name": Artist.query.get(upcoming_show.artist_id).name,
            "artist_image_link": Artist.query.get(upcoming_show.artist_id).image_link,
            "start_time": str(upcoming_show.start_time)
        }
        data["upcoming_shows"].append(show)

    for past_show in past_shows:
        show = {
            "artist_id": past_show.artist_id,
            "artist_name": Artist.query.get(past_show.artist_id).name,
            "artist_image_link": Artist.query.get(past_show.artist_id).image_link,
            "start_time": str(past_show.start_time)
        }
        data["past_shows"].append(show)

    return render_template('pages/show_venue.html', venue=data)
