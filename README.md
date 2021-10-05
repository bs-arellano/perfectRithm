

## PERFECT RITHM
Proyecto:  Juego Perfect Rithm v1


#### MODELOS DE PROGRAMACIÓN 2

Integrantes:
- Brayan Steven Arellano Espinosa 
COD: 20191020151
- Hanna Caroline Villamil Ortiz
COD: 20161150007
- Jorge Daniel Gomez Vanegas
COD: 20161020101

##### Descripción del juego
**Perfect Rithm** es un videojuego de ritmo para navegador, el cual cuenta con una jugabilidad fácil de entender pero difícil de dominar, mejora tu precisión, rompe tu record personal, juega mapas de mayor dificultad o escala en la clasificación general.

##### Desarrollo del juego y herramientas a utilizar
El proyecto es desarrollado haciendo uso de tecnologías web, contando con diversos paradigmas de programación como lo son la programación imperativa, programación declarativa y scripting. Al ser basado en la web este se divide en un cliente, un servidor python y un motor de base de datos:
 
**Cliente** 
El cliente del aplicativo se basa en HTML5, CSS3 y Javascript. Se implementa el framework Phaser 3 para la presentación y lógica del juego.
 
**Backend**
El backend se encarga de enviar al cliente todos los datos que necesite, para lo cual se despliega un servidor python usando Flask, el cual hace uso de las herramientas que ofrece la librería para recibir, procesar y contestar las peticiones que se puedan generar desde el cliente.
 
**Base de Datos** 
El aplicativo permite el registro de usuarios así como el de sus respectivas puntuaciones, para lo cual se implementa el motor de bases de datos PostgreSQL, el cual se conecta al servidor mediante Psycopg2.

**Parte imperativa**
Se trabaja sobre todo en la parte del servidor enfocada al manejo de peticiones que llegan desde el cliente.
 
**Parte declarativa**
El paradigma se implementa en el sistema de recomendación de canciones, el cual hará uso de datos históricos del jugador para sugerir canciones que se adapten a su nivel de habilidad.
