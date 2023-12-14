import webbrowser
from flask import Flask, render_template, request, redirect,url_for
from api import API
import requests
from form_request import format_req
import json
import subprocess
from response_to_json import to_json
import multiprocessing.dummy as mp
import time
import resources
sample_list = ["48.8566, 2.3522", "43.2965, 5.3698", "45.7640, 4.8357", "44.8378, 0.5792", "43.7102, 7.2620", "52.5200, 13.4050", "48.1351, 11.5820", "53.5511, 9.9937", "50.1109, 8.6821", "50.9375, 6.9603", "48.7758, 9.1829"]
temp=[]
# for i in range(0, 10):
#     temp.insert(i,cords)
#     for j in range(0, 10):
#         if (i != j):
#             print(temp[i][j])
#     #print(temp[i])
from itertools import combinations

api = API()
list_combinations = list()
id_list = []
sample_set = set(sample_list)
def comb_api(line):
    print(line)
    requestJson = format_req(line)
    api.set_json(requestJson)
    resp = str(api.get_id())
    id_list.append(resp)
def get_dist(id):
    resp = (to_json(str(api.get_distance(id))))



if __name__=="__main__":
    st = time.time()
    list_combinations = list()
    for n in range(len(sample_set) + 1):
        list_combinations += list(combinations(sample_set, n))
    api = API()
    #
    id_list = []
    p=mp.Pool(4)
    temp_list = []
    dist_list = []
    # for line in list_combinations:
    #
    #     if (len(line) == 9):
    #         line = str(line).replace("'", '"').replace('(', '[').replace(')', ']')
    #         requestJson = format_req(line)
    #         api.set_json(requestJson)
    #         resp = str(api.get_id())
    #         id_list.append(str(resp))
    for line in list_combinations:
        if len(line) == 9:
            line = str(line).replace("'", '"').replace('(', '[').replace(')', ']')
            temp_list.append(line)
    print(len(line))

    p.map(comb_api,(temp_list)) # range(0,1000) if you want to replicate your example
    p.join()

    p.close()
    p.map(get_dist, (id_list))  # range(0,1000) if you want to replicate your example
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')