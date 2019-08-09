from flask import Flask, request
import sqlite3
from flask import jsonify
import logging


app = Flask(__name__)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaapp.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@app.route("/escolas", methods=["GET"])
def getEscolas():
    logger.info("Listando escolas.")
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(escola)



@app.route("/escolas/<int:id>", methods=["GET"])
def getEscolaByID(id):
    logger.info("Listando escolas pelo ID.")
    try:
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

        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")
        return jsonify(linha)


    return ("Dados consultados com sucesso.", 200)

@app.route("/escola", methods=["POST"])
def setEscola():
    logger.info("Cadastrando escolas.")
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(escola)

        return ("Cadastro de Escola realizado com sucesso!", 200)


@app.route("/alunos", methods=["GET"])
def getAlunos():
    logger.info("Listando alunos.")
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")
        return jsonify(alunos)

@app.route("/alunos/<int:id>", methods=["GET"])
def getAlunosByID(id):
    logger.info("Listando alunos por ID.")
    try:

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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")
        return jsonify(alunos)

@app.route("/aluno", methods=["POST"])
def setAlunos():
    logger.info("Cadastrando alunos.")

    aluno = request.get_json()

    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['datanasc']
    try:

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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(aluno)

@app.route("/cursos", methods=["GET"])
def getCurso():
    logger.info("Listando cursos.")
    try:

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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(cursos)
        return ("Dados consultados com sucesso.", 200)

@app.route("/cursos/<int:id>", methods=["GET"])
def getCursoByID(id):
    logger.info("Listando cursos pelo ID.")
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(curso)
        return ("Dados consultados com sucesso.", 200)

@app.route("/curso", methods=["POST"])
def setCurso():

    logger.info("Cadastrando curso.")
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']
    try:
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

        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(curso)
        return ("Cadastro de Aluno realizado com sucesso!", 200)

@app.route("/turmas", methods=["GET"])
def getTurma():
    logger.info("Listando Turma.")
    try:

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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")
        return jsonify(turmas)
        return ("Dados consultados com sucesso.", 200)

@app.route("/turmas/<int:id>", methods=["GET"])
def getTurmaByID(id):
    logger.info("Listando Turmas por ID.")
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(linha)
        return ("Dados consultados com sucesso.", 200)

@app.route("/turma", methods=["POST"])
def setTurma():
    logger.info("Cadastrando Turmas.")
    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(turma)
        return ("Cadastro de Aluno realizado com sucesso!", 200)

@app.route("/disciplinas", methods=["GET"])
def getDisciplinas():
    logger.info("Listando disciplinas.")
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(disciplinas)

        return ("Dados consultados com sucesso.", 200)

@app.route("/disciplinas/<int:id>", methods=["GET"])
def getDisciplinaByID(id):
    logger.info("Listando disciplinas por ID.")
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")
        return jsonify(linha)
        return ("Dados consultados com sucesso.", 200)

@app.route("/disciplina", methods=["POST"])
def setDisciplina():
    logger.info("Cadastrando Disciplina.")
    disciplina = request.get_json()
    nome = disciplina['nome']
    try:
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
        execpt(sqlite3.Error):
            logger.error("Aconteceu um erro.")

        return jsonify(disciplina)
        return ("Cadastro de Aluno realizado com sucesso!", 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
