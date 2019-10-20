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
    campaigns = [
        {
            'img': '/static/images/buy_agricultural_land_malaysia.png',
            'title': 'Bukit Nanas Degradation',
            'volunteer': '5/15',
            'location': 'Bukit Nanas, Kuala Lumpur',
            'price': 'RM 13 370',
            'width': "60%"
        },
        {
            'img':'/static/images/Kenyans-with-idle-land-to-lose-titles.png',
            'title': 'MaGIC’s Compound',
            'volunteer': '2/7',
            'location': 'MaGIC, Cyberjaya',
            'price': 'RM 10 350',
            'width': "35%"
        },
        {
            'img':'/static/images/images.png',
            'title': 'FRIM Camp Site',
            'volunteer': '9/10',
            'location': 'FRIM, Kepong',
            'price': 'RM 25 000',
            'width': "60%"
        },
        {
            'img':'/static/images/yq-malaysiapalm-04032010.png',
            'title': 'Daren’s Backyard',
            'volunteer': '0/2',
            'location': 'Puchong, Selangor',
            'price': 'RM 700',
            'width': "10%"
        },
    ]
    return render_template('campaigns.html', campaigns=campaigns)

@application.route("/impact", methods=['GET','POST'])
def impact():
    return render_template('impact.html')

@application.route("/campaign_details",methods=['GET', 'POST'])
def campaign_details():
    return render_template('campaign-details.html')

@application.route("/explore",methods=['GET', 'POST'])
def explore():
    return render_template('explore.html')

@application.route("/contribution",methods=['GET', 'POST'])
def contribution():
    return render_template('contribution.html')

if __name__ == "__main__":
    # Run the API server
    print("Starting up Server")
    application.run(debug=True,use_reloader=True)
	# app.run(debug=True,use_reloader=True)
	# app.run()
	# app.run('0.0.0.0')