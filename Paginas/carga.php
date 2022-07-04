<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <title>
        Machine Learning
    </title>
    <script>
      var abrirArchivo = function(event){
          var archivo = event.target;
          var reader = new FileReader();
          reader.onload = function(){
              var contenido = reader.result;
              document.getElementById("texto").innerHTML = contenido;
              console.log(contenido);
              json_peticion = JSON.stringify({contenido:contenido});
              let respuesta = fetch("https://olc2-p2-201907636-backend.herokuapp.com/AnalizarCSV",{
                  method: 'POST',
                  body: json_peticion,
                  headers: {'Content-Type':'application/json'}
              })
              console.log(respuesta)
              alert("Archivo Cargado exitosamente")
          };
          reader.readAsText(archivo.files[0])
      };
    </script>
</head>
<body background="static/inicio.jpg">
    <div class="container" >
        
        <div class="card">
            <div class="card-header text-white bg-danger">

                <h1 class="display-1 text-center">Machine Learning</h1>
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="http://127.0.0.1:8000/cargar">Proyecto 2 OLC2</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNavDropdown">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                 <a class="nav-link active" aria-current="page" href="carga.php">Cargar Archivo CSV</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link active" aria-current="page" href="Lineal.php">Regresion Lineal</a>
                                </li>                                
                                <li class="nav-item">
                                    <a class="nav-link" href="Polinomial.php">Regresion Polinomial</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="Arbol.php">Clasificador de árboles de decisión</a>
                                </li>                                
                                <li class="nav-item">
                                    <a class="nav-link" href="Gaussiano.php">Clasificador Gaussiano</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="Neuronal_Pred.php">Prediccion Neuronal</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="Neuronal_Clasi.php">Clasificacion Neuronal</a>
                                </li>
                                <li class="nav-item dropdown">
                                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                       Peticiones
                                    </a>
                                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                        <li><a class="dropdown-item" href="http://127.0.0.1:8000/CME">Canciones mas escuchadas</a></li>
                                        <li><a class="dropdown-item" href="http://127.0.0.1:8000/">Artistas mas reproducidos</a></li>
                                        <li><a class="dropdown-item" href="http://127.0.0.1:8000/Clasificacion">Clasificacion</a></li>
                                        <li><a class="dropdown-item" href="http://127.0.0.1:8000/">Listas mas escuchadas</a></li>
                                        <li><a class="dropdown-item" href="http://127.0.0.1:8000/">Listas mas populares</a></li>
                                    </ul>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="http://127.0.0.1:8000/ayuda">Ayuda</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </div>
    <div class="row">
      <form action="" method="post" enctype="multipart/form-data">
          <div class="mb-3">
              <p class="h2">Cargar Archivo</p>
              <div class="input-group mb-3">
                <input type = 'file' id = 'archivoT'>
              </div>
          </div>
      </form>
      <div class="col-sm-6">
          <div class="card">
          <div class="card-body">
              <h5 class="card-title">Entrada</h5>
              <div class="form-floating">
                <textarea id = "contenido" class="form-control style="height: 360px"></textarea>
              </div>
              <form action="/enviar" method="post" enctype="multipart/form-data">
              <input type="submit" value="Enviar" class="btn btn-dark btn-m">
              </form>
          </div>
          </div>
      </div>
      <div class="col-sm-6">
          <div class="card">
          <div class="card-body">
              <h5 class="card-title">Salida</h5>
              <div class="form-floating">
                  <textarea class="form-control" placeholder="Leave a comment here" id="salida" style="height: 360px"></textarea>
              </div>
              <form action="/reset" method="post" enctype="multipart/form-data">
              <input type="submit" value="Reset" class="btn btn-danger btn-m">
              </form>
          </div>
          </div>
      </div>
  </div>
    <footer class="footer">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-auto">
                    <p style="color: #9FFFEF;">© 2021 Copyright: Carlos Roberto Rangel Castillo</p>
                </div>
            </div>
        </div>
    </footer>
    <button onclick="metodo()">Enviar</button>
    <input id="cuadro" type="text" name="tipo_de_dato"/>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
<script>
    let info;
    var archi;
    let nombreArchivo;
    let prueba;
    function abrir(ev){
      let arch = ev.target.files[0];
      if (arch){
         let reader = new FileReader();
          reader.onload = function(a){
              let contenido = a.target.result;
              texto = document.getElementById("contenido");
              texto.value = contenido;
              console.log(contenido);
              json_peticion = JSON.stringify({contenido:contenido});
              let respuesta = fetch("https://olc2-p2-201907636-backend.herokuapp.com/AnalizarCSV",{
                method: 'POST',
                body: json_peticion,
                headers: {'Content-Type':'application/json'}
            })
              alert("Archivo Cargado exitosamente")
            };
          reader.readAsText(arch);
      }
      }
      window.addEventListener('load', () =>{
      document.getElementById('archivoT').addEventListener('change', abrir);        
  });
</script>
<script>
    function metodo(){    
        alert("Prueba");               
        let xhr = new XMLHttpRequest();
        //var ruta = "http://127.0.0.1:3000/AnalizarCSV";
        xhr.open('POST', ruta);
        xhr.send()
        xhr.onreadystatechange = (e) => {
            var peliculas = JSON.parse(xhr.responseText);

            document.getElementById("peliculas").innerHTML = peli;
        }
    }
</script>

</body>
</html>