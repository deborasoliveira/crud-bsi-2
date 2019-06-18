import sqlite3 as sql

class Banco(): #CONEXÃO COM O BANCO DE DADOS E AS OPERAÇÕES QUE SERÃO REALIZADAS
    database= "turma.db"
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
    trans.execute("CREATE TABLE IF NOT EXISTS turma (id INTEGER PRIMARY KEY , codt TEXT, codd TEXT, p TEXT, cpfp TEXT, cpfaluno TEXT)")
    trans.persist()
    trans.desconectar()

#FUNÇÕES DA INTERFACE:

def listar(): #EXIBIR TODOS OS DADOS PRESENTES NO BANCO
    trans = Banco()
    trans.conectar()
    trans.execute("SELECT * FROM turma") #SELECIONA TODOS OS ITENS
    rows = trans.fetchall()
    trans.desconectar()
    return rows #EXIBIR USUÁRIOS CADASTRADOS

def cadastrar(nome, cpf): #CADASTRA OS DADOS
    trans = Banco()
    trans.conectar()
    trans.execute("INSERT INTO turma VALUES(NULL, ?,?,?,?,?)", (codt, codd, p, cpfp, cpfa))
    trans.persist()
    trans.desconectar()


def buscar(codt="", codd="", cpfp=""): #BUSCA CADASTRO POR MEIO DE NOME, CPF, CÓDIGO OU DEPARTAMENTO
    trans = Banco()
    trans.conectar()
    trans.execute("SELECT * FROM turma WHERE codt=? or codd=? or cpfp=?", (codt, codd, cpfp))
    rows = trans.fetchall()
    trans.desconectar()
    return rows #RETORNA USUÁRIO SELECIONADO


def deletar(id):
    trans = Banco()
    trans.conectar()
    trans.execute("DELETE FROM turma WHERE id = ?", (id))
    trans.persist()
    trans.desconectar()

def atualizacao(codt, codd, p, cpfp, cpfa):
    trans = Banco()
    trans.conectar()
    trans.execute("UPDATE turma SET codt =?, codd=?, p=?, cpfa=?, cpfp=? WHERE id = ?",(codt, codd, p, cpfa, cpfp))
    trans.persist()
    trans.desconectar()

iniciarDB() #EXECUÇÃO DOS BANCO DE DADOS
