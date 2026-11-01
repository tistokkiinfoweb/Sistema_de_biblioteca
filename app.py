from flask import Flask, render_template
from controllers.auth import auth_bp
from controllers.livros import livros_bp
from database import banco_de_dados

app = Flask(__name__)

app.secret_key = "AdventureTime ep The Real You"

app.register_blueprint(auth_bp)
app.register_blueprint(livros_bp)

banco_de_dados()

@app.route("/")
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)