from flask import Flask
from dotenv import load_dotenv
from config import Config
from extensions import db
from rol.rol import rol_bp
from usuario.usuario import usuario_bp

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Registra los Blueprints
app.register_blueprint(rol_bp, url_prefix="/v1")
app.register_blueprint(usuario_bp, url_prefix="/v1")

if __name__ == '__main__':
    app.run(debug=True)