# Instalación
Para el despliegue de este sistema podemos optar por dos opciones, un despliegue local utilizando la herramienta Docker Compose o un despliegue en remoto utilizando el proveedor PaaS Heroku, se recomienda especialmente este último método si el sensor y el servidor central se encuentran en diferentes redes ya que Heroku nos facilita exponer el servidor central a internet.

## Docker Compose
Antes de realizar este tipo de despliegue es necesario instalar las aplicaciones  [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/), ambas herramientas están disponibles para sistemas Linux, Mac y Windows.

También es necesario establecer algunas variables de entorno antes de realizar el despliegue, estas variables se establecerán en los ficheros indicados en las opciones `env_file` del fichero `docker-compose.yml`, por defecto  `web.env.sample` y `db.env.sample`.

`web.env`
  - **POSTGRES_USER**: Usuario principal que será creado en la base de datos y con el que contenedor del servicio web conectará.
  - **POSTGRES_PASSWORD**: Contraseña para el usuario especificado.


`db.env`
  - **FLASK_APP**: Módulo Python que arrancará la aplicación Flask. El valor debe ser `vedetra-server.py`.
  - **FLASK_ENV**: Define el tipo de servidor en el que se ejecutará `development`, `testing` o `production`. Por defecto `production`.
  - **FLASK_CONFIG**: Define la configuración de entorno que se cargará, puede tomar los valores `development`, `testing` o `production`. Por defecto `production`.
  - **DATABASE_URL**: Dirección de la base de datos (postgresql://<user>:<password>@db/vedetra).
  - **LOAD_DUMMY_DATA**: Cuando se establece a `true` realiza una carga de sensores y detecciones falsas en la base de datos para ver una demostración de la interfaz. Por defecto `false`
  - **PORT**: Puerto en el que se expondrá la aplicación web. Por defecto el puerto 5000.

Una vez satisfechos los prerrequisitos podemos proceder al despliegue, para ello desde el directorio principal del proyecto, donde se encuentra el fichero `docker-compose.yml`, podemos lanzar el siguiente comando que se encargará de construir la imagen y desplegar los contenedores.

```bash
$ docker-compose up --build
```

## Heroku
Para este despliegue es necesario disponer de una cuenta en [Heroku](https://www.heroku.com/), para desplegar estos recursos podemos utilizar la cuenta gratuita que nos ofrecen. También será necesario instalar la herramienta `Heroku CLI`, en sistemas Linux podemos instalarla con un simple comando:

```bash
$ curl https://cli-assets.heroku.com/install.sh | sh
```

Para otros métodos de instalación o sistemas operativos consultar la [documentación oficial](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Una vez creada la cuenta e instalada la herramienta `Heroku CLI` el primer paso será iniciar sesión usando el siguiente comando:

```bash
$ heroku login -i
```

El método de despliegue de Heroku se basa en subidas al repositorio Git de Heroku, por lo que si la copia que tenemos del proyecto no ha sido clonada del repositorio de GitHub el primer paso será inicializar un repositorio, para ello nos situamos en la raíz del proyecto y ejecutamos el siguiente comando:

```bash
$ git init
```

El siguiente paso será crear una aplicación de Heroku y especificar que se trata de una aplicación basada en contenedores. Al crear la aplicación se añadirá automáticamente a nuestro repositorio local un nuevo repositorio remoto con el nombre `heroku`.

```bash
$ heroku apps:create <nombre_app>
$ heroku stack:set container
```

Al igual que en el despliegue de Docker Compose tendremos que definir algunas variables de entorno, en este caso lo realizaremos mediante la CLI de Heroku, a continuación se muestran las variables a definir.

```bash
$ heroku config:set FLASK_APP=vedetra-server.py
$ heroku config:set FLASK_CONFIG=production
$ heroku config:set FLASK_ENV=production
```

A continuación crearemos el `addon` para PostgreSQL, automáticamente inyectará los datos de conexión al contenedor web mediante la variable de entorno `DATABASE_URL`.

```bash
$ heroku addons:create heroku-postgresql:hobby-dev
```

Una vez inicializados todos los componentes solo tendremos que crear un `commit` en el repositorio y subirlo al remoto de Heroku, en caso de haber clonado el respositorio de GitHub se pueden obviar los dos primero comandos.

```bash
$ git add -A
$ git commit -m "Despliegue inicial"
$ git push heroku master
```

Una vez finalizado el despliegue podemos abrir la aplicación en nuestro navegador predeterminado con el siguiente comando.

```bash
$ heroku apps:open
```

## Inicialización

Una vez arrancado el servidor central y el sensor será necesario crear una entrada para el sensor que realizará el envío de detecciones. Para ello podemos realizar una llamada a la API utilizando el comando `curl`, solo necesitamos la dirección del servidor y el identificador del sensor, las instrucciones para obtener este último dato se encuentran detalladas en la [documentación de instalación del sensor](https://github.com/adalsa91/tfg/blob/master/INSTALL.md).

```bash
$ curl --location --request POST 'http://<host>:<port>/api/v1.0/sensors/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "363daf8619557863c7b4f9767389cb6c",
    "description": "Sensor 1"
}'
```

