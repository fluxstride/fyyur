from datetime import datetime
from flask import render_template, request
from models import Show, Venue


def search_venues():
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
    # seach for Hop should return "The Musical Hop".
    # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"

    search_term = request.form.get('search_term', '')
    search = "%{}%".format(search_term)
    venues = Venue.query.filter(Venue.name.ilike(search)).all()
    print(search, venues)
    response = {
        "count": Venue.query.filter(Venue.name.like(search)).count(),
        "data": []
    }

    now = datetime.now()
    for venue in venues:
        chunk = {
            "id": venue.id,
            "name": venue.name,
            "num_upcoming_shows": Show.query.join(Venue).filter(Show.venue_id == venue.id).filter(Show.start_time > now).count()
        }
        response["data"].append(chunk)

    return render_template('pages/search_venues.html', results=response, search_term=search_term)
