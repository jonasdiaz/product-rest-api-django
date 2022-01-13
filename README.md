# product-rest-api-django

Author: Jonás Diaz Monachesi - jonas.diaz0@gmail.com

<strong>Para empezar</strong>.

Es necesario tener instalado docker y docker-compose. <a>https://docs.docker.com/engine/install/</a>

En la raíz ejecutar <code>mkdir .envs/production </code>.

Dentro de la misma crear los archivos <code>.django</code> y <code>.postgres</code>.

En el archivo <code>.postgres</code> poner los datos de ejemplo que dejo a continuación:

<code>POSTGRES_HOST=postgres</code><br>
<code>POSTGRES_PORT=5432</code><br>
<code>POSTGRES_DB=test</code><br>
<code>POSTGRES_USER=test</code><br>
<code>POSTGRES_PASSWORD=test1234</code><br>

Para finalizar ejecutar <code>docker-compose up --build</code> para arrancar el proyecto.
