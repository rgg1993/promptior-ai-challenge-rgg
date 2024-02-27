# promptior-ai-challenge-rgg

## cómo correr la app
Este repositorio contiene lo necesario para levantar un api y consultar qué hace Promptior y cuándo fue fundada. 
Para poder correr correctamente el servicio, hay que clonar el repositorio y luego agregar un archivo llamado .env que contenga la api key de open ai. El nombre de la variable en el archivo .env debe ser: OPENAI_API_KEY. A modo de ejemplo, el archivo .env contendría lo siguiente: OPENAI_API_KEY="dummy-key-para-probar-esto". Una vez creado el archivo .env, se deben ejecutar los comandos de "docker build . " y "docker run".

## descripción general del proyecto
El proyecto procura desplegar un bot en una api en la cual el usuario pueda realizarle preguntas sobre la empresa Promptior. 
Aún asi, se puede adaptar y hacer que responda preguntas sobre cualquier otra web, siempre y cuando se modifique el código del archivo retrieve_web_page_contents.py. Es un proyecto en su versión beta, por lo cual no se recomienda utilizar el código aquí presente para desplegar en ambientes productivos sin previa validación. 

## proceso de resolución
Básicamente, para desarrollar esta app se realizó un despliegue local. Una vez resueltas las principales dificultades, se procedió a su dockerización. La dockerización se hizo mediante pruebas en una ec2 en AWS. Dentro de las dificultades principales, destacaron:

- familiarización con nuevas tecnologías  (primvera vez trabajando con langchain y selenium)
- despliegue en ubuntu: acá importante considerar que es requerido python3.10 o superior (para instalar las dependencias de langchain), tener Chrome y su correspondiente webdriver instalados (los cuales deben tener versiones compatibles), asegurarse que todas las librerías y paquetes requeridos estén dispnibles
- lectura del sitio de Pomptior, ya que la web carga el html a través de un script js que obliga a la interacción para poder traer los html
- instalación de dependencias en el Dockerfile 

## diagrama de componentes

![diagrama de componentes](https://github.com/rgg1993/promptior-ai-challenge-rgg/blob/main/diagram.png)

# importante
No se recomienda el manejo de archivos .env dentro de docker. 
La solución aquí presentada es una prueba de desarrollo. 



