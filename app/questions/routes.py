from flask import render_template, request, url_for, redirect, jsonify
from app.questions import bp
from app.models.question import Question
from app.extensions import db


@bp.route('/', methods=(['POST']))
def index():
    if request.method == 'POST':
        new_question = Question(content=request.form['content'],
                                answer=request.form['answer'])
        db.session.add(new_question)
        db.session.commit()
        return jsonify(new_question.as_dict())
