from flask import render_template
from models import Artist


def artists():
    # TODO: replace with real data returned from querying the database
    data = Artist.query.all()

    return render_template('pages/artists.html', artists=data)
