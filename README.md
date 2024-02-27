# promptior-ai-challenge-rgg

## Cómo correr la aplicación
Este repositorio contiene los archivos necesarios para levantar una API que permite consultar información sobre Promptior, incluyendo su descripción y fecha de fundación. Para ejecutar el servicio correctamente, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
2. Crea un archivo llamado `.env` en la raíz del proyecto y agrega la API Key de OpenAI. La variable en el archivo `.env` debe llamarse `OPENAI_API_KEY`. Por ejemplo: `OPENAI_API_KEY="dummy-key-para-probar-esto"`
3. Una vez creado el archivo `.env`, ejecuta los siguientes comandos en la terminal:

'''
docker build -t promptior-ai-challenge .
docker run -d -p 80:8000 promptior-ai-challenge
'''

## Descripción general del proyecto
El proyecto consiste en desplegar un bot en una API que permite a los usuarios hacer preguntas sobre la empresa Promptior. Si bien está diseñado específicamente para Promptior, el código puede ser modificado para que responda preguntas sobre cualquier otro tema. Es importante tener en cuenta que este proyecto se encuentra en versión beta, por lo que no se recomienda su uso en entornos de producción sin una validación previa.

## Proceso de resolución
El desarrollo de esta aplicación comenzó con una implementación local. Una vez resueltas las principales dificultades, se procedió a su dockerización. Las principales dificultades encontradas fueron:

- Familiarización con nuevas tecnologías (primera vez trabajando con langchain y selenium).
- Despliegue en Ubuntu: se requiere Python 3.10 o superior (para instalar las dependencias de langchain), Chrome y su correspondiente WebDriver instalados, así como asegurarse de que todas las librerías y paquetes necesarios estén disponibles.
- Lectura del sitio de Promptior, ya que la web carga el HTML a través de un script JS que requiere interacción para poder traer los datos.
- Instalación de dependencias en el Dockerfile.

## diagrama de componentes

![diagrama de componentes](https://github.com/rgg1993/promptior-ai-challenge-rgg/blob/main/diagram.png)

# Importante
No se recomienda manejar archivos `.env` dentro de Docker. Esta solución es únicamente para fines de desarrollo y pruebas.