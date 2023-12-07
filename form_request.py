def format_req(cords):
    #finalJson = 'ddd' + args.get('description')
    firstPart = ('{ "description":"route ", "locations": { "id": 2, "location": '
                 + str(cords) + ' }, "vehicles": [{ "id": 1, "start_index": 0, "capacity": [8]}],"shipments": [')
    temp = ''
    for i in range(1, 9 ,1):
        #print (i)
        temp += '{ "pickup":{ "id": ' + str(i) + ',"location_index": 0 ,"service": 600}, "delivery": { "id": ' + str(i) + ',"location_index": ' + str(i) + ',"service": 600 }, "amount": [1]}'
        if (i != 8):
            temp += ','

    finalJson = firstPart + temp+']}'
    return finalJson








