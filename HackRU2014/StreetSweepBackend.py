from flask import Flask, render_template, jsonify, url_for, request
import json, requests, urllib2, time, datetime, calendar
import foursquare
app = Flask(__name__) 

@app.route("/")
def first_one():
	return "it works!"

@app.route("/number_one/")
def second_one():
	return render_template('testonenumber.html')

@app.route("/test_this/")
def third_one():
	return "it worked again"

@app.route("/help_me/")
def fourth_one():
	users = {"Jason Wu":'4ZSLCLMZ2MOWNW3EZNUYYIYVZJ2BLRG3W5BA5XTOPJQEYFN3'}
	test_one = {"first": "451ad473f964a520683a1fe3", "second": "4a78c3eaf964a5205ae61fe3", "third": "4d460bb7fcb7ba7a4740a1f0"}
	return "done"

@app.route("/form_test/")
def fifth_one():
	return render_template('latitude_longitude_form.html')

@app.route("/form_test/", methods = ['POST'])
def sixth_one():
	name = request.form['name']
	street = request.form['street']
	city = request.form['city']
	state = request.form['state']
	country = request.form['country']
	street = street.replace(" ", "_")
	city = city.replace(" ", "_")
	state = state.replace(" ", "_")
	country = country.replace(" ", "_")
	if name == "" or name == None:
		name = "random ass person"
	location_total = street + "," + city + "," + state + "," + country
	google_url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + location_total + "&sensor=false"
	google_data = json.loads(urllib2.urlopen(google_url).read())
	lat = google_data["results"][0]["geometry"]["location"]["lat"]
	lon = google_data["results"][0]["geometry"]["location"]["lng"]
	return render_template('pointer_market.html', lat = lat, lon = lon)

if __name__ == '__main__':
	app.run(debug = True)