import json

def to_json(cords,dist,dur):

    cords = cords[1:-1]
    #print(cords)
    cords = cords.replace("'[",'"')
    cords = cords.replace("]'", '"')
    #print(cords)
    resp = ('{"response": [' + cords + '], "distance": '+dur+', "duration": '+dist+'}')
    return resp