import psycopg2
import os  # Asegúrate de importar os para usar las variables de entorno

class DAOproyecto:
    def connect(self):
        # Obtener la configuración desde las variables de entorno
        host = os.getenv("DB_HOST", "localhost")  # El valor por defecto es "localhost"
        port = os.getenv("DB_PORT", "5432")      # Puerto por defecto es 5432
        user = os.getenv("DB_USER", "postgres")
        password = os.getenv("DB_PASSWORD", "postgres")
        dbname = os.getenv("DB_NAME", "postgres")

        # Conectar a la base de datos PostgreSQL usando psycopg2
        try:
            return psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                dbname=dbname
            )
        except Exception as e:
            print("Error al conectar con la base de datos:", e)
            return None

    def read_proyecto(self, id=None):
        con = self.connect()
        if con is None:  # Verifica si la conexión falló
            return ()

        cursor = con.cursor()

        try:
            if id is None:
                cursor.execute("SELECT * FROM proyectos ORDER BY id ASC")
            else:
                cursor.execute("SELECT * FROM proyectos WHERE id = %s ORDER BY id ASC", (id,))
            return cursor.fetchall()
        except Exception as e:
            print("Error al ejecutar la consulta:", e)
            return ()
        finally:
            cursor.close()  # Asegúrate de cerrar el cursor
            con.close()      # Cierra la conexión
    def insert_proyecto(self, data):
        con = self.connect()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO proyectos (nombre, descripcion) VALUES (%s, %s)",
                (data['nombre'], data['descripcion'])
            )
            con.commit()
            return True
        except Exception as e:
            print("Error:", e)
            con.rollback()
            return False
        finally:
            con.close()