from flask import Flask
from database import criar_tabelas
from controllers.rotas import biblioteca_bp
import os


app = Flask(__name__)

criar_tabelas()
app.register_blueprint(biblioteca_bp)

@app.route("/")
def home():
    return "OK"

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



