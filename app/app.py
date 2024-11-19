from flask import Flask, render_template
from dao.DAOproyecto import DAOproyecto

app = Flask(__name__)

# Clave secreta para la gestión de sesiones y mensajes flash
app.secret_key = 'mi_clave_secreta_unica'

@app.route('/')
def home():
    # Llama al método 'read_proyecto' para obtener los proyectos
    proyectos = DAOproyecto().read_proyecto()
    
    # Si la consulta a la base de datos falla, inicializamos la lista con valores de error
    if not proyectos:
        proyectos = [["error", "error"], ["error", "error"], ["error", "error"], ["error", "error"]]  # Lista con errores

    return render_template("index.html", proyectos=proyectos)  # Renderiza la plantilla index.html

if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5000 y habilita el modo debug
    app.run(port=5000, host="0.0.0.0", debug=True)
