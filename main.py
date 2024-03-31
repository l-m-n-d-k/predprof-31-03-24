from flask import Flask, render_template, redirect
from flask_restful import Api
from data.date_resource import DormitoryResource, DormitoryListResource
from forms.job_form import JobsForm
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


# @app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(Jobs).all()
#     users = db_sess.query(User).all()
#     names = {item.id: f"{item.surname} {item.name}" for item in users}
#     return render_template("index.html", jobs=jobs, names=names)
#
#
# @app.route('/date',  methods=['GET', 'POST'])
# def add_job():
#     form = JobsForm()
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         jobs = Jobs()
#         jobs.job = form.job.data
#         jobs.team_leader = form.team_leader.data
#         jobs.work_size = form.work_size.data
#         jobs.collaborators = form.collaborators.data
#         jobs.is_finished = form.is_finished.data
#         db_sess.add(jobs)
#         db_sess.commit()
#         return redirect('/')
#     return render_template('add_job.html', title='Добавление работы', form=form)


def main():
    db_session.global_init("db/dermitory.db")
    api.add_resource(DormitoryListResource, '/date')
    api.add_resource(DormitoryResource, '/date/<int:day>/<int:month>/<int:year>')
    app.run()


if __name__ == '__main__':
    main()
