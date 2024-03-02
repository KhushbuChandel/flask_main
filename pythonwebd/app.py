from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Initialize the SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Todo('{self.title}', '{self.desc}')"
    
@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        
        todo = Todo(title=title, desc=desc) 
        db.session.add(todo) 
        db.session.commit()
  # todo = Todo(title="First Todo", desc="Start investing in Stock market")
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is the products page'

if __name__ == "__main__":
    # with app.app_context():
    #     # Create the database tables if they don't exist
    #     db.create_all()
    app.run(debug=True)
