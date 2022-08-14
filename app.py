#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template
from flask_moment import Moment
import logging
from logging import Formatter, FileHandler
from forms import *

from flask_migrate import Migrate
from models import db
from views import index
from views.venues import search_venues, venues, show_venue, create_venue, delete_venue, edit_venue
from views.artists import search_artists, artists, show_artist, create_artist, delete_artist, edit_artist
from views.shows import shows, create_show

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')

# initializing the database
db.init_app(app)

# TODO: connect to a local postgresql database
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#  Venues
#  ----------------------------------------------------------------
app.add_url_rule('/', view_func=index.index, methods=['GET'])

#  Venues
#  ----------------------------------------------------------------
#  View all venues
app.add_url_rule(
    '/venues', view_func=venues.venues, methods=['GET'])
#  Search for a venue
app.add_url_rule('/venues/search',
                 view_func=search_venues.search_venues, methods=['POST'])
#  View a menu detail
app.add_url_rule('/venues/<int:venue_id>',
                 view_func=show_venue.show_venue, methods=['GET'])
#  Create Venue
#  ----------------------------------------------------------------
#  Create a venue page
app.add_url_rule('/venues/create',
                 view_func=create_venue.create_venue, methods=['GET'])
#  Create a venue form submission handler
app.add_url_rule('/venues/create',
                 view_func=create_venue.create_venue_handler, methods=['POST'])
#  Delete a venue
app.add_url_rule('/venues/<int:venue_id>',
                 view_func=delete_venue.delete_venue, methods=['DELETE'])

#  Update
#  ----------------------------------------------------------------
#  Edit a venue page
app.add_url_rule('/venues/<int:venue_id>/edit',
                 view_func=edit_venue.edit_Venue, methods=['GET'])
#  Edit a venue page form submission handler
app.add_url_rule('/venues/<int:venue_id>/edit',
                 view_func=edit_venue.edit_venue_handler, methods=['POST'])


#  Artists
#  ----------------------------------------------------------------
#  View all artists
app.add_url_rule(
    '/artists', view_func=artists.artists, methods=['GET'])
#  Search for an artist
app.add_url_rule('/artists/search',
                 view_func=search_artists.search_artists, methods=['POST'])
#  View an artist detail
app.add_url_rule('/artists/<int:artist_id>',
                 view_func=show_artist.show_artist, methods=['GET'])
#  Create Artist
#  ----------------------------------------------------------------
#  Create an artist page
app.add_url_rule('/artists/create',
                 view_func=create_artist.create_artist, methods=['GET'])
#  Create an artist form submission handler
app.add_url_rule('/artists/create',
                 view_func=create_artist.create_artist_handler, methods=['POST'])
#  Delete an artist
app.add_url_rule('/artists/<int:artist_id>',
                 view_func=delete_artist.delete_artist, methods=['DELETE'])

#  Update
#  ----------------------------------------------------------------
#  Edid an artist
app.add_url_rule('/artists/<int:artist_id>/edit',
                 view_func=edit_artist.get, methods=['GET'])
app.add_url_rule('/artists/<int:artist_id>/edit',
                 view_func=edit_artist.post, methods=['POST'])


#  Shows
#  ----------------------------------------------------------------
app.add_url_rule('/shows', view_func=shows.shows, methods=["GET"])
app.add_url_rule(
    '/shows/create', view_func=create_show.create_show, methods=["GET"])
app.add_url_rule(
    '/shows/create', view_func=create_show.create_show_handler, methods=["POST"])


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')


app.jinja_env.filters['datetime'] = format_datetime


@ app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@ app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
