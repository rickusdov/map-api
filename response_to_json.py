import json

def to_json(cords):
    cords = cords[1:-1]
    print(cords)
    cords = cords.replace("'[",'"')
    cords = cords.replace("]'", '"')
    print(cords)
    resp = ('{"response:" [' + cords + ']}')
    return resp