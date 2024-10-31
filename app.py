from flask import Flask, render_template
import pandas as pd
import requests
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    # URL del CSV del INPRES
    url = 'http://contenidos.inpres.gob.ar/formatos/sismos30d.csv'  # Cambia esto por la URL real del CSV
    response = requests.get(url)
    
    # Comprobar que la solicitud fue exitosa
    if response.status_code == 200:
        # Leer el contenido del CSV
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        # Procesar el DataFrame para extraer información relevante
        sismos = []
        for index, row in df.iterrows():
            sismos.append({
                'registro': row['Datetime'],  # Cambié a 'Datetime' según tu CSV
                'provincia': row['Region'],  # Cambié a 'Region' según tu CSV
                'profundidad': row['Depth'],  # Cambié a 'Profundidad' según tu CSV
                'ubicacion': row.get('Referencia', 'N/A'),  # 'Referencia' puede no estar presente
                'magnitud': row['Magnitude'],
                'coordenadas': f"{row['Lat']}, {row['Lon']}"  # Asegúrate que 'Lat' y 'Lon' sean correctos
            })

        return render_template('sismos.html', sismos=sismos)
    else:
        return "Error al cargar el archivo CSV", 500

if __name__ == '__main__':
    app.run(debug=True)
