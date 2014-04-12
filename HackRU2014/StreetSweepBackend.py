from flask import Flask, render_template, jsonify, url_for, request
import json, requests, urllib2, time, datetime, calendar
app = Flask(__name__) 

@app.route("/")
def first_one():
	return "it works!"

@app.route("/number_one/")
def second_one():
	return render_template('testonenumber.html')

if __name__ == '__main__':
	app.run(debug = True)