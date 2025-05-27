from flask import Flask, render_template, request, redirect
from flask import flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'doacoes-alagoas-123456'

# Banco de dados
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS instituicoes (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                cidade TEXT,
                necessidade TEXT,
                pix TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS doacoes (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    contato TEXT,
                    item TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instituicoes', methods=['GET', 'POST'])
def instituicoes():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        cidade = request.form['cidade']
        necessidade = request.form['necessidade']
        pix = request.form['pix']
        c.execute("INSERT INTO instituicoes (nome, cidade, necessidade) VALUES (?, ?, ?)", 
                  (nome, cidade, necessidade, pix))
        conn.commit()
        flash('Ponto de apoio cadastrado com sucesso!')

    
    c.execute("SELECT * FROM instituicoes")
    instituicoes = c.fetchall()
    conn.close()
    return render_template('instituicoes.html', instituicoes=instituicoes)

@app.route('/doadores')
def doadores():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM doacoes")
    doadores = c.fetchall()
    conn.close()
    return render_template('doadores.html', doadores=doadores)



@app.route('/doar', methods=['GET', 'POST'])
def doar():
    if request.method == 'POST':
        nome = request.form['nome']
        contato = request.form['contato']
        item = request.form['item']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO doacoes (nome, contato, item) VALUES (?, ?, ?)", 
                  (nome, contato, item))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('doar.html')

@app.route('/campanhas')
def campanhas():
    campanhas = [
        {'nome': 'Campanha Alagoas Solidária', 'descricao': 'Ajude as vítimas das enchentes.'},
        {'nome': 'Doação de água e mantimentos', 'descricao': 'Itens mais necessários: água, alimentos não perecíveis, roupas.'}
    ]
    return render_template('campanhas.html', campanhas=campanhas)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)
