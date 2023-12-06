from flask import Flask, render_template, request, redirect
from api import API
import requests
from form_request import format_req
import json
import subprocess
app = Flask(__name__)


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
    return redirect('/dist?response='+str(api.get_distance()),302)
@app.route('/dur')
def get_duration():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api = API()
    api.set_json(requestJson)
    return redirect('/dur?response='+str(api.get_duration()),302)
if __name__ == "__main__":
    app.run()
    api = API()


