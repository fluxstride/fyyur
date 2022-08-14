from flask import render_template, request, flash
from models import db, Show
from forms import ShowForm
from sys import exc_info


def create_show():
    # renders form. do not touch.
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)


def create_show_handler():
    # called to create new shows in the db, upon submitting new show listing form
    # TODO: insert form data as a new Show record in the db, instead
    try:
        form = ShowForm(request.form)
        new_show = Show(
            artist_id=form.artist_id.data,
            venue_id=form.venue_id.data,
            start_time=form.start_time.data
        )
        db.session.add(new_show)
        db.session.commit()
        # on successful db insert, flash success
        flash('Show was successfully listed!')

    except:
        db.session.rollback()
        print(exc_info())
        # TODO: on unsuccessful db insert, flash an error instead.
        # e.g., flash('An error occurred. Show could not be listed.')
        # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
        flash('An error occurred. Show could not be listed.')

    finally:
        db.session.close()

    return render_template('pages/home.html')
