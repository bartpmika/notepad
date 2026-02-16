from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.models import Note
from app.notes import bp
from app.notes.forms import NoteForm


@bp.route('/')
@login_required
def dashboard():
    notes = current_user.notes.order_by(Note.updated_at.desc()).all()
    return render_template('notes/dashboard.html', notes=notes)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(
            title=form.title.data,
            body=form.body.data,
            user_id=current_user.id,
        )
        db.session.add(note)
        db.session.commit()
        flash('Note created.', 'success')
        return redirect(url_for('notes.dashboard'))
    return render_template('notes/create.html', form=form)


@bp.route('/<int:id>')
@login_required
def view(id):
    note = db.session.get(Note, id)
    if note is None:
        abort(404)
    if note.user_id != current_user.id:
        abort(403)
    return render_template('notes/view.html', note=note)


@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    note = db.session.get(Note, id)
    if note is None:
        abort(404)
    if note.user_id != current_user.id:
        abort(403)
    form = NoteForm(obj=note)
    if form.validate_on_submit():
        note.title = form.title.data
        note.body = form.body.data
        db.session.commit()
        flash('Note updated.', 'success')
        return redirect(url_for('notes.view', id=note.id))
    return render_template('notes/edit.html', form=form, note=note)


@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    note = db.session.get(Note, id)
    if note is None:
        abort(404)
    if note.user_id != current_user.id:
        abort(403)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted.', 'info')
    return redirect(url_for('notes.dashboard'))
