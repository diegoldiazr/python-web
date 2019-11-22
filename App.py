## archivo inicial de la aplicacion
from flask import Flask

app = Flask(__name__)

##debug = true hace que el servidor se reinicie con cada cambio
if __name__ == '__main__':
    app.run(port=3000, debug=True)

