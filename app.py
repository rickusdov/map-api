from flask import Flask, render_template, request, redirect,url_for
from api import API
import requests
from form_request import format_req
import json
import subprocess
from response_to_json import to_json
app = Flask(__name__)
from rev_form_request import rev_form_request
from route_on_maps import generate_google_maps_url

api = API()

@app.route('/')
def get_id():
    return '<p>no cords</p>'
@app.route('/route')
def get_route():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
    api.set_json(requestJson)
    id=api.get_id()
    url = f'https://api.nextbillion.io/optimization/v2/result?id={id}&key={api.key}'
    r = requests.get(url)
    results = r.json()
    while(results['message'] == 'Job still processing'):
        r = requests.get(url)
        results = r.json()
        if results['message'] != 'Job still processing':
            break


    #resp = (to_json(str(api.get_order(results))))
    print(str(api.get_duration(results)))
    print(str(api.get_distance(results)))

    if api.set_json(requestJson) != 0:
        #resp = to_json(str(api.get_order(results)), str(api.get_duration(results)), str(api.get_distance(results)))
        cords = cords.replace(' ', '')
        cords = cords[1:-1]
        cords = cords.split('","')
        cords = str(cords)
        cords = cords.replace('"',"'").replace("[''","['[").replace("'']","]']").replace("',", "]',").replace(", '", ", '[")
        print(cords)
        print(cords)


        resp = (to_json(str(api.get_order(results)), str(api.get_duration(results)), str(api.get_distance(results))))

    else:
        url = ''
        resp = 'Per daug masinu vienam uzsakymui'
    return '<p>'+resp+'</p>'
@app.route('/rev-route')
def get_rev_route():
    cords = request.args.get('cords')
    requestJson = rev_form_request(cords)
    api.set_json(requestJson)
    id = api.get_id()
    url = f'https://api.nextbillion.io/optimization/v2/result?id={id}&key={api.key}'
    r = requests.get(url)
    results = r.json()
    while (results['message'] == 'Job still processing'):
        r = requests.get(url)
        results = r.json()
        if results['message'] != 'Job still processing':
            break

    # resp = (to_json(str(api.get_order(results))))
    print(str(api.get_duration(results)))
    print(str(api.get_distance(results)))

    if api.set_json(requestJson) != 0:
        # resp = to_json(str(api.get_order(results)), str(api.get_duration(results)), str(api.get_distance(results)))
        cords = cords.replace(' ', '')
        cords = cords[1:-1]
        cords = cords.split('","')
        cords = str(cords)
        cords = cords.replace('"', "'").replace("[''", "['[").replace("'']", "]']").replace("',", "]',").replace(", '",
                                                                                                                 ", '[")
        print(cords)
        print(cords)

        resp = (to_json(str(api.get_order(results)), str(api.get_duration(results)), str(api.get_distance(results))))

    else:
        url = ''
        resp = 'Per daug masinu vienam uzsakymui'
    return '<p>' + resp + '</p>'
@app.route('/dist')
def get_distance():
    cords = request.args.get('cords')
    requestJson = format_req(cords)
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

    api.set_json(requestJson)
    resp = (to_json(str(api.get_duration())))
    if api.set_json(requestJson) != 0:
        resp = (to_json(str(api.get_duration())))
        #return render_template('home.html', resp = resp)
    else:
        resp = 'Per daug masinu vienam uzsakymui'
    return render_template('home.html', resp=resp)
# @app.errorhandler(500)
# def pageNotFound(error):
#     return redirect(request.url, code=302)

#
# @app.errorhandler(404)
# def internalerror(error):
#     return render_template('home.html')
if __name__ == "__main__":
    app.run()
    api = API()


