# promptior-ai-challenge-rgg

## cómo correr la app
Este repositorio contiene lo necesario para levantar un api y consultar qué hace Promptior y cuándo fue fundada. 
Para poder correr correctamente el serivcio, hay que agregar un .env que contenga la api key de open ai en un archivo llamado .env  El nombre de la variable debe ser: OPENAI_API_KEY. A modo de ejemplo, el archivo .env contendría lo siguiente: OPENAI_API_KEY="dummy-key-para-probar-esto"
Una vez creado el archivo .env, se debe ejecutar los comandos de docker build y docker run $id-de-la-imagen-anterior para levantar el servicio.

## descripción general del proyecto

## proceso de resolución
Básicamente, para desarrollar esta app se realizó un despliegue local. Una vez resueltas las principales dificultades, se procedió a su dockerización. La dockerización se hizo mediante pruebas en una ec2. Dentro de las dificultades principales, destacaron:

- familizariación con nuevas tecnologías
- despliegue en ubunut: acá importante considerar que es requerido python3.10 o superior (para instalar las dependencias de langchaing), tener Chrome y su correspondiente webdriver instalados (los cuales deben tener versiones compatibles), asegurarse que todas las librerías y paquetes requeridos estén dispnibles
- lectura del sitio de Pomptior, ya que al traer el contenido a través de un script obliga a la interacción para traer los html
- instalación de dependencias en el Dockerfile 

## diagrama de componentes

![Diagram](https:https://github.com/rgg1993/promptior-ai-challenge-rgg/Promptior.drawio.png)

# importante
No se recomienda el manejo de archivos .env dentro de docker. 
La solución aquí presentada es una prueba de desarrollo. 


