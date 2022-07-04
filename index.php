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
</head>
<body background="static/inicio.jpg">
    <div class="container" >
        
        <div class="card">
            <div class="card-header text-white bg-danger">

                <h1 class="display-1 text-center">Machine Learning</h1>
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="http://127.0.0.1:8000/cargar">Proyecto 2</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNavDropdown">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                 <a class="nav-link active" aria-current="page" href="Paginas/carga.php">Cargar Archivo CSV</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link active" aria-current="page" href="Paginas/Lineal.php">Regresion Lineal</a>
                                </li>                                
                                <li class="nav-item">
                                    <a class="nav-link" href="Paginas/Polinomial.php">Regresion Polinomial</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="Paginas/Arbol.php">Clasificador de árboles de decisión</a>
                                </li>                                
                                <li class="nav-item">
                                    <a class="nav-link" href="Paginas/Gaussiano.php">Clasificador Gaussiano</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="Paginas/Neuronal_Pred.php">Prediccion Neuronal</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="Paginas/Neuronal_Clasi.php">Clasificacion Neuronal</a>
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
    <footer class="footer">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-auto">
                    <p style="color: #9FFFEF;">© 2021 Copyright: Carlos Roberto Rangel Castillo</p>
                </div>
            </div>
        
        </div>
    </footer>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
</body>
</html>