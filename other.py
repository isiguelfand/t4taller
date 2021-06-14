#se usó este link https://medium.com/@robertopreste/from-xml-to-pandas-dataframes-9292980b1c1c
import xml.etree.ElementTree as ET
import requests
import pandas as pd 
import gspread
import httplib2
import os
from gspread_dataframe import set_with_dataframe
gc = gspread.service_account(filename="credentials.json")
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
countries_link={"USA":"1r9xnc7i84ABjTkKRIX2BodmA3dTEcPuNf713jVujIbc",
            "CHL":"11Bn61ImxL3Cr7clY6-pvvbzKbWF9k3qPHTCv7nhvaV0",
            "ITA":"1zXPRnpO_-B47-ACeoDOeQe-F4f4jfDzRwvHaHoBLWrA",
            "MEX":"1imk2klz0ldH5q4ZSeXIkOBMbf3wBPeyBto5TxUEA7co",
            "BRA":"10ApWKOKXb59K-beaVJqT8xfA3l8ssOq3mKuOqZiPff0",
            "MLT":"1dBYrnpAKoowrXt89-iT-nEFO5QVDIRYk8YxXw_8636M"}
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
rows = []
for c in countries:
    request = "http://tarea-4.2021-1.tallerdeintegracion.cl/gho_"+c+".xml"
    r=requests.get(request)
    tree=ET.fromstring(r.content)
    name=c +".txt"
    #root=tree.getroot()
    for node in tree:
        if node.find('GHO').text is not None and not pd.isna(node.find('GHO').text) :
            fact=node.find('GHO').text.strip()
            #print(fact)
            #print(type(fact))
            if fact in useful:
                        gho = fact
                        for y in node:
                             if y.tag=="AGEGROUP" and y.text is not None:
                                print(y.text)
                                agegroup=y.text

                        country = node.find("COUNTRY").text if node.find("COUNTRY") is not None else None
                        sex = node.find("SEX").text if node.find("SEX") is not None else None
                        year = node.find("YEAR").text if node.find("YEAR") is not None else None
                        ghecauses = node.find("GHECAUSES").text if node.find("GHECAUSES") is not None else None
                        age=[]
                                #age.append(y.text)
                            #agegroup = node.find("AGEGROUP").text if node.find("AGREGROUP") is not None else None
                        #agegroup=age    
                        display = str(node.find("Display").text) if node.find("Display") is not None else None
                        numeric = float(node.find("Numeric").text) if node.find("Numeric") is not None else None
                        low = float(node.find("Low").text) if node.find("Low") is not None else None     
                        high = float(node.find("High").text) if node.find("High") is not None else None                                                             
                        rows.append({"GHO":fact,
                        "COUNTRY":country, 
                        "SEX":sex, 
                        "YEAR":year,
                        "GHECAUSES":ghecauses ,
                        "AGEGROUP":agegroup, 
                        "Display":display,
                        "Numeric":numeric, 
                        "Low":low, 
                        "High":high})
    
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
out_df = pd.DataFrame(rows, columns = df_cols)
sh = gc.open_by_key(countries_link["CHL"])
ws=sh.get_worksheet(0)
set_with_dataframe(ws, out_df)
