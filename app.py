from flask import Flask, render_template, request, redirect,url_for
from api import API
import requests
from form_request import format_req
import json
import subprocess
from response_to_json import to_json
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
    #resp = (to_json(str(api.get_order())))
    #print(to_json(api.get_order()))
    if api.set_json(requestJson) != 0:
        resp = (to_json(str(api.get_order())))
        #return render_template('home.html', resp = resp)
    else:
        resp = 'Per daug masinu vienam uzsakymui'
    return render_template('home.html', resp=resp)
@app.route('/dist')
def get_distance():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api = API()
    api.set_json(requestJson)
    resp = (to_json(str(api.get_distance())))
    if api.set_json(requestJson) != 0:
        resp = (to_json(str(api.get_distance())))
        #return render_template('home.html', resp = resp)
    else:
        resp = 'Per daug masinu vienam uzsakymui'
    return render_template('home.html', resp=resp)
@app.route('/dur')
def get_duration():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api = API()
    api.set_json(requestJson)
    resp = (to_json(str(api.get_duration())))
    if api.set_json(requestJson) != 0:
        resp = (to_json(str(api.get_duration())))
        #return render_template('home.html', resp = resp)
    else:
        resp = 'Per daug masinu vienam uzsakymui'
    return render_template('home.html', resp=resp)
@app.errorhandler(500)
def pageNotFound(error):
    return redirect(request.url, code=302)

#
# @app.errorhandler(404)
# def internalerror(error):
#     return render_template('home.html')
if __name__ == "__main__":
    app.run()
    api = API()


