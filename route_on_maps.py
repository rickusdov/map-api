def generate_google_maps_url(coordinates):
    #print((coordinates))
    #coordinates = str(coordinates)
    coordinates = coordinates[1:-1]
    coordinates = coordinates.replace(' ', '')
    coordinates = coordinates.replace("'[",'/')
    coordinates = coordinates.replace("]'", '/')
    coordinates = coordinates.replace(",/", '')
    coordinates = coordinates[1:]
    #coordinates = coordinates.replace('"', '')
    #print(coordinates)
    base_url = "https://www.google.com/maps/dir/"
    #print(base_url + coordinates)
    return base_url + coordinates


