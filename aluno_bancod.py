import sqlite3 as sql

class Banco(): #CONEXÃO COM O BANCO DE DADOS E AS OPERAÇÕES QUE SERÃO REALIZADAS
    database= "aluno.db"
    conn= None
    cur= None
    connected= False

    def conectar(self): #CONEXÃO COM O BANCO DE DADOS
        Banco.conn = sql.connect(Banco.database)
        Banco.cur = Banco.conn.cursor()
        Banco.connected = True

    def desconectar(self): #FINALIZA A CONEXÃO
        Banco.conn.close()
        Banco.connected = False

    def execute(self, sql, parms = None): #EXECUTA ALGUM COMANDO DO BANCO
        if Banco.connected:
            if parms == None:
                Banco.cur.execute(sql)
            else:
                Banco.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self): #RECUPERA OS VALORES RECEBIDOS DE UM COMANDO
        return Banco.cur.fetchall()

    def persist(self): #GRAVA DADOS INSERIDOS NA BASE
        if Banco.connected:
            Banco.conn.commit()
            return True
        else:
            return False



def iniciarDB(): #CRIANDO O BANCO DE DADOS E SE CONCTANDO À LISTA DE ALUNOS
    trans = Banco()
    trans.conectar()
    trans.execute("CREATE TABLE IF NOT EXISTS aluno (id INTEGER PRIMARY KEY , nome TEXT, cpf TEXT)")
    trans.persist()
    trans.desconectar()

#FUNÇÕES DA INTERFACE:

def listar(): #EXIBIR TODOS OS DADOS PRESENTES NO BANCO
    trans = Banco()
    trans.conectar()
    trans.execute("SELECT * FROM aluno") #SELECIONA TODOS OS ITENS
    rows = trans.fetchall()
    trans.desconectar()
    return rows #EXIBIR USUÁRIOS CADASTRADOS

def cadastrar(nome, cpf): #CADASTRA OS DADOS
    trans = Banco()
    trans.conectar()
    trans.execute("INSERT INTO aluno VALUES(NULL, ?,?)", (nome, cpf))
    trans.persist()
    trans.desconectar()


def buscar(nome="", cpf=""): #BUSCA CADASTRO POR MEIO DE NOME, CPF, CÓDIGO OU DEPARTAMENTO
    trans = Banco()
    trans.conectar()
    trans.execute("SELECT * FROM aluno WHERE nome=? or cpf=?", (nome, cpf))
    rows = trans.fetchall()
    trans.desconectar()
    return rows #RETORNA USUÁRIO SELECIONADO


def deletar(id):
    trans = Banco()
    trans.conectar()
    trans.execute("DELETE FROM aluno WHERE id = ?", (id))
    trans.persist()
    trans.desconectar()

def atualizacao(id, nome, cpf):
    trans = Banco()
    trans.conectar()
    trans.execute("UPDATE aluno SET nome =?, cpf=? WHERE id = ?",(nome, cpf, id))
    trans.persist()
    trans.desconectar()

iniciarDB() #EXECUÇÃO DOS BANCO DE DADOS
