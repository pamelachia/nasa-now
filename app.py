#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request, send_file, abort
from werkzeug.wrappers import Request, Response
import datetime

# Global Variable
# EB looks for an 'application' callable by default.
application = Flask(__name__)
# app = Flask(__name__)

@application.route("/")
@application.route("/home",methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@application.route("/course_page",methods=['GET', 'POST'])
def course_page():
    return render_template('course.html')

@application.route("/register_course",methods=['GET', 'POST'])
def register_course():
    return render_template('register_course.html')

if __name__ == "__main__":
    # Run the API server
    # app.config['TEMPLATES_AUTO_RELOAD']=True
    print("Starting up Server")
    application.run(debug=True,use_reloader=True)
	# app.run(debug=True,use_reloader=True)
	# app.run()
	# app.run('0.0.0.0')