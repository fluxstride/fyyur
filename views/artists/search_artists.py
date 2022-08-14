from datetime import datetime
from flask import render_template, request

from models import Artist, Show


def search_artists():
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
    # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
    # search for "band" should return "The Wild Sax Band".
    search_term = request.form.get('search_term', '')
    search = '%{}%'.format(search_term)
    response = {
        "count": Artist.query.filter(Artist.name.ilike(search)).count(),
        "data": []
    }

    now = datetime.utcnow()
    artists = Artist.query.filter(Artist.name.ilike(search)).all()
    for artist in artists:
        chunk = {
            "id": artist.id,
            "name": artist.name,
            "num_upcoming_shows": Show.query.join(Artist).filter(Show.artist_id == artist.id).filter(Show.start_time > now).count(),
        }
        response["data"].append(chunk)
    return render_template('pages/search_artists.html', results=response, search_term=search_term)
