import xml.etree.ElementTree as ET
import requests
countries=["USA","CHL","ITA","MEX","BRA","MLT"]
for c in countries:
    request = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_"+c+".xml"
    r=requests.get(request)
    tree=ET.fromstring(r.content)
    useful=[]
    name=c +".txt"
    textfile=open(name,"w")
    #root=tree.getroot()
    for child in tree:
        if child.find('GHO').text is not None:
            fact=child.find('GHO').text
            if fact not in useful:
                useful.append(fact)

        for x in child:
            #print(x.text)
            pass
    for element in useful:
        textfile.write(element + "\n")
    textfile.close()