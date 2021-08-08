from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from learning_log_flask.extentions import db
from .modules import Topic, Entry


ll_bp = Blueprint('ll_bp', __name__, template_folder='templates')

@ll_bp.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@ll_bp.route('/topics')
@login_required
def topics():
    """Show list of all topics"""
    topics = Topic.query.filter_by(owner_id=current_user.id).order_by(Topic.time_added).all()
    return render_template('topics.html', topics=topics)

@ll_bp.route('/topics/<int:topic_id>')
@login_required
def topic(topic_id):
    """Show entries for selected topic"""
    topic = Topic.query.filter_by(id=topic_id, owner_id=current_user.id).first_or_404()
    entries = topic.entries
    context = {'topic': topic, 'entries': entries}
    return render_template('topic.html', **context)

@ll_bp.route('/add_topic', methods=['GET', 'POST'])
@login_required
def add_topic():
    """Add new topic"""
    if request.method == 'POST':
        topic_name = request.form['name']
        topic = Topic(name=topic_name, owner_id=current_user.id)
        db.session.add(topic)
        db.session.commit()
        return redirect(url_for('ll_bp.topics'))
    else:
        return render_template('add_topic.html')

@ll_bp.route('/add_entry/<int:topic_id>', methods=['GET', 'POST'])
@login_required
def add_entry(topic_id):
    """Add new entry to specified topic"""
    topic = Topic.query.filter_by(id=topic_id, owner_id=current_user.id).first_or_404()

    if request.method == 'POST':
        entry_text = request.form['text']
        entry = Entry(text=entry_text, topic_id=topic.id)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('ll_bp.topic', **{'topic_id': topic.id}))
    else:
        return render_template('add_entry.html', topic=topic)

@ll_bp.route('/edit_entry/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    """Edit existed entry"""
    entry = Entry.query.get_or_404(entry_id)
    topic = Topic.query.filter_by(id=entry.topic_id, owner_id=current_user.id).first_or_404()

    if request.method == 'POST':
       edited_text = request.form['text']
       entry.text = edited_text
       db.session.commit()
       return redirect(url_for('ll_bp.topic', **{'topic_id': topic.id}))
    else:
        return render_template('edit_entry.html', entry=entry)  