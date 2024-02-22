# from flask import Flask

# # Create a Flask application instance
# app = Flask(__name__)

# # Define a route for the root URL
# @app.route('/albeli')
# def hello():
#     a=""
#     for i in range(0,6):
#         a=a+" Khushbu"
#     return a

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

# ////////////2
# from flask import Flask
# # WSGI Application

# app=Flask(__name__)

# @app.route('/')
# def welcome():
#        return "Welcome to ABCD App"


# @app.route('/members')
# def members():
#      return "Welcome to my youtube channel members"
   



# if __name__=='__main__':
#    app.run(debug=True)


# /////////////3//////////
# // building url dynamically & Variable rules and url building//////
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my Youtube Channel'

@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the marks is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is " + str(score)

### Result Checker

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)
