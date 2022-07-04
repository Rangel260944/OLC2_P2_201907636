from flask import Flask, request, jsonify
import json
from flask_cors import CORS, cross_origin
import os
from numpy import array, r_
import pandas as pd
import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB;
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LinearRegression;
from sklearn.preprocessing import PolynomialFeatures;
from sklearn.metrics import mean_squared_error, r2_score;
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def inicio():
    contanera = ""
    for i in range(0, 100):
        contanera += "<h1>"+ str(i) + "<h1>" + "\n"
    with open("Prueba.txt", "w", encoding="utf-8") as f:
        f.write(contanera)
        f.close()
    with open("Prueba.txt", "r", encoding="utf-8") as f:
        x = f.readlines()
    entrada = ""
    for j in x:
        entrada += j
    return entrada

@app.route('/menu', methods=['GET'])
def menu():
    return "<h1>Bienvenido al menu</h1>"

@app.route('/AnalizarCSV', methods=['POST'])
def Analizar():
    cuerpo = request.get_json()
    contenido = cuerpo['contenido']
    with open("salida.txt", "w", encoding="utf-8") as f:
        contenidot = contenido.replace("\"", "")
        f.write(contenidot)
        f.close()         
    read_file = pd.read_csv (r'salida.txt', error_bad_lines=False)
    read_file.to_csv (r'Entrada.csv', index=None)
    #print(contenido)
    #filas = contenido.split("\r\n")
    return "Archivo Cargado Exitosamente"

@app.route('/RegresionLineal', methods=['POST'])
def RL():
    cuerpoRL = request.get_json()
    Eje_x = cuerpoRL['eje_x']
    print(Eje_x)
    Eje_y = cuerpoRL['eje_y']
    print(Eje_y)
    Prediccion = cuerpoRL['prediccion']
    print(Prediccion)
    data = pd.read_csv("Entrada.csv");
    X = np.asarray(data[Eje_x]).reshape(-1, 1);
    Y = data[Eje_y];
    linear_regression = LinearRegression();
    linear_regression.fit(X, Y);
    Y_pred = linear_regression.predict(X);  
    r_2 = r2_score(Y, Y_pred)
    coeficiente = linear_regression.coef_
    error_medio = mean_squared_error(Y, Y_pred, squared=True)
    titulo = 'Prediccion = {}; Coeficiente = {}; R2 = {}'.format(Y_pred, round(coeficiente[0],2), round(r_2,2))
    plt.title("Prueba\n" + titulo, fontsize=10)
    print(Y_pred);
    print("Error medio: ", mean_squared_error(Y, Y_pred, squared=True));
    print("Coef: ", linear_regression.coef_);
    print("R2: ", r_2);
    plt.scatter(X, Y);
    #plt.plot(X, Y_pred, color='red');
    plt.savefig("Regresion.png")
    Y_new = linear_regression.predict([[int(Prediccion)]]);
    print(Y_new);
    return jsonify({"mensaje":"Regresion Lineal Ejecutada con Exito :D"})

@app.route('/RegresionPolinomial', methods=['POST'])
def RP():
    cuerpoRP = request.get_json()
    Eje_x = cuerpoRP['eje_x']
    print(Eje_x)
    Eje_y = cuerpoRP['eje_y']
    print(Eje_y)
    Prediccion = cuerpoRP['prediccion']
    print(Prediccion)
    Grado = cuerpoRP['grado']
    print(Grado)
    data = pd.read_csv("Entrada.csv");
    x = np.asarray(data[Eje_x]).reshape(-1, 1);
    y = np.asarray(data[Eje_y]).reshape(-1, 1);
    plt.scatter(x,y)
    poly_degree = int(Grado)
    polynomial_features = PolynomialFeatures(degree = poly_degree)
    x_transform = polynomial_features.fit_transform(x)
    model = LinearRegression().fit(x_transform, y)
    y_new = model.predict(x_transform)
    rmse = np.sqrt(mean_squared_error(y, y_new))
    print("RMSE: " + str(rmse))
    r2 = r2_score(y, y_new)
    print("R2: " + str(r2))
    x_new_min = -x.min()
    x_new_max = x.max()
    x_new = np.linspace(x_new_min, x_new_max, 50)
    x_new = x_new[:,np.newaxis]
    x_new_transform = polynomial_features.fit_transform(x_new)
    y_new = model.predict(x_new_transform)
    print(y_new)
    plt.plot(x_new, y_new, color='coral', linewidth=3)
    plt.grid()
    plt.xlim(x.min(),x_new_max)
    plt.ylim(y.min(),y.max())
    print(y.min())
    print(y.max())
    title = 'Degree = {}; RMSE = {}; R2 = {}'.format(poly_degree, round(rmse,2), round(r2,5))
    plt.title("\n " + title, fontsize=10)
    plt.xlabel(str(Eje_x))
    plt.ylabel(str(Eje_y))   
    plt.savefig("Paginas/static/Regresion_Polinomial.png")
    plt.clf()
    #print(X)
    #print(Y)
    #poly = PolynomialFeatures(degree=int(Grado));
    #X = poly.fit_transform(X)
    #Y = poly.fit_transform(Y);
    #linear_regression = LinearRegression();
    #linear_regression.fit(X, Y);
    #Y_pred = linear_regression.predict(X);
    #plt.scatter(X, Y);
    #plt.plot(X, Y_pred, color='red');
    #Y_new = linear_regression.predict(poly.fit_transform([[int(Prediccion)]]));
    return jsonify({"mensaje":"Regresion Polinomial Ejecutada con Exito :D"})

