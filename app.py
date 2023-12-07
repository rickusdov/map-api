from flask import Flask, render_template, request, redirect,url_for
from api import API
import requests
from form_request import format_req
import json
import subprocess
app = Flask(__name__)

@app.route('/')
def get_id():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api = API()
    api.set_json(requestJson)
    return '<p>'+str(api.get_id())+'</p>'
@app.route('/route')
def get_route():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api = API()
    api.set_json(requestJson)

    return redirect('/route?response='+str(api.get_order()),302)
@app.route('/dist')
def get_distance():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api = API()
    api.set_json(requestJson)
    return redirect('/home.html?response='+str(api.get_distance()),302)
@app.route('/dur')
def get_duration():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api = API()
    api.set_json(requestJson)
    return redirect('/dur?response='+str(api.get_duration()),302)
@app.errorhandler(404)
def pageNotFound(error):
    resp = request.args.get('response')
    if (resp != ''):
        return "<p>"+resp+"</p>"
    else:
        return '<p>request empty</p>'

@app.errorhandler(500)
def internalerror(error):
    return render_template('home.html')
if __name__ == "__main__":
    app.run()
    api = API()


