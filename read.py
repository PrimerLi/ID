import json
import os

def read_json(inputFileName):
    assert(os.path.exists(inputFileName))
    ifile = open(inputFileName, "r")
    string_data = ifile.read()
    ifile.close()
    data = json.loads(string_data)
    return data

def toString(element):
    if (type(element) == unicode):
        return element.encode("utf-8")
    else:
        return str(element)

def print_dict(dictionary):
    keys = dictionary.keys()
    for i in range(len(keys)):
        print keys[i], dictionary[keys[i]]

def process_data(data):
    country = data["86"]
    province_keys = sorted(data['86'].keys())
    ofile = open("ID.csv", "w")
    for i in range(len(province_keys)):
        #print province_keys[i], data['86'][province_keys[i]]
        ofile.write(str(province_keys[i]) + "," + toString(data['86'][province_keys[i]]) + "\n")
        if (not province_keys[i] in data.keys()):
            print province_keys[i], data['86'][province_keys[i]]
            continue
        province_dictionary = data[province_keys[i]]
        city_keys = sorted(province_dictionary.keys())
        for j in range(len(city_keys)):
            #print city_keys[j], data['86'][province_keys[i]], province_dictionary[city_keys[j]]
            ofile.write(str(city_keys[j]) + "," + toString(data['86'][province_keys[i]]) + "," + toString(province_dictionary[city_keys[j]]) + "\n")
            if (not city_keys[j] in data.keys()):
                print city_keys[j], data['86'][province_keys[i]], province_dictionary[city_keys[j]]
                continue
            city_dictionary = data[city_keys[j]]
            county_keys = city_dictionary.keys()
            for k in range(len(county_keys)):
                #print county_keys[k], data['86'][province_keys[i]], province_dictionary[city_keys[j]], city_dictionary[county_keys[k]]
                ofile.write(str(county_keys[k]) + "," + toString(data['86'][province_keys[i]]) + "," + toString(province_dictionary[city_keys[j]]) + "," + toString(city_dictionary[county_keys[k]]) + "\n")
    ofile.close()