@app.route('/ArbolDecision', methods=['POST'])
def AD():
    array_features = []
    data = pd.read_csv("Entrada.csv");
    cuerpoAR = request.get_json()
    Prediccion = cuerpoAR['prediccion']
    Rango = cuerpoAR['rango']
    Separar = Rango.split("-")
    inicio = int(Separar[0])
    final = int(Separar[1])
    le = preprocessing.LabelEncoder()
    pred = np.asarray(data[Prediccion]).reshape(-1, 1);
    label = le.fit_transform(pred)
    for i in range(inicio, final+1):
        temp = data.iloc[:, i].values.reshape(-1, 1)
        temporal = le.fit_transform(temp)
        array_features.append(temporal)
    print(array_features)
    features=list(zip(*array_features))
    print(features)
    clf = DecisionTreeClassifier().fit(features, label)  
    plot_tree(clf, filled=True)
    plt.savefig("Arbol_Supervisado.png")
    return jsonify({"mensaje":"Arbol de desicion ejecutado con Exito :D"})  
   
@app.route('/ArbolNoSupervisado', methods=['POST'])
def ANS():
    array_features = []
    data = pd.read_csv("Entrada.csv");
    cuerpoAR = request.get_json()
    Rango = cuerpoAR['rango']
    Separar = Rango.split("-")
    inicio = int(Separar[0])
    final = int(Separar[1])
    le = preprocessing.LabelEncoder()
    for i in range(inicio, final+1):
        temp = data.iloc[:, i].values.reshape(-1, 1)
        temporal = le.fit_transform(temp)
        array_features.append(temporal)
    print(array_features)
    features=list(zip(*array_features))
    print(features)
    clf = DecisionTreeClassifier().fit(features)  
    plot_tree(clf, filled=True)
    plt.savefig("Arbol_No_Supervisado.png")
    return jsonify({"mensaje":"Arbol de desicion ejecutado con Exito :D"}) 
        
@app.route('/Gaussiano', methods=['POST'])
def Gauss():  
    array_features = []
    data = pd.read_csv("Entrada.csv");
    cuerpoAR = request.get_json()
    Prediccion = cuerpoAR['prediccion']
    campo = cuerpoAR['campo']
    #new_campo =  campo.replace("\'", "")
    split_campo = campo.split(",")
    print(split_campo)
    tama = len(split_campo)
    pred = data.iloc[:, int(Prediccion)].values;
    print(pred)
    Rango = cuerpoAR['rango']
    Separar = Rango.split("-")
    inicio = int(Separar[0])
    final = int(Separar[1])
    le = preprocessing.LabelEncoder()
    label = le.fit_transform(pred)
    for i in range(inicio, final+1):
        temp = data.iloc[:, i].values.reshape(-1, 1)
        temporal = le.fit_transform(temp)
        array_features.append(temporal)
    features=list(zip(*array_features))
    print(features)
    model = GaussianNB(); 
    model.fit(features, label);
    if tama == 1:
        predict = model.predict([[split_campo[0]]])
        print(predict)
    elif tama == 2:
        predict = model.predict([[split_campo[0],split_campo[1]]])
        print(predict)
    elif tama == 3:
        predict = model.predict([[split_campo[0],split_campo[1],split_campo[2]]])
        print(predict)
    elif tama == 4:
        predict = model.predict([[int(split_campo[0]),int(split_campo[1]),int(split_campo[2]),int(split_campo[3])]])
        print(predict)
    elif tama == 5:
        predict = model.predict([[split_campo[0],split_campo[1],split_campo[2],split_campo[3],split_campo[4]]])
        print(predict)
    elif tama == 6:
        predict = model.predict([[split_campo[0],split_campo[1],split_campo[2],split_campo[3],split_campo[4],split_campo[5]]])
        print(predict)
    elif tama == 7:
        predict = model.predict([[split_campo[0],split_campo[1],split_campo[2],split_campo[3],split_campo[4],split_campo[5],split_campo[6]]])
        print(predict)
    elif tama == 8:
        predict = model.predict([[split_campo[0],split_campo[1],split_campo[2],split_campo[3],split_campo[4],split_campo[5],split_campo[6],split_campo[7]]])
        print(predict)
    elif tama == 9:
        predict = model.predict([[split_campo[0],split_campo[1],split_campo[2],split_campo[3],split_campo[4],split_campo[5],split_campo[6],split_campo[7],split_campo[8]]])
        print(predict)
    elif tama == 10:
        predict = model.predict([[split_campo[0],split_campo[1],split_campo[2],split_campo[3],split_campo[4],split_campo[5],split_campo[6],split_campo[7],split_campo[8],split_campo[9]]])
        print(predict)
    return jsonify({"mensaje":"Gaussiano ejecutado con Exito :D"})


