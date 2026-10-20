
from flask import Flask, render_template_string
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "usuario"),
            password=os.getenv("DB_PASSWORD", "clave123"),
            database=os.getenv("DB_NAME", "holamundo")
        )
        conexion.close()
        estado = "Conexión con MySQL exitosa."
    except Exception as error:
        estado = "No se pudo conectar con MySQL."

    with open("src/index.html", "r", encoding="utf-8") as archivo:
        pagina = archivo.read()

    return pagina.replace(
        '<p id="estado">Conectando con la base de datos...</p>',
        f'<p id="estado">{estado}</p>'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
