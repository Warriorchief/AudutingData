import csv
import pprint
CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes={}
    with open(filename,'r') as f:
        reader=csv.reader(f)
        headers=reader.next()
        reader.next()
        reader.next()
        reader.next()
        columns={}
        for j in headers:
            columns[j]=[]
        H=len(headers)
        print 'number of categories:',H
        for row in reader:
            for i in range(H):
                columns[headers[i]].append(row[i])       
        #print columns.keys()
        for field in fields:
            data=columns[field]
            types=[]
            for d in data:
                if d=='NULL':
                    types.append(type(None))
                    continue
                if d[0]=='{':
                    types.append(type([5,6,7]))
                    continue
                try:
                    int(d)
                    types.append(type(int(d)))
                except ValueError:
                    try:
                        float(d)
                        types.append(type(float(d)))
                    except ValueError:
                        types.append(type('donkey'))
            #print 'types is:',types
            fieldtypes[field]=set(types)
        return fieldtypes
            

    

fieldtypes=audit_file(CITIES,FIELDS)
for key in fieldtypes.keys():
    print fieldtypes[key]


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
#test()