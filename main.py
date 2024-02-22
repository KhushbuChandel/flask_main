# Integrate HTML with Flask
# HTTP Verb Get and Post


#Jinja2 tenmplate engine
'''  {%...%}for statements
 {{}}expressions to print output
 {#...#} this is for comments
 '''
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
        exp={'score':score,'res':res}
    # return render_template('result.html', result=res)
    
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is " + str(score)

### Result Checker

@app.route('/results/<int:marks>')
def results(marks):
    if marks < 50:
        return redirect(url_for('fail', score=marks))
    else:
        return redirect(url_for('success', score=marks))

# Result checker HTML page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
        return redirect(url_for('results', marks=total_score))

if __name__ == '__main__':
    app.run(debug=True)
