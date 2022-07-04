import pandas as pd;
import os
'''with open('Petrol Dataset June 20 2022.xls') as File:
    x = File.readline()
separar = x.split(",")
tupla_report = dict.fromkeys(separar).keys()
seleccion = str(input("Seleccione el dato para Y: "))
seleccion2 = seleccion.upper()
print(seleccion2)
for i in tupla_report:
    if(str(i).upper().strip(" ") == seleccion2.strip(" ")):
            print("Se selecciono la columna: " + str(i) + " para los datos en Y")
            df = pd.read_excel('Petrol Dataset June 20 2022.xls', engine='xlrd')
            print(df)
    else:
        print("No se encontro alguna columna con ese nombre")'''
path = 'Petrol Dataset June 20 2022.xls'
root, extension = os.path.splitext(path)
#excel = pd.read_excel('Petrol Dataset June 20 2022.xls') #<-- Excel file that saved as xlsx
file = open(path)
if extension == 'xlsx':
    df = pd.read_excel(file.read(), engine='openpyxl')
    print(df)
elif extension == "xls":
    df = pd.read_excel(file.read())
    print(df)
elif extension == 'csv':
    df = pd.read_csv(file.read())
    print(df)
elif extension == 'json':
    print("")


