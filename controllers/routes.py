from flask import Flask, render_template, url_for, request, redirect, session
from controllers.routes import auth_bp
from werkzeug.security import generate_password_hash, check_password_hash

@auth_bp.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    pass

@auth_bp.route('/index')
def index():
    pass

@auth_bp.route('/listar')
def listar():
    pass

@auth_bp.route('/livro', methods=['POST', 'GET'])
def livro():
    pass 