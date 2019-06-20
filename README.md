# Vedetra Server



[![Build Status](https://travis-ci.org/adalsa91/vedetra-server.svg?branch=master)](https://travis-ci.org/adalsa91/vedetra-server)
[![codecov](https://codecov.io/gh/adalsa91/vedetra-server/branch/master/graph/badge.svg)](https://codecov.io/gh/adalsa91/vedetra-server)

Sistema para recolección y consulta de detecciones de dispositivos WiFI mediante API REST, también dispone de una interfaz web para visualizar los datos.

El sistema consta de dos servicios: el servidor web desarrollado con [Flask](http://flask.pocoo.org/) y un servicio de  base de datos ([PostgreSQL](https://hub.docker.com/_/postgres)).
### Prerrequisitos

Seguir las instrucciones oficiales para instalar Docker y Docker Compose.

[Docker](https://docs.docker.com/install/)

[Docker Compose](https://docs.docker.com/compose/install/)

### Instalación

Clonar el repositorio

``` bash
git clone https://github.com/adalsa91/vedetra-server.git
cd vedetra-server
```

Crear imágenes
``` bash
docker-compose build
```

Arrancar entorno de desarrollo
``` bash
docker-compose -f "docker-compose.yml" -f "docker-compose-dev.yml" up
```
El entorno de desarrollo crea un volumen en el contenedor enlazado a tu copia local de la aplicación para poder hacer modificaciones sin necesidad de volver a crear la imagen.

:warning: __Warning__ No usar `docker-compose-dev.yml` en producción.

### Variables de entorno

Las variables de entorno se pasan a los contenedores a través de los ficheros especificados en la directiva ```env_file``` de los ficheros ```docker-compose*.yml```.

Se puede consultar las variables a definir en los ejemplos [web.env.sample](web.env.sample) y [db.env.sample](db.env.sample).


### Lanzar tests
``` bash
docker-compose run --name db -d db
docker-compose run vedetra flask test
```