#se usó este link https://medium.com/@robertopreste/from-xml-to-pandas-dataframes-9292980b1c1c
import xml.etree.ElementTree as ET
import requests
import pandas as pd 
df_cols=["GHO","COUNTRY", 
                 "SEX", 
                 "YEAR",
                 "GHECAUSES", 
                 "AGEGROUP", 
                 "Display",
                "Numeric", 
                 "Low", 
                 "High"]
countries=["USA","CHL","ITA","MEX","BRA","MLT"]
useful = ["Number of deaths", 
            "Number of infant deaths", 
            "Number of under-five deaths", 
           "Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)",
           "Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)",
           "Estimates of number of homicides",
           "Crude suicide rates (per 100 000 population)",
           "Mortality rate attributed to unintentional poisoning (per 100 000 population)",
           "Number of deaths attributed to non-communicable diseases, by type of disease and sex",
           "Estimated road traffic death rate (per 100 000 population)",
           "Estimated number of road traffic deaths",
           "Mean BMI (kg/m&#xb2;) (crude estimate)",
           "Mean BMI (kg/m&#xb2;) (age-standardized estimate)",
           "Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)",
           "Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)",
           "Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)",
           "Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)",
           "Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)",
           "Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)",
           "Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)",
           "Estimate of daily cigarette smoking prevalence (%)",
           "Estimate of daily tobacco smoking prevalence (%)",
           "Estimate of current cigarette smoking prevalence (%)",
           "Estimate of current tobacco smoking prevalence (%)",
           "Mean systolic blood pressure (crude estimate)",
           "Mean fasting blood glucose (mmol/l) (crude estimate)",
           "Mean Total Cholesterol (crude estimate)"
          ]
for c in countries:
    rows = []
    request = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_"+c+".xml"
    r=requests.get(request)
    tree=ET.fromstring(r.content)
    name=c +"txt"
    #root=tree.getroot()
    for node in tree:
        if node.find('GHO').text is not None and not pd.isna(node.find('GHO').text) :
            fact=node.find('GHO').text.strip()
            #print(fact)
            #print(type(fact))
            if fact in useful:
                        #print(fact)
                        #rows.append({fact:}])
                        #for x in child:
                            #print(x.text)
                        #  pass
                        #print(node.tag)
                        for x in node:
                             if x.tag=="AGEGROUP" and x.text is not None:
                                #agegroup=x.text
                                #rows.append({"AGEGROUP": agegroup })
                                print(x.text)
                        # rows.append({"GHO": fact})
                        # if node.find("COUNTRY") is not None  and node.find("COUNTRY").text is not None and not pd.isna(node.find('COUNTRY').text):
                        #     country = str(node.find("COUNTRY").text) if node is not None else None
                        # else:
                        #     country=None
                        # if node.find("SEX") is not None and node.find("SEX").text is not None and not pd.isna(node.find('SEX').text):
                        #     sex = node.find("SEX").text  #if node is not None else None
                        #     rows.append({"SEX": sex })
                        # else:
                        #     sex=None
                        # if node.find("YEAR") is not None and node.find("YEAR").text is not None and not pd.isna(node.find('YEAR').text):
                        #     year = node.find("YEAR").text  #if node is not None else None
                        #     rows.append({"YEAR": year })
                        # if node.find("GHECAUSES")  and node.find("GHECAUSES").text is not None and not pd.isna(node.find('GHECAUSES').text):
                        #     ghecauses = node.find("GHECAUSES").text  #if node is not None else None
                        #     rows.append({"GHECAUSES": ghecauses })
                        if node.find("AGEGROUP") and node.find("AGEGROUP").attrib is not None :
                             agegroup = str(node.find("AGEGROUP").text)  if node is not None else None
                             rows.append({"AGEGROUP": agegroup })
                        # if node.find("Display") and node.find("Display").text is not None and not pd.isna(node.find('Display').text):
                        #     display = node.find("Display").text  #if node is not None else None
                        #     rows.append({"Display": display })
                        # if node.find("Numeric")  and not pd.isna(node.find('Numeric').text):
                        #     numeric = node.find("Numeric").text  #if node is not None else None
                        #     rows.append({"Numeric": numeric })
                        # if node.find("Low")  and not pd.isna(node.find('Low').text):
                        #     low = node.find("Low").text  #if node is not None else None
                        #     rows.append({"Low": low })
                        # if node.find("High")  and not pd.isna(node.find('High').text):
                        #     high = node.find("High").text  #if node is not None else None
                        #     rows.append({"High": high })
                        # #print(fact)

    out_df = pd.DataFrame(rows, columns = df_cols)
    print(out_df)
   # out_df=out_df.astype({"GHO":str,
        #        "COUNTRY":str, 
        #         "SEX":str, 
         #        "YEAR":int,
          #       "GHECAUSES":str, 
          #       "AGEGROUP":str, 
            #     "Display":str,
            #     "Numeric":int, 
            #      "Low":int, 
            #     "High":int})
    print(out_df)
