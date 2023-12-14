import json
def rev_form_request(cords):
    cords = str(cords)
    cords = ''.join(cords.split())
    temp1 = cords.split('",')
    #print(cords)
    if (len(temp1) <= 90):
        #print(len(temp1))

        #finalJson = 'ddd' + args.get('description')
        firstPart = ('{ "description":"route ", "locations": { "id": 2, "location": '
                     + str(cords) + ' }, "vehicles": [{ "id": 1, "end_index": '+str((len(temp1)-1))+', "capacity": [8]}],"shipments": [')
        temp = ''
        for i in range(0, len(temp1)-1 ,1):
            #print (i)
            temp += '{ "pickup":{ "id": ' + str(i) + ',"location_index": '+str(i)+' ,"service": 600}, "delivery": { "id": ' + str(i) + ',"location_index": ' + str((len(temp1)-1)) + ',"service": 600 }, "amount": [1]}'
            if ((i) != (len(temp1)-2)):
                #print(str(i) + ' ' +str(((len(temp1)-1))))
                temp += ','

        finalJson = firstPart + temp+']}'
        #finalJson = json.loads(finalJson)
        #print(finalJson)
        return (finalJson)
    else:
        return 0
#print(format_req('[ "51.4095261,9.3716946","51.4095261,9.3716946", "48.3668041,10.8986971", "48.3668041,10.8986971", "47.6303784,13.0042595", "47.5702774,10.6669948", "47.5702774,10.6669948", "47.5653342,9.7061951","51.4095261,9.3716953", "53.5068888,13.9989638" ]'))


#print(format_req('["48.8566,2.3522", "49.3988,8.6724", "48.1351,11.5820", "48.5734,7.7521", "52.5200,13.4050", "48.7758,9.1829", "50.6292,3.0573", "52.3705,9.7332", "43.2965,5.3698"]'))


