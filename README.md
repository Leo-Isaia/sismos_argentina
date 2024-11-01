<div align="center">
    <img src="https://github.com/Leo-Isaia/sismos_argentina/blob/main/static/icon.png" alt="Icono Aplicación Sismos" style="width:180px;"/>
    <h1>Sismos Argentina</h1>
</div>

<br>

# 🌎💥- Visualizador de Sismos - 😬 🇦🇷 ⚠️

### Herramienta desarrollada con Python, Flask, HTML, CSS y JS 

<br>

<div align="center">
    <img src="https://github.com/Leo-Isaia/sismos_argentina/blob/main/static/ScreenCapture.png" alt="Captura de la Aplicación" style="width:100%;"/>
</div>

Actualmente el proyecto se encuentra desplegado en RENDER para poder probar las funcionalidades:
### **https://sismos-argentina.onrender.com/**

###### Aclaración: como se encuentra alojada en un entorno gratuito de RENDER, es posible que al ingresar haya que esperar 50 segundos a que el servidor donde se encuentra alojado el proyecto "vuelva del estado de suspensión". Luego de esa carga, el tiempo de espera es de microsegundos entre recargas.


<div>
</div>

Para la visualización de los datos en el mapa interactivo se empleó la librería de JavaScript [Leaflet](https://leafletjs.com/), permitiendo así incorporar diversas fuentes de datos, plugins para manipular la información, dibujar, medir y demás posibilidades.

La tabla con los eventos registrados hace uso de la librería de JavaScript DataTables (https://datatables.net/), incorporando así filtros, búsqueda multicolumna, paginación, etc.

La fuente de los datos es la que publica el INPRES vía [CSV](http://contenidos.inpres.gob.ar/formato)
