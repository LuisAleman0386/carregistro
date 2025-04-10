from app import app

# Crear la instancia de la aplicación


# Para que arranque servidor
if __name__ == '__main__':
    # Se mantiene en escucha por los cambios
    app.run(host="127.0.0.1", port=3000, debug=True)