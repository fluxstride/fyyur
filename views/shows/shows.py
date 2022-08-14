from flask import render_template

from models import Artist, Show, Venue


def shows():
    # displays list of shows at /shows
    # TODO: replace with real venues data.

    data = []
    shows = Show.query.all()

    for show in shows:
        data_chunk = {
            "venue_id": show.venue_id,
            "venue_name": Venue.query.get(show.venue_id).name,
            "artist_id": show.artist_id,
            "artist_name": Artist.query.get(show.artist_id).name,
            "artist_image_link": Artist.query.get(show.artist_id).image_link,
            "start_time": str(show.start_time)
        }
        data.append(data_chunk)

    return render_template('pages/shows.html', shows=data)
