from flask import url_for, request, redirect, render_template,session as flask_session
from controllers.auth import auth_bp
from models.models import Livro, Autor, Usuario
from database import session
from werkzeug.security import generate_password_hash, check_password_hash



@auth_bp.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            return redirect(url_for('auth.cadastro'))

        senha = generate_password_hash(senha)

        usuario = Usuario(nome=nome, email=email, senha=senha)

        session.add(usuario)
        session.commit()

        return redirect(url_for('index'))

    return render_template('auth/cadastro.html')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = session.query(Usuario).filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):

            flask_session['usuario'] = usuario.email

            return redirect(url_for('index'))

        return redirect(url_for('auth.login'))

    return render_template('auth/login.html')
