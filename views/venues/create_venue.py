from flask import render_template, request, flash
from forms import VenueForm
from models import db, Venue
from sys import exc_info


def create_venue():
    form = VenueForm()
    return render_template('forms/new_venue.html', form=form)


def create_venue_handler():
    # TODO: insert form data as a new Venue record in the db, instead
    # TODO: modify data to be the data object returned from db insertion

    try:
        venue_form = VenueForm(request.form)
        venue_data = Venue(
            name=venue_form.name.data,
            city=venue_form.city.data,
            state=venue_form.state.data,
            address=venue_form.address.data,
            phone=venue_form.phone.data,
            image_link=venue_form.image_link.data,
            facebook_link=venue_form.facebook_link.data,
            genres=", ".join(venue_form.genres.data),
            website_link=venue_form.website_link.data,
            seeking_talent=venue_form.seeking_talent.data,
            seeking_description=venue_form.seeking_description.data
        )
        db.session.add(venue_data)
        db.session.commit()

        # on successful db insert, flash success
        flash('Venue ' + request.form['name'] +
              ' was successfully listed!')
        print("yikes")
    except:
        print(exc_info())
        print(venue_form.errors, venue_data)
        db.session.rollback()

        # TODO: on unsuccessful db insert, flash an error instead.
        # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
        flash('An error occurred. Venue ' +
              venue_data.name + ' could not be listed.')
        # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/

    finally:
        db.session.close()

    return render_template('pages/home.html')
