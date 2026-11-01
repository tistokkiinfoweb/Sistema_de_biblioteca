from flask import url_for, request, redirect, render_template
from controllers.livros import livros_bp
from models.models import Livro, Autor
from database import session


@livros_bp.route('/livro', methods=['POST', 'GET'])
def livro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
                
        if not titulo or not autor:
             return redirect(url_for('livros.livro'))
        

        livro = Livro(titulo=titulo, autor_id=autor)

        session.add(livro)
        session.commit()

        return redirect(url_for('livros.listar'))

    autores = session.query(Autor).all()

    return render_template('livros/livro.html', autores=autores)

@livros_bp.route('/autor', methods=['POST', 'GET'])
def autor():
    if request.method == 'POST':
        nome = request.form.get('nome')
                
        if not nome:
             return redirect(url_for('livros.autor'))
        
        autor = Autor(nome=nome)

        session.add(autor)
        session.commit()
 
        return redirect(url_for('livros.livro'))


    return render_template('livros/autor.html')


@livros_bp.route('/listar')
def listar():

    livros = session.query(Livro).all()

    return render_template('livros/listar.html', livros=livros)


@livros_bp.route('/listarA')
def listarA():

    autores = session.query(Autor).all()

    return render_template('livros/listarA.html', autores=autores)