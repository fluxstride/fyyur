from flask import render_template, request, flash
from forms import ArtistForm
from models import db, Artist
from sys import exc_info


def create_artist():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


def create_artist_handler():
    # TODO: insert form data as a new Venue record in the db, instead
    # TODO: modify data to be the data object returned from db insertion

    try:
        artist_form = ArtistForm(request.form)
        artist_data = Artist(
            name=artist_form.name.data,
            city=artist_form.city.data,
            state=artist_form.state.data,
            phone=artist_form.phone.data,
            image_link=artist_form.image_link.data,
            facebook_link=artist_form.facebook_link.data,
            genres=", ".join(artist_form.genres.data),
            website_link=artist_form.website_link.data,
            seeking_venue=artist_form.seeking_venue.data,
            seeking_description=artist_form.seeking_description.data
        )
        db.session.add(artist_data)
        db.session.commit()

        # on successful db insert, flash success
        flash('Venue ' + request.form['name'] +
              ' was successfully listed!')
        print("yikes")
    except:
        print(exc_info())
        print(artist_form.errors, artist_data)
        db.session.rollback()

        # TODO: on unsuccessful db insert, flash an error instead.
        # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
        flash('An error occurred. Venue ' +
              artist_data.name + ' could not be listed.')
        # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/

    finally:
        db.session.close()

    return render_template('pages/home.html')
