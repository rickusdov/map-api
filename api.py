import requests
import json
class API:
    def __init__(self):
        self.key = '689bc28853ff462bb5bc29237a72a25a'

    def set_json(self, request):
        self.request_json = json.loads(request)
        #print(self.request_json)
        return self.request_json


    def get_id(self):
        url = f'https://api.nextbillion.io/optimization/v2?key={self.key}'
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=self.request_json, headers=headers)
        results = r.json()

        if results['status'] == 'Ok':
            return results['id']

    def get_distance(self):
        id = self.get_id()
        url = f'https://api.nextbillion.io/optimization/v2/result?id={id}&key={self.key}'
        r = requests.get(url)
        results = r.json()
        #print(results)
        return round(float(results['result']['summary']['distance']) / 1000, 2)

    def get_duration(self):
        id = self.get_id()
        #print(id)
        url = f'https://api.nextbillion.io/optimization/v2/result?id={id}&key={self.key}'
        r = requests.get(url)
        results = r.json()
        #print(results)
        return (round(results['result']['summary']['duration'] * 0.0002777778, 2))

    def get_order(self):
        id = self.get_id()
        url = f'https://api.nextbillion.io/optimization/v2/result?id={id}&key={self.key}'
        r = requests.get(url)
        results = r.json()
        #print (results)
        temp = ''
        #print(results['result']['routes'])
        temp = str(results['result']['routes'])[1:-1]
        temp = temp.replace("'", '"')
        #print(temp)
        d = json.loads(temp)
        temp = str(d['steps'])[2:-2]
        temp = temp.replace("'", '"')
        new_list = temp.split(', {')
        #print(new_list)
        temp_list = []
        order_list = []

        for x in new_list:

            x = x.replace('}', '')
            x = x.replace("'", '"')
            temp = x.split(', "')
            #print(temp)
            temp_list.append(temp)
        for i in range(0,len(temp_list)):
            if ('end' not in str(temp_list[i]) and 'start' not in str(temp_list[i])):
                #print((temp_list[i]))
                for j in range(0,len(temp_list[i])):
                    #print(temp_list[i][j])
                    if 'location"' in str(temp_list[i][j]):
                        #print (temp_list[i][j])
                        temp = temp_list[i][j].replace('location": ', '')
                        order_list.append(temp)
        #print(order_list)
        clean_list = list(dict.fromkeys(order_list))
        #print(clean_list)
        return clean_list
