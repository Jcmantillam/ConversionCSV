import csv
import json


def write_jason(data):
    with open('table.json','w') as table:
        json.dump(data,table)

def read_jason():
    with open('table.json','r') as table:
        content = json.load(table)

    print("Contenido")
    print(content)
    return content

def save_data(data):
    data_all = ""
    for row in data:
        for e in row:
            data_all = data_all + e + "|"
        data_all = data_all + "\n"
    print(data_all)
    write_jason(data_all)

def load(root):
    data = []
    with open(root,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row[0].split(";"))

    #save(data)
    #read_jason()
    csvfile.close()
    return data

