from flask import Flask, request
import sqlite3
from flask import jsonify
import logging


app = Flask(__name__)

@app.route("/escolas", methods=["GET"])
def getEscolas():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_escola;
    """)
    escolas=[]
    for linha in cursor.fetchall():
        escola{
        "id_escola":linha[0],
        "nome":linha[1],
        "logradouro":linha[2],
        "cidade":linha[3]
        ]
        }
        escolas.append(escolas)
    conn.close()
    return jsonify(escola)

@app.route("/escolas/<int:id>", methods=["GET"])
def getEscolaByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_escola WHERE id_escola = ? ;
    """,(id,))
    linha = cursor.fetchone()
    escola = {
        "id_escola": linha[0],
        "nome": linha[1],
        "logradouro": linha[2],
        "cidade": linha[3]
    }
    conn.close()
    return jsonify(linha)
    return ("Dados consultados com sucesso.", 200)

@app.route("/escola", methods=["POST"])
def setEscola():
escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_escola(nome, logradouro, cidade)
        VALUES(?,?,?);
    """, (nome,logradouro, cidade))
    conn.commit()
    conn.close()

    id_escola = cursor.lastrowid
    escola["id_escola"] = id_escola

    return jsonify(escola)

    return ("Cadastro de Escola realizado com sucesso!", 200)

@app.route("/alunos", methods=["GET"])
def getAlunos():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_aluno;
    """)
    alunos = []
    for linha in cursor.fetchall():
        aluno = {
            "id_aluno": linha[0],
            "nome": linha[1],
            "matricula": linha[2],
            "cpf": linha[3],
            "nascimento": linha[4],
        }
        alunos.append(aluno)
    conn.close()
    return jsonify(alunos)

@app.route("/alunos/<int:id>", methods=["GET"])
def getAlunosByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_aluno WHERE id_aluno = ?;
    """,(id,))
    alunos=[]
    for linha in cursor.fetchall():
        aluno = {
            "id_aluno": linha[0],
            "nome": linha[1],
            "matricula": linha[2],
            "cpf": linha[3],
            "nascimento": linha[4],
        }
        alunos.append(aluno)
    conn.close()
    return jsonify(alunos)

@app.route("/aluno", methods=["POST"])
def setAlunos():

    aluno = request.get_json()

    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['datanasc']
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
        VALUES(?,?,?,?);
    """, (nome,matricula, cpf, nascimento))
    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno["id"] = id

    return jsonify(aluno)

@app.route("/cursos", methods=["GET"])
def getCurso():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_curso;
    """)
     cursos = []

    for linha in cursor.fetchall():
        curso = {
            "id_curso" : linha[0],
            "nome" : linha[1],
            "turno" : linha[2]
        }
        cursos.append(curso)

    conn.close()

    return jsonify(cursos)
    return ("Dados consultados com sucesso.", 200)

@app.route("/cursos/<int:id>", methods=["GET"])
def getCursoByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_curso WHERE id_curso = ?;
    """,(id,))
    linha = cursor.fetchone()
    curso = {
        "id_curso" : linha[0],
        "nome" : linha[1],
        "turno" : linha[2]
    }
    conn.close()

    return jsonify(curso)
    return ("Dados consultados com sucesso.", 200)

@app.route("/curso", methods=["POST"])
def setCurso():
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_curso(nome, turno)
        VALUES(?,?);
    """, (nome, turno))
    conn.commit()
    conn.close()

     id = cursor.lastrowid
    curso["id_curso"] = id

    return jsonify(curso)
    return ("Cadastro de Aluno realizado com sucesso!", 200)

@app.route("/turmas", methods=["GET"])
def getTurma():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM tb_turma;
    """)
    turmas = []
    for linha in cursor.fetchall():
        turma = {
            "id_turma" : linha[0],
            "nome" : linha[1],
            "curso" : linha[2]
        }
        turmas.append(turma)

    conn.close()
    return jsonify(turmas)
    return ("Dados consultados com sucesso.", 200)

@app.route("/turmas/<int:id>", methods=["GET"])
def getTurmaByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_turma WHERE id_turma = ?;
    """, (id,))
     linha = cursor.fetchone()
    turma = {
        "id_turma" : linha[0],
        "nome" : linha[1],
        "curso" : linha[2]
    }
    conn.close()

    return jsonify(linha)
    return ("Dados consultados com sucesso.", 200)

@app.route("/turma", methods=["POST"])
def setTurma():
    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_turma(nome, curso)
        VALUES(?,?);
    """, (nome,curso))
    conn.commit()
    conn.close()
     id = cursor.lastrowid
    turma["id_turma"] = id

    return jsonify(turma)
    return ("Cadastro de Aluno realizado com sucesso!", 200)

@app.route("/disciplinas", methods=["GET"])
def getDisciplinas():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM tb_disciplina;
    """)
    disciplinas = []
    for linha in cursor.fetchall():
        disciplina = {
            "id_disciplina" : linha[0],
            "nome" : linha[1]
        }
        disciplinas.append(disciplina)
    conn.close()

    return jsonify(disciplinas)

    return ("Dados consultados com sucesso.", 200)

@app.route("/disciplinas/<int:id>", methods=["GET"])
def getDisciplinaByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_disciplina WHERE id_disciplina = ?;
    """, (id,))
    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    linha = cursor.fetchone()
    disciplina = {
        "id_disciplina" : linha[0],
        "nome" : linha[1]
    }
    conn.close()
    return jsonify(linha)
    return ("Dados consultados com sucesso.", 200)

@app.route("/disciplina", methods=["POST"])
def setDisciplina():
    disciplina = request.get_json()
    nome = disciplina['nome']
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_disciplina(nome)
        VALUES(?);
    """, (nome,))
    conn.commit()
    conn.close()
    id = cursor.lastrowid
    disciplina["id_disciplina"] = id

    return jsonify(disciplina)
    return ("Cadastro de Aluno realizado com sucesso!", 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
