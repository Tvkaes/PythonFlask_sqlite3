from flask import Flask, render_template,url_for,request,redirect
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/info.db'
db = SQLAlchemy(app)

class Info(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

@app.route("/")
def login():
    infos=Info.query.all()
    return render_template("/index.html", infos = infos)

@app.route('/create-task', methods=['POST'])
def create():
    Infor = Info(content=request.form['content'], done= False)
    db.session.add(Infor)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/editar/<id>')
def editar(id):
    Info.query.filter_by(id=int(id)).first()
    Info.done=not(Info.done)   
    db.session.commit()
    return redirect(url_for('login')) 

@app.route('/delete/<id>')
def delete(id):
    Info.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run()