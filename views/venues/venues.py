from datetime import datetime
from flask import render_template

from models import Show, Venue, db


def venues():
    # TODO: replace with real venues data.
    #       num_upcoming_shows should be aggregated based on number of upcoming shows per venue.

    venues = Venue.query.all()
    areas = []

    for venue in venues:
        area = {
            "city": venue.city,
            "state": venue.state,
            "venues": []
        }

        area_venues_list = Venue.query.filter_by(
            city=venue.city, state=venue.state).all()

        for venue in area_venues_list:

            area_venue = {
                "id": venue.id,
                "name": venue.name,
                "num_upcoming_shows": db.session.query(Show).join(Venue).filter(Show.venue_id == venue.id).filter(Show.start_time > datetime.now()).count()
            }
            area["venues"].append(area_venue)

        if (area in areas):
            continue
        else:
            areas.append(area)
    return render_template('pages/venues.html', areas=areas)
