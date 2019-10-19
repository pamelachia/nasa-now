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

@application.route("/campaigns",methods=['GET', 'POST'])
def campaigns():
    print('click')

    campaigns = {
        1: '1',
        2: '2',
        3: '3'
    }
    return render_template('campaigns.html', campaigns=campaigns)

if __name__ == "__main__":
    # Run the API server
    print("Starting up Server")
    application.run(debug=True,use_reloader=True)
	# app.run(debug=True,use_reloader=True)
	# app.run()
	# app.run('0.0.0.0')