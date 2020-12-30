require('rootpath')()
const express = require('express')
const morgan = require('morgan')
const mongoose = require('mongoose')
const cors = require('cors')
const bodyParser = require('body-parser')
const jwt = require('./authentication/backend/_services/jwt')
const errorHandler = require('./authentication/backend/_services/error-handler')

const app = express();
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(cors())
app.use('/users', require('./authentication/backend/users/users-controller'))
app.use(errorHandler)

//Conexión con la base de datos, cuando se despliegue en servidor  se tendrá que cambiar la dirección
mongoose.connect('mongodb://omar:antonio1997@cluster0-shard-00-00-svm5b.mongodb.net:27017,cluster0-shard-00-01-svm5b.mongodb.net:27017,cluster0-shard-00-02-svm5b.mongodb.net:27017/TrabajoFinalCN?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')
  .then(db => console.log('DB conectada')) //Imprimir DB conectada en caso de que todo vaya bien
  .catch(err => console.error(err)); //Imprime error si no se puedo conectar

//Ajustes

    //Si el servidor tiene puerto lo coge sino pone el puerto 4100
    app.set('port', process.env.PORT || 4100  );

  //Middlewares
  //Sirve para imprimir las peticiones Get de la consola
  app.use(morgan('dev'));
  //Body-parser viene integrado con express (sirve para trabajar con los json)
  app.use(express.json());

//Routes
    //Ruta donde se encuentran las funciones de la base de datos TODAS (insertar/eliminar/modificar)
    app.use('/api/CosasDeClase/Producto',require('./routes/Producto'));

//Ficheros estáticos, coge el index.html dentro de public
app.use(express.static(__dirname + '/public'));

//Sever escucha en el puerto x te lo muestra por pantalla
app.listen(app.get('port'), () =>{
    console.log('Client on port', app.get('port'));
});