@app.route('/NeuronalPred', methods=['POST'])
def NP():
    data = pd.read_csv("Entrada.csv")
    cuerpoNP = request.get_json()
    Eje_x = cuerpoNP['eje_x']
    Eje_y = cuerpoNP['eje_y']
    Prediccion = cuerpoNP['prediccion']
    x = np.asarray(data[Eje_x]).reshape(-1,1)
    y=data[Eje_y]
    x_train, x_test, y_train, y_test = train_test_split(x,y)
    net = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(3,3), random_state=1)
    net.fit(x_train, y_train)
    pred =net.predict(np.array([int(Prediccion)]).reshape(1,1))
    print(pred)         
    return jsonify({"mensaje":"Prediccion Neuronal ejecutada con Exito :D"})


@app.route('/NeuronalClasi', methods=['POST'])
def NC():
    arrary_aux = []
    encoder = LabelEncoder()
    data = pd.read_csv("Entrada.csv")
    cuerpoNC = request.get_json()
    Eje_x = cuerpoNC['eje_x']
    Eje_y = cuerpoNC['eje_y']
    new_x = Eje_x.replace("\"", "")
    Separador_x = new_x.split(",")
    tama = len(Separador_x)
    #for i in Separador_x:
     #   print(i)
     #   temporal = encoder.fit_transform(data[i].values)
     #   print(temporal)
      #  arrary_aux.append(temporal)
    #print(arrary_aux)
    X = data[[]]
    if tama == 1:
        temporal = encoder.fit_transform(data[Separador_x[0]].values)
        X = data[[temporal]]
    elif tama == 2: 
        X = data[[Separador_x[0],Separador_x[1]]]
    elif tama == 3: 
        data[str(Separador_x[0])] = encoder.fit_transform(data[Separador_x[0]].values)
        data[str(Separador_x[1])] = encoder.fit_transform(data[Separador_x[1]].values)
        data[str(Separador_x[2])] = encoder.fit_transform(data[Separador_x[2]].values)
        X = data[[str(Separador_x[0]),str(Separador_x[1]),str(Separador_x[2])]]
    elif tama == 4: 
        X = data[[Separador_x[0],arrary_aux[1],Separador_x[2],Separador_x[3]]]  
    elif tama == 5: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4]]] 
    elif tama == 6: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4],Separador_x[5]]]
    elif tama == 7: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4],Separador_x[5],Separador_x[6]]]
    elif tama == 8: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4],Separador_x[5],Separador_x[6],Separador_x[7]]]
    #print(Separador_x)
    y = data[Eje_y]
    #print(X)
   # print(y)
    X_train, X_test, y_train, y_test = train_test_split(X,y)
    scaler = StandardScaler()
    scaler.fit(X_train)
    print("**************************************************")
    print(X_train)
    print("**************************************************")
    X_train = scaler.transform(X_train)

    X_test = scaler.transform(X_test)
    net = MLPClassifier(hidden_layer_sizes = (100,), max_iter=500000, alpha=0.0001, solver='adam',
                    random_state=21, tol=0.000000001)
    net.fit(X_train, y_train)
    predictions=net.predict(X_test)
    print(classification_report(y_test,predictions))
    return jsonify({"mensaje":"Clasificacion Neuronal ejecutada con Exito :D"}) 


if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=puerto)
  #  app.run(debug=True, port=3000)