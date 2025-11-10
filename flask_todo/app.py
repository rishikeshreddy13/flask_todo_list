from flask import Flask,redirect,render_template,url_for,request,flash,config
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key = 'your_secret_key'  


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
class task_table(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    def __init__(self,name):
        self.name=name

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=request.form['username']
        password=request.form['password']
        if ( user=='rishikesh' and password=='123'):
            return redirect(url_for('task_view'))
        else:
            flash('invalid username or password')
    return render_template('auth.html')


@app.route('/task',methods=['GET','POST'])
def task_view():
    if (request.method=='POST'):
        task=request.form['task']
        new_task=task_table(task)
        db.session.add(new_task)
        db.session.commit()
        
    return render_template('task.html',tasks=task_table.query.all())
@app.route('/delete/<id>',methods=['GET','POST'])
def delete_task(id):
    if ( request.method=='POST'):
         row_delete=task_table.query.get(id)
         db.session.delete(row_delete)
         db.session.commit()
         return redirect(url_for('task_view'))

@app.route('/logout',methods=['GET','POST'])
def logout():
    return redirect('/')

    
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    